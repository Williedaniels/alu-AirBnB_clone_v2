#!/usr/bin/python3
""" State Module for HBNB project """
import os

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.city import City
import models


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'

    name = Column(String(128), nullable=False)

    if os.getenv("HBNB_TYPE_STORAGE") == "db":
        cities = relationship('City', backref='state',
                              cascade='all, delete-orphan')

    else:
        @property
        def cities(self):
            """ Returns the list of City instances with state_id
            equals to the current State.id. """
            return [city for city in models.storage.all(City).values()
                    if city.state_id == self.id]

    @classmethod
    def create_state(cls, California):
        """ Creates a State instance with the given name """
        if 'name' in California:
            new_state = cls(California))
            models.storage.new(new_state)
            models.storage.save()
            return new_state
        else:
            print("Error: 'name' is a required argument.")
            return None
