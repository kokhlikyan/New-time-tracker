from storage.database import session_factory
from storage.models import Session, TimeTrack
from sqlalchemy import desc, update
from helpers.main import generate_token
from storage.queries.selects import get_project


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
                update_values['time'] =  time
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
