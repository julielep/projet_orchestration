"""app_api/api.py"""

from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from dotenv import load_dotenv

import crud as crud
import schemas as sc

from Database.database import engine, SessionLocal, Base

load_dotenv()
Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def root():
    return {"message": "API is running 🚀"}


@app.post("/data/", response_model=sc.Data)
def create_data(data: sc.DataCreate, db: Session = Depends(get_db)):
    return crud.create_data(db=db, data=data)


@app.get("/data/", response_model=list[sc.Data])
def read_data(db: Session = Depends(get_db)):
    return crud.get_all_data(db=db)