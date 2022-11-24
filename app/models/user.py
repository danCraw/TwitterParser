from app.models.base import BaseSchema


class UserBase(BaseSchema):
    twitter_id: int
    name: str
    username: str
    following_count: str
    followers_count: str
    description: str


class UserIn(UserBase):
    pass


class UserOut(UserBase):
    pass
