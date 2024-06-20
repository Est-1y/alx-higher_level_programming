#!/usr/bin/python3
"""
class definition of a State and an instance
"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, create_engine


# declarative_base
Base = declarative_base()


class State(Base):
    """
    states table
    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, nullable=False,
                autoincrement=True)
    name = Column(String(128), nullable=False)
