from typing import Dict, Type, Union

import sqlalchemy
from asyncpg import UndefinedTableError

from app.db.repositories.base import BaseRepository
from app.db.tables.status import Status
from app.models.base import BaseSchema
from app.models.status import StatusIn, StatusOut


class StatusRepository(BaseRepository):
    @property
    def _table(self) -> sqlalchemy.Table:
        return Status

    @property
    def _schema_out(self) -> Type[StatusOut]:
        return StatusOut

    @property
    def _schema_in(self) -> Type[StatusIn]:
        return StatusIn

    async def create(self, values: Union[BaseSchema, Dict]) -> _schema_out:
        if isinstance(values, dict):
            values = self._schema_in(**values)
        dict_values = dict(values)
        try:
            record_id = await self._db.execute(query=self._table.insert(), values=dict_values)
        except UndefinedTableError as e:
            raise e
        return record_id

    async def get_id(self, accounts: Union[str]) -> _schema_out:
        row = await self._db.fetch_one(query=self._table.select().where(self._table.c.accounts == accounts))
        if row:
            return self._schema_out(**dict(dict(row).items()))
        else:
            return row
