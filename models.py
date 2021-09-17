from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Dialogue(Base):
    __tablename__ = "dialogue"
    id = Column(Integer, primary_key=True)
    statement = Column(String)
    choices = Column(String)
