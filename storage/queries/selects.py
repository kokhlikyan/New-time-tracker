from storage.database import session_factory
from storage.models import Session, TimeTrack
from sqlalchemy import desc


def select_session() -> Session:
    with session_factory() as session:
        result = session.query(Session).order_by(desc(Session.id)).first()
        return result


def get_project(project_name) -> TimeTrack:
    with session_factory() as session:
        result = session.query(TimeTrack).filter(TimeTrack.project == project_name).first()
        return result
