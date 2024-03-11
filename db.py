from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import DeclarativeBase
from dotenv import load_dotenv
import os
load_dotenv()  # take environment variables from .env. need to install python-dotenv and need to give path as argument if .env is not in the same directory

engine=create_async_engine(
    url=os.getenv("DATABASE_URL"),
    echo = True
)

class Base(DeclarativeBase):
    pass