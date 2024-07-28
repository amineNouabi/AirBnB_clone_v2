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
        place_amenities = relationship("Place", secondary=place_amenity,
                                       back_populates="amenities")
    else:
        name = ""

    def __init__(self, *args, **kwargs):
        """ Initializes an amenity """
        super().__init__(*args, **kwargs)

    if HBNB_TYPE_STORAGE != 'db':
        @property
        def place_amenities(self):
            """Getter attribute in case of file storage"""
            import models
            return [place_amenity for place_amenity
                    in models.storage.all("Place").values()
                    if place_amenity.amenity_id == self.id]
