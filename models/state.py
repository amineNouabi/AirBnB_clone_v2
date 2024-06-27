#!/usr/bin/python3
""" State Module for HBNB project """
from models.__init__ import HBNB_TYPE_STORAGE
from models.base_model import BaseModel, Base
from models.city import City

from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """

    if HBNB_TYPE_STORAGE == 'db':
        __tablename__ = "states"
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state", cascade="all, delete")

    elif HBNB_TYPE_STORAGE == 'file':
        name = ""

    def __init__(self, *args, **kwargs):
        """ Initializes a state """
        super().__init__(*args, **kwargs)

    @property
    def cities(self):
        """Returns the list of City instances with state_id
            equal to the current State.id"""
        from models import storage

        cities = storage.all(City)
        return cities.values().filter(lambda city: city.state_id == self.id)
