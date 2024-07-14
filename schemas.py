from typing import Optional

from pydantic import BaseModel


class RegisterUser(BaseModel):
    username: str
    password: str
    email: str
    confirm_password: str
    first_name: Optional[str]
    last_name: Optional[str]

    class Config:
        from_attribute = True


class UserOut(BaseModel):
    id: str
    username: str
    email: str
    first_name: Optional[str]
    last_name: Optional[str]


class LoginUser(BaseModel):
    username: str
    password: str


class DeleteUser(BaseModel):
    username: str
