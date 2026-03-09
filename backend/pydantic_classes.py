from datetime import datetime, date, time
from typing import Any, List, Optional, Union, Set
from enum import Enum
from pydantic import BaseModel, field_validator


############################################
# Enumerations are defined here
############################################

class Genre(Enum):
    Technology = "Technology"
    Cookbooks = "Cookbooks"
    Poetry = "Poetry"
    Horror = "Horror"
    Philosophy = "Philosophy"
    Adventure = "Adventure"
    Fantasy = "Fantasy"
    History = "History"
    Romance = "Romance"
    Thriller = "Thriller"

############################################
# Classes are defined here
############################################
class AuthorCreate(BaseModel):
    birth: date
    name: str
    books: List[int]  # N:M Relationship


class LibraryCreate(BaseModel):
    telephone: str
    name: str
    address: str
    web_page: str
    books: List[int]  # N:M Relationship


class BookCreate(BaseModel):
    title: str
    release: date
    genre: Genre
    stock: int
    pages: int
    price: float
    library: List[int]  # N:M Relationship
    authors: List[int]  # N:M Relationship

    @field_validator('pages')
    @classmethod
    def validate_pages_1(cls, v):
        """OCL Constraint: constraint_Book_1_1"""
        if not (v < 10000):
            raise ValueError('pages must be < 10000')
        return v
    @field_validator('pages')
    @classmethod
    def validate_pages_2(cls, v):
        """OCL Constraint: constraint_Book_0_1"""
        if not (v > 10):
            raise ValueError('pages must be > 10')
        return v

