#!/usr/bin/python3
""" Amenity Model for HBNB project """

from sqlalchemy import Column, String

from models import HBNB_TYPE_STORAGE
from models.base_model import BaseModel


class Amenity(BaseModel):
    """ The amenity class, contains name """

    if HBNB_TYPE_STORAGE == 'db':
        __tablename__ = "amenities"
        name = Column(String(128), nullable=False)
    else:
        name = ""

    def __init__(self, *args, **kwargs):
        """ Initializes an amenity """
        super().__init__(*args, **kwargs)
