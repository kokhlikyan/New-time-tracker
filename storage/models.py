import enum
import datetime

from typing import Annotated, Optional
from sqlalchemy import ForeignKey, text
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase

pk = Annotated[int, mapped_column(primary_key=True)]
created_at = Annotated[datetime.datetime, mapped_column(default=datetime.datetime.utcnow)]
updated_at = Annotated[datetime.datetime, mapped_column(default=datetime.datetime.utcnow,
                                                        onupdate=datetime.datetime.utcnow)]


class Base(DeclarativeBase):
    pass


class Session(Base):
    __tablename__ = 'sessions'

    id: Mapped[pk]
    token: Mapped[Optional[str]]
    created_at: Mapped[created_at]
    updated_at: Mapped[updated_at]


class TimeTrack(Base):
    __tablename__ = 'time_tracks'

    id: Mapped[pk]
    project: Mapped[str]
    description: Mapped[Optional[str]]
    time: Mapped[int]
    created_at: Mapped[created_at]
    updated_at: Mapped[updated_at]


class MouseEvents(Base):
    __tablename__ = 'mouse_events'

    id: Mapped[pk]
    time_tracks_id: Mapped[int] = mapped_column(ForeignKey('time_tracks.id', ondelete='CASCADE'))
    left: Mapped[int]
    right: Mapped[int]


class KeyboardEvents(Base):
    __tablename__ = 'keyboard_events'

    id: Mapped[pk]
    time_tracks_id: Mapped[int] = mapped_column(ForeignKey('time_tracks.id', ondelete='CASCADE'))
    click: Mapped[int]
