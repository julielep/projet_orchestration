from pydantic import BaseModel


class DataBase(BaseModel):
    a: float
    b: float


class DataCreate(DataBase):
    pass


class Data(DataBase):
    id: int
    result: float

    class Config:
        orm_mode = True