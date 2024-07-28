#!/usr/bin/python3
""" Amenity Model for HBNB project """

from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from models import HBNB_TYPE_STORAGE
from models.base_model import BaseModel, Base


class Amenity(BaseModel, Base):
    """ The amenity class, contains name """

    if HBNB_TYPE_STORAGE == 'db':
        from models.place import place_amenity

        __tablename__ = "amenities"
        name = Column(String(128), nullable=False)
        place_amenities = relationship("Place", secondary=place_amenity)
    else:
        name = ""

    def __init__(self, *args, **kwargs):
        """ Initializes an amenity """
        super().__init__(*args, **kwargs)
