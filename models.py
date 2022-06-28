from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from database import Base


class Class(Base):
    __tablename__ = "CLASS"

    ID = Column(Integer, primary_key=True, index=True)
    CLASS_NAME = Column(String, index=True)

    DATA_CLASS = relationship("DataClass", back_populates="OWNER")


class DataClass(Base):
    __tablename__ = "DATACLASS"

    ID_DATA = Column(Integer, primary_key=True, index=True)
    SAINT_NAME = Column(String, index=True)
    LAST_NAME = Column(String, index=True)
    FIRST_NAME = Column(String, index=True)
    CLASS = Column(String, index=True)
    CLASS_ID = Column(Integer, ForeignKey("CLASS.ID"))

    DATA_STU = relationship("Point", back_populates="DATA_ONE")
    OWNER = relationship("Class", back_populates="DATA_CLASS")
    DATA_PRE= relationship("Presence", back_populates="PRE_ONE")


class Point(Base):
    __tablename__ = "POINTSTABLE"

    ID_POINT = Column(Integer, primary_key=True, index=True)
    MINS_15 = Column(String, index=True)
    MINS_45 = Column(String, index=True)
    SEMI_POINT = Column(String, index=True)
    STU_ID = Column(Integer, ForeignKey("DATACLASS.ID_DATA"))

    DATA_ONE = relationship("DataClass", back_populates="DATA_STU")

class Presence(Base):
    __tablename__ = "PRESENCE"

    ID_PRE = Column(Integer, primary_key=True, index=True)
    WEEK_1 = Column(String, index=True)
    WEEK_2 = Column(String, index=True)
    WEEK_3 = Column(String, index=True)
    WEEK_4 = Column(String, index=True)
    WEEK_5 = Column(String, index=True)
    STU_ID = Column(Integer, ForeignKey("DATACLASS.ID_DATA"))

    PRE_ONE = relationship("DataClass", back_populates="DATA_PRE")