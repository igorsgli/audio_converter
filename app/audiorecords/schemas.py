from pydantic import UUID4, BaseModel


class SAudioInfo(BaseModel):
    id: UUID4
    user: UUID4
    filename: str

    class Config:
        orm_mode = True
