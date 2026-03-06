from pydantic import BaseModel, ConfigDict


class DataBase(BaseModel):
    a: float
    b: float


class DataCreate(DataBase):
    pass


class Data(DataBase):
    id: int
    result: float

    model_config = ConfigDict(from_attributes=True)
