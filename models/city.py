#!/usr/bin/python3
""" City Module for HBNB project """
import models
from models.base_model import BaseModel, Base
from models.place import Place

from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class City(BaseModel, Base):
    """ The city class, contains state ID and name """

    if models.HBNB_TYPE_STORAGE == 'db':
        __tablename__ = "cities"
        state_id = Column(String(60), ForeignKey(
            'states.id', name='cities_ibfk_1'), nullable=False)
        name = Column(String(128), nullable=False)
        places = relationship("Place", backref="cities", cascade="all, delete")

    else:
        state_id = ""
        name = ""

    def __init__(self, *args, **kwargs):
        """ Initializes a city """
        super().__init__(*args, **kwargs)

    if models.HBNB_TYPE_STORAGE != 'db':
        @property
        def places(self):
            """Getter attribute in case of file storage"""
            place_list = []
            for place in models.storage.all(Place).values():
                if place.city_id == self.id:
                    place_list.append(place)
                return place_list
