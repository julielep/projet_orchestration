from sqlalchemy import Column, Integer, Float

from Database.database import Base


class Data(Base):
    __tablename__ = "data"
    id = Column(Integer, primary_key=True, index=True)
    a = Column(Float)
    b = Column(Float)
    result = Column(Float)
