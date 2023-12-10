#!/usr/bin/python3
"""
File: user.py

Author:
    Adeniji Aliu Adeyemi <adenijialiuadeyemi@gmail.com>

Defines a class User
"""
from models.base_model import BaseModel


class User(BaseModel):
    """Class that represents a User inheriting from BaseModel"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
