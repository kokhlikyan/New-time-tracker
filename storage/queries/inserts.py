from storage.database import session_factory
from storage.models import Session, TimeTrack, MouseEvents
from sqlalchemy import desc, update
from helpers.main import generate_token
from storage.queries.selects import get_project, get_mouse_events


def auth():
    with session_factory() as session:
        new_session = Session(
            token=generate_token()
        )
        session.add(new_session)
        session.commit()


def create_or_update(project_name, time=None, description=None):
    with session_factory() as session:
        project = get_project(project_name)
        if project is not None:
            update_values = {}
            if time is not None:
                update_values['time'] = time
            if description is not None:
                update_values['description'] = description

            if update_values:
                stmt = (
                    update(TimeTrack)
                    .where(TimeTrack.project == project_name)
                    .values(**update_values)
                )
                res = session.execute(stmt)
        else:
            new_project = TimeTrack(
                project=project_name,
                time=time
            )
            session.add(new_project)
        session.commit()


def create_or_update_mouse_event(track_id: int, left: int, right: int) -> MouseEvents:
    with session_factory() as session:
        mouse_event = get_mouse_events(track_id)
        if mouse_event is not None:
            update_values = {
                'left': left,
                'right': right,
            }

            if update_values:
                stmt = (
                    update(MouseEvents)
                    .where(MouseEvents.time_tracks_id == track_id)
                    .values(**update_values)
                )
                session.execute(stmt)
        else:
            new_mouse_event = MouseEvents(
                time_tracks_id=track_id,
                left=left,
                right=right
            )
            session.add(new_mouse_event)
        session.commit()
