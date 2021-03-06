from sqlalchemy import Column, ForeignKey, Integer, String, Boolean, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from datetime import datetime

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
    last_name = Column(String(250), nullable=False)
    authority_level = Column(Integer) 
    power_key = Column(String(500))
    telegram_id = Column(Integer)
    is_human = Column(Boolean, unique=False, default=True)


class Topic(Base):
    __tablename__ = 'topics'
    id = Column(Integer, primary_key=True)
    topic = Column(String(250))
    abstract = Column(String(500))
    public_opinion = Column(String(500), nullable=False)
    is_active = Column(Boolean,unique=False, default=True)

class Message(Base):
    __tablename__ = 'messages'
    id = Column(Integer, primary_key=True)
    text = Column(String)
    time = Column(DateTime)
    reference_id = Column(String(50))
    channel = Column(String(50))

class BibleVerse(Base):
    __tablename__ = 'bible'
    id = Column(Integer, primary_key=True)
    book = Column(String)
    chapter = Column(String)
    verse = Column(String)
    content = Column(String)






