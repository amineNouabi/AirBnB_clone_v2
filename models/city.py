#!/usr/bin/python3
""" City Module for HBNB project """
from models.__init__ import HBNB_TYPE_STORAGE
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey


class City(BaseModel, Base):
    """ The city class, contains state ID and name """

    if HBNB_TYPE_STORAGE == 'db':
        __tablename__ = "cities"
        state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
        name = Column(String(128), nullable=False)

    elif HBNB_TYPE_STORAGE == 'file':
        state_id = ""
        name = ""

    def __init__(self, *args, **kwargs):
        """ Initializes a city """
        super().__init__(*args, **kwargs)
