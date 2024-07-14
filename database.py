from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

engine = create_engine('postgresql://postgres:080550@localhost:5432/n_41fastapi')

Base = declarative_base()
session = sessionmaker()
