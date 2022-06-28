from typing import List, Optional

import uvicorn
from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session

import crud
import models
import readExcel
import schemas

from database import engine, get_db

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get("/classes", response_model=List[schemas.Class])
def get_classes(db: Session = Depends(get_db), skip: Optional[int] = 0, limit: Optional[int] = 100):
    db_users = crud.get_all_classes(db=db, skip=skip, limit=limit)
    return db_users


@app.get("/class/{class_name}", response_model=schemas.Class)
def get_class(class_name: str, db: Session = Depends(get_db)):
    db_return = crud.get_class_by_name(db=db, class_name=class_name)
    return db_return

isRun = True
if isRun:
    name_files, danh_sach = readExcel.updateOrInsertExcel()


    @app.post("/create-class")
    def create_user(db: Session = Depends(get_db)):
        for name in name_files:
            class_name = name.replace(" ", "_")
            data_return = crud.get_class_by_name(db=db, class_name=class_name)
            if data_return:
                continue
            crud.create_class(db=db, class_name=class_name)
        db.commit()
        return {"detail": "All Done!"}


    @app.post("/create-data")
    def create_data(db: Session = Depends(get_db)):
        for thieu_nhi in danh_sach:
            class_name = thieu_nhi["OWNER"]
            data_return = crud.get_class_by_name(db=db, class_name=class_name)
            if data_return:
                crud.create_data(db=db, saint=thieu_nhi["SAINT_NAME"], last=thieu_nhi["LAST_NAME"],
                                 first=thieu_nhi["FIRST_NAME"], clasz=thieu_nhi["CLASS"], class_id=data_return.ID)
        db.commit()
        return {"detail": "All Done!"}


    @app.post("/class/data/pre")
    def create_pre( db: Session = Depends(get_db)):
        for i in range(1, 762):
            crud.create_pre(db=db, week1="", week2="", week3="", week4="",week5="",data_id=i)
        db.commit()
        return {"detail": "All Done!"}


@app.post("/class/data/point", response_model=schemas.Point)
def create_point(id_data: int,point: schemas.PointCreate, db: Session = Depends(get_db)):
    data_return = crud.get_data_by_id(db=db, id_data=id_data)
    if data_return != None:
        data = crud.create_point(db=db, point=point, data_id=data_return.ID_DATA)
        db.commit()
        return data


@app.get("/stu/{id_stu}", response_model=schemas.Data)
def get_data_stu(id_stu: int, db: Session = Depends(get_db)):
    data = crud.get_data_by_id(db=db,id_data=id_stu)
    return data


if __name__ == "__main__":
    uvicorn.run("main:app", port=8001)
