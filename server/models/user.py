from typing import Optional
from pydantic import typing
from pydantic import BaseModel
from typing import Optional, List


class UserBase(BaseModel):
    first: str
    last: str
    middle: Optional[str] = None
    born: int


class UserCreate(UserBase):
    email: str


class User(UserCreate):
    id: str
