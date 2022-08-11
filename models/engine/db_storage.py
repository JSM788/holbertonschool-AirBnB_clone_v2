#!/usr/bin/python3
""" Creaction of class db_storage"""
from models.base_model import BaseModel, Base
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class DBStorage:
    """ Creation of class db_storage """
    __engine = None
    __session = None

    def __init__(self):
        """ Inicializacion atributos """
        user = os.getenv('HBNB_MYSQL_USER')
        password = os.getenv('HBNB_MYSQL_PWD')
        host = os.getenv('HBNB_MYSQL_HOST')
        database = os.getenv('HBNB_MYSQL_DB')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
            user,
            password,
            host,
            database),
            pool_pre_ping=True
        )

        if os.getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """ Methods for list the table"""
        dictionary = {}
        classes = [User, State, City, Place, Review]
        if cls is None:
            for x in classes:
                queryAll = self.__session.query(x)
                for obj in queryAll:
                    key = "{}.{}".format(obj.__class__.__name__, obj.id)
                    dictionary[key] = obj
        else:
            if cls in classes:
                query = self.__session.query(cls).all()
                for obj in query:
                    key = "{}.{}".format(obj.__class__. __name__, obj.id)
                    dictionary[key] = obj
        return dictionary

    def new(self, obj):
        """ methods to add to the DB  """
        self.__session.add(obj)

    def save(self):
        """ method to reflect the changes in the DB """
        self.__session.commit()

    def delete(self, obj=None):
        """ Methods to perform class removal """
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """ method to reload the data to be displayed """
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session

    def close(self):
        """ Method to close the DB connection """
        self.__session.close()
