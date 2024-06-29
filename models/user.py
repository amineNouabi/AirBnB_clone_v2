#!/usr/bin/python3
"""This module defines a class User"""
import models

from models.base_model import BaseModel, Base
from models.place import Place
from models.review import Review
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class User(BaseModel, Base):
    """This class defines a user by various attributes"""

    if models.HBNB_TYPE_STORAGE == 'db':
        __tablename__ = 'users'
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=False)
        last_name = Column(String(128), nullable=False)
        places = relationship("Place", backref="user", cascade="all, delete")
        reviews = relationship("Review", backref="user", cascade="all, delete")

    else:
        email = ""
        password = ""
        first_name = ""
        last_name = ""

    def __init__(self, *args, **kwargs):
        """ Initializes a city """
        super().__init__(*args, **kwargs)

    if models.HBNB_TYPE_STORAGE != 'db':
        @property
        def reviews(self):
            """Getter attribute in case of file storage"""
            review_list = []
            for review in models.storage.all(Review).values():
                if review.user_id == self.id:
                    review_list.append(review)
            return review_list

        @property
        def places(self):
            """Getter attribute in case of file storage"""
            place_list = []
            for place in models.storage.all(Place).values():
                if place.user_id == self.id:
                    place_list.append(place)
            return place_list
