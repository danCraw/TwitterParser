from typing import Dict, List

from app.models.base import BaseSchema


class StatusBase(BaseSchema):
    accounts: List


class StatusIn(StatusBase):
    pass


class StatusOut(StatusBase):
    pass
