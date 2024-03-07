#!/usr/bin/python3

import uuid
from datetime import datetime
from models import storage

class BaseModel:
    
    def __init__(self, **kwargs):
        if kwargs:
            format_style = '%Y-%m-%dT%H:%M:%S.%f'
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)
                if key == 'created_at':
                    self.created_at = datetime.strptime(value, format_style)
                if key == 'updated_at':
                    self.updated_at = datetime.strptime(value, format_style)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        return "[{}] ({}) {}".format(type(self).__name__, self.id, self.__dict__)

    def save(self):
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = type(self).__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict
