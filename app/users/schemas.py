from datetime import datetime
from pydantic import UUID4, BaseModel


class SUser(BaseModel):
    username: str

    class Config:
        orm_mode = True


class SUserInfo(BaseModel):
    id: UUID4
    access_token: str

    class Config:
        orm_mode = True


class SUserInfoAll(BaseModel):
    id: UUID4
    username: str
    access_token: str
    created_at: datetime

    class Config:
        orm_mode = True
