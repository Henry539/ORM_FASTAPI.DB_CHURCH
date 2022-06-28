from sqlalchemy.orm import Session
from typing import Optional

import models
import schemas


def create_class(db: Session, class_name: str):
    db_class = models.Class(CLASS_NAME=class_name)
    db.add(db_class)
    return db_class


def create_data(db: Session, saint: str, last: str, first: str, clasz: str, class_id: int):
    db_data = models.DataClass(SAINT_NAME=saint, LAST_NAME=last, FIRST_NAME=first, CLASS=clasz, CLASS_ID=class_id)
    db.add(db_data)
    return db_data

def create_pre(*,db: Session, week1: Optional[str]=None, week2: Optional[str]=None, week3: Optional[str]=None, week4: Optional[str]=None,week5:Optional[str]=None , data_id: int):
    db_pre = models.Presence(WEEK_1=week1, WEEK_2=week2, WEEK_3=week3, WEEK_4=week4,WEEK_5=week5, STU_ID=data_id)
    db.add(db_pre)
    return db_pre


def create_point(*,db: Session, point: schemas.PointCreate , data_id: int):
    data_point = models.Point(MINS_15=point.MINS_15, MINS_45=point.MINS_45, SEMI_POINT=point.SEMI_POINT, STU_ID=data_id)
    db.add(data_point)
    return data_point


def get_all_classes(db: Session, skip: int, limit: int):
    return db.query(models.Class).offset(skip).limit(limit).all()


def get_class_by_name(db: Session, class_name: str):
    data = db.query(models.Class).filter(models.Class.CLASS_NAME == class_name).first()
    return data


def get_data_by_id(db: Session , id_data: int):
    data1 = db.query(models.DataClass).filter(models.DataClass.ID_DATA == id_data).first()
    return data1


