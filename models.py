from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


Base = declarative_base()


class Config(Base):
    __tablename__ =  'config'
    key = Column(String(250), nullable=False, primary_key=True)
    value = Column(String(1000), nullable=True)


class Person(Base):
    __tablename__ = 'persons'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    authority_leel = Column(Integer) 
    power_key = Column(String(500))


class Topic(Base):
    __tablename__ = 'topics'
    id = Column(Integer, primary_key=True)
    topic = Column(String(250))
    abstract = Column(String(500))
    public_opinion = Column(String(500), nullable=False)
    is_active = Column(String(250), nullable=False)




