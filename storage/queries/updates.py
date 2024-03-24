from sqlalchemy import update

from storage.database import session_factory
from storage.models import Session, TimeTrack
from storage.models import TimeTrack
from storage.database import session_factory
from storage.queries.selects import select_session, get_project


def update_project(project_name, time=None, description=None):
    pass