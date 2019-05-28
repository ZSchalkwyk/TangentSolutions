import json
from datetime import datetime

import sqlalchemy.orm
from sqlalchemy import (
    Column,
    DateTime,
    ForeignKey,
    Integer,
    String,
    create_engine,
    func
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import create_database, database_exists


def get_engine():
    return sqlalchemy.create_engine('sqlite:///super_quick.db')


db = get_engine()
connection = db.connect()
print(connection)
Base = declarative_base()


class Employee(Base):
    __tablename__ = "Employee"
    id = Column(Integer, autoincrement=True, primary_key=True)
    emp_number = Column(String)
    phone_number = Column(String)
    first_name = Column(String)
    last_name = Column(String)
    leave = relationship("Leave")


class Leave(Base):
    __tablename__ = "Leave"
    id = Column(Integer, autoincrement=True, primary_key=True)
    employee_pk = Column(Integer, ForeignKey('Employee.id'))
    status = Column(String)
    start_date = Column(DateTime)
    end_date = Column(DateTime)
    days_of_leave = Column(Integer)


Base.metadata.create_all(bind=db)
Session = sessionmaker(db)
session = Session()


def get_session():
    Session = sessionmaker(db)
    return Session()
