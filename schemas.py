from typing import List, Optional

from pydantic import BaseModel


class PointCreate(BaseModel):
    MINS_15: Optional[float]=None
    MINS_45: Optional[float]=None
    SEMI_POINT: Optional[float]=None


class Point(PointCreate):
    ID_POINT: int
    STU_ID: int

    class Config:
        orm_mode = True

class PresenceCreate(BaseModel):
    WEEK_1: Optional[str] = None
    WEEK_2: Optional[str] = None
    WEEK_3: Optional[str] = None
    WEEK_4: Optional[str] = None
    WEEK_5: Optional[str] = None

class Presence(PresenceCreate):
    ID_PRE: int
    STU_ID: int

    class Config:
        orm_mode = True


class DataCreate(BaseModel):
    SAINT_NAME: Optional[str] = None
    LAST_NAME: str
    FIRST_NAME: str
    CLASS: str


class Data(DataCreate):
    ID_DATA: int
    CLASS_ID: int
    DATA_STU: List[Point] = []
    DATA_PRE: List[Presence]

    class Config:
        orm_mode = True


class ClassCreate(BaseModel):
    ID: int
    CLASS_NAME: str


class Class(ClassCreate):
    DATA_CLASS: List[Data] = []


    class Config:
        orm_mode = True
