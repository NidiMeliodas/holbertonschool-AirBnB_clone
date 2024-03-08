#!/usr/bin/python3
"""
Module for the User class.
"""


from models.base_model import BaseModel


class User(BaseModel):
    """
    Represents a user.
    """
    def __init__(self, *args, **kwargs):
        """Initialize User instance."""
        super().__init__(*args, **kwargs)
        self.email = kwargs.get('email', "")
        self.password = kwargs.get('password', "")
        self.first_name = kwargs.get('first_name', "")
        self.last_name = kwargs.get('last_name', "")
