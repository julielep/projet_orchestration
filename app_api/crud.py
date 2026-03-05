from sqlalchemy.orm import Session
from app_api.Database import models
import app_api.maths as maths


def create_data(db: Session, data):
    result = maths.add(data.a, data.b)

    db_data = models.Data(
        a=data.a,
        b=data.b,
        result=result
    )

    db.add(db_data)
    db.commit()
    db.refresh(db_data)

    return db_data


def get_all_data(db: Session):
    return db.query(models.Data).all()