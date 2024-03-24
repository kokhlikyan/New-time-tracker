import os
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from sqlalchemy import create_engine
from core.config import APP_LOCAL_FOLDER
from .models import Base
sync_engine = create_engine(
    url=f'sqlite:///{APP_LOCAL_FOLDER}/storage.db',
    echo=False
)

session_factory = sessionmaker(sync_engine)


def init():
    # Base.metadata.drop_all(sync_engine)
    Base.metadata.create_all(sync_engine)

