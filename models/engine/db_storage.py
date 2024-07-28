#!/usr/bin/python3
"""This module defines a class to manage db storage for hbnb clone"""


from os import getenv
from models.base_model import Base
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session


class DBStorage:
    """This class manages storage of hbnb models in a database"""
    __engine = None
    __session = None

    __classes = {
        'City': City,
        'State': State,
        'User': User,
        'Place': Place,
        'Review': Review
    }

    def __init__(self):
        """Creates the engine"""
        HBNB_MYSQL_USER = getenv('HBNB_MYSQL_USER')
        HBNB_MYSQL_PWD = getenv('HBNB_MYSQL_PWD')
        HBNB_MYSQL_HOST = getenv('HBNB_MYSQL_HOST')
        HBNB_MYSQL_DB = getenv('HBNB_MYSQL_DB')
        HBNB_ENV = getenv('HBNB_ENV')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}?charset=latin1'
                                      .format(HBNB_MYSQL_USER,
                                              HBNB_MYSQL_PWD,
                                              HBNB_MYSQL_HOST,
                                              HBNB_MYSQL_DB),
                                      pool_pre_ping=True,)
        if HBNB_ENV == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        objs = {}
        for cl in self.__classes:
            if not cls or cls is cl or cls is self.__classes[cl]:
                for obj in self.__session.query(self.__classes[cl]).all():
                    objs[obj.__class__.__name__ + '.' + obj.id] = obj
        return objs

    def new(self, obj):
        """Adds new object to storage"""
        self.__session.add(obj)

    def save(self):
        """Commits all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Deletes obj from the current database session"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Creates all tables in the database"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session

    def close(self):
        """Closes the current session"""
        self.__session.remove()

    def close(self):
        """Closes the current session"""
        self.__session.remove()
