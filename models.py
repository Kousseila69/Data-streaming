from sqlalchemy import Column, Integer, Float, String, ForeignKey, DateTime, Date
from sqlalchemy.dialects.mysql import FLOAT as MY_SQL_FLOAT, JSON
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


class clean_log(Base):
    __tablename__ = "clean_log"

    id = Column(String(100), primary_key=True, nullable=False)
    timestamp = Column(String(50), nullable=False)
    year = Column(String(10), nullable=False)
    month = Column(String(15), nullable=False)
    day = Column(String(15), nullable=True)
    day_of_week = Column(String(15), nullable=True)
    time = Column(String(20), nullable=True)
    ip = Column(String(20), nullable=True)
    country = Column(String(15), nullable=True)
    city = Column(String(50), nullable=True)
    session = Column(String(100), nullable=True)
    user = Column(String(50), nullable=True)
    is_email = Column(String(10), nullable=True)
    email_domain = Column(String(15), nullable=True)
    rest_method = Column(String(10), nullable=True)
    url = Column(String(9500), nullable=True)
    schema = Column(String(10), nullable=True)
    host = Column(String(50), nullable=True)
    rest_version = Column(String(20), nullable=True)
    status = Column(Integer, nullable=True)
    status_verbose = Column(String(50), nullable=True)
    size_bytes = Column(Float, nullable=True)
    size_kilo_bytes = Column(Float, nullable=True)
    size_mega_bytes = Column(Float, nullable=True)


class raw_log(Base):
    __tablename__ = "raw_log"

    id = Column(String(100), primary_key=True, nullable=False)
    timestamp = Column(String(50), nullable=False)
    log = Column(String(9500), nullable=False)