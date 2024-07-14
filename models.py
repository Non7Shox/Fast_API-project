from sqlalchemy import Column, Integer, String
from database import Base


class User(Base):
    __tablename__ = 'User'
    id = Column(Integer, primary_key=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    username = Column(String(100), nullable=False, unique=True)
    email = Column(String(100), unique=False)
    password = Column(String(100), nullable=False)

    def __repr__(self):
        return self.username
