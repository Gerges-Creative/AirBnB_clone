#!/usr/bin/python3
""" This script defines the basic attributes and methods for the entire project

The the datetime module is used to store the time at creation and updating.

The UUID module is used to generate uniqe ids for every instance created
for this object.
"""
import datetime
import uuid


class BaseModel:
    """
    This class is the main class used to define all common attributes and
    methods for other classes
    """

    # This cls attr is for the setattr to check if attr assignment has occured
    _is_changed = False

    def __init__(self, *args, **kwargs):
        """
        This the constructor method doesn't recieve any parameters but defines
        all the used ones throughout the project
        """

        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                # setattr is a built-in function that sets the value of an
                # attribute on an object.
                setattr(self, key, value)
                self.created_at = datetime.datetime.fromisoformat(
                    kwargs["created_at"])
                self.updated_at = datetime.datetime.fromisoformat(
                    kwargs["updated_at"])
        else:
            self.my_number = None
            self.name = None
            self.created_at = datetime.datetime.now()
            self.updated_at = self.created_at
            self.id = str(uuid.uuid4())

    def __str__(self):
        """
        The __str__ method is used to return a string of basic info
        """
        if BaseModel._is_changed is True:
            self.updated_at = datetime.datetime.now()
            BaseModel._is_changed = False
        return ("[BaseModel] ({}) {}".format(self.id, self.__dict__))

    # For now its just used as check point to updated time
    def save(self):
        """
        The save method is used to update time for the attribute updated_at
        """
        self.updated_at = datetime.datetime.now()

    def __setattr__(self, key, value):
        """
        The __setattr__ method is used to check if any assignments have occured
        in the object instance
        """
        if key != '_is_changed':
            BaseModel._is_changed is True
        super(BaseModel, self).__setattr__(key, value)

    def to_dict(self):
        """
        The to_dict method is used to modify the format of created_at and
        updated_atand add a new attribute called __class__ to __dict__
        """
        if BaseModel._is_changed is True:
            self.updated_at = datetime.datetime.now()
            BaseModel._is_changed = False

        self.created_at = self.created_at.isoformat()
        self.updated_at = self.updated_at.isoformat()
        # There is another way by making a copy of BaseModel first then modify
        self.__dict__["__class__"] = "BaseModel"
        return self.__dict__
