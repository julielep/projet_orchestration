from sqlalchemy import Column, Float, Integer

from app_api.Database.database import Base


class Data(Base):
    __tablename__ = "data"
    id = Column(Integer, primary_key=True, index=True)
    a = Column(Float)
    b = Column(Float)
    result = Column(Float)
