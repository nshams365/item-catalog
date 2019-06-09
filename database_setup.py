
import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()



class Catagory(Base):

    __tablename__ = 'catagory'

    id = Column(Integer, primary_key = True)
    name = Column(String(80), nullable = False)


class Title(Base):

    __tablename__ = 'title'

    name = Column(String(80), nullable =False)
    id = Column(Integer, primary_key = True)
    author_name = Column(String(250))
    price = Column(String(8))
    catagory_id = Column(Integer, ForeignKey('catagory.id'))
    catagory = relationship(Catagory)

class Audit_trail(Base):

    __tablename__ = 'audit_trail'

    op_time = Column(DateTime, default=func.now())
    title_id = Column(Integer, ForeignKey('title.id'))
    title = relationship(Title)


engine = create_engine('sqlite:///catalog.db')
Base.metadata.create_all(engine)