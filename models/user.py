#!/usr/bin/python3
"""This module defines a class User"""
from models.__init__ import HBNB_TYPE_STORAGE
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String


class User(BaseModel, Base):
    """This class defines a user by various attributes"""

    if HBNB_TYPE_STORAGE == 'db':
        __tablename__ = 'users'
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=False)
        last_name = Column(String(128), nullable=False)

    elif HBNB_TYPE_STORAGE == 'file':
        email = ""
        password = ""
        first_name = ""
        last_name = ""

    def __init__(self, *args, **kwargs):
        """ Initializes a city """
        super().__init__(*args, **kwargs)
