#!/usr/bin/python3
""" class Model """
from sqlalchemy import Integer, String, Column, ForeignKey
from model_state import Base


class City(Base):
    """ for task 14 """

    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'))
