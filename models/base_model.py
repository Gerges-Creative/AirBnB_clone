#!/usr/bin/python3
import datetime, uuid

class BaseModel:

    _is_changed = False
    def __init__(self):
        self.my_number = None
        self.name = None
        self.created_at = datetime.datetime.now()
        self.updated_at = self.created_at
        self.id = str(uuid.uuid4())


    def __str__(self):
        if BaseModel._is_changed == True:
            self.updated_at = datetime.datetime.now()
            BaseModel._is_changed = False
        return ("[BaseModel] ({}) {}".format(self.id, self.__dict__))

    def save(self):
        self.updated_at = datetime.datetime.now()

    def __setattr__(self, key, value):
        if key != '_is_changed':
            BaseModel._is_changed = True
        super(BaseModel, self).__setattr__(key, value)

    def to_dict(self):
        if BaseModel._is_changed == True:
            self.updated_at = datetime.datetime.now()
            BaseModel._is_changed = False

        self.created_at = self.created_at.isoformat()
        self.updated_at = self.updated_at.isoformat()
        # There is another way by making a copy of BaseModel first then modify
        self.__dict__["__class__"] = "BaseModel"
        return self.__dict__
