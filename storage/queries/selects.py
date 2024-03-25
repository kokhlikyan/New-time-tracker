from storage.database import session_factory
from storage.models import Session, TimeTrack,MouseEvents
from sqlalchemy import desc


def select_session() -> Session:
    with session_factory() as session:
        result = session.query(Session).order_by(desc(Session.id)).first()
        return result


def get_project(project_name) -> TimeTrack:
    with session_factory() as session:
        result = session.query(TimeTrack).filter(TimeTrack.project == project_name).first()
        return result


def get_mouse_events(track_id) -> MouseEvents:
    with session_factory() as session:
        result = session.query(MouseEvents).filter(MouseEvents.time_tracks_id == track_id).first()
        return result
