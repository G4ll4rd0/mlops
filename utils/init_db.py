'''
Database Start-Up
'''
from sqlalchemy import Column, Integer, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///./artifacts/data.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

class Credit(Base): # pylint: disable=missing-class-docstring
    __tablename__ = "credit"

    idx = Column(Integer, primary_key=True)
    X1 = Column(Integer)
    X2 = Column(Integer)
    X3 = Column(Integer)
    X4 = Column(Integer)
    X5 = Column(Integer)
    X6 = Column(Integer)
    X7 = Column(Integer)
    X8 = Column(Integer)
    X9 = Column(Integer)
    X10 = Column(Integer)
    X11 = Column(Integer)
    X12 = Column(Integer)
    X13 = Column(Integer)
    X14 = Column(Integer)
    X15 = Column(Integer)
    X16 = Column(Integer)
    X17 = Column(Integer)
    X18 = Column(Integer)
    X19 = Column(Integer)
    X20 = Column(Integer)
    X21 = Column(Integer)
    X22 = Column(Integer)
    X23 = Column(Integer)
    Y = Column(Integer)
