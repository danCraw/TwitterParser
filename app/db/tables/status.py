import json
from typing import Dict

import sqlalchemy
from sqlalchemy import ARRAY, Column, Integer, JSON, PickleType, String, Table, TypeDecorator

from app.db.base import metadata


class TextPickleType(TypeDecorator):
    impl = sqlalchemy.Text(256)

    def process_bind_param(self, value, dialect):
        if value is not None:
            value = json.dumps(value)

        return value

    def process_result_value(self, value, dialect):
        if value is not None:
            value = json.loads(value)
        return value


Status = Table(
    'statuses',
    metadata,
    Column("id", Integer, primary_key=True),
    Column("accounts", ARRAY(TextPickleType()), nullable=False)
)
