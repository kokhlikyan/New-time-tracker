import logging

from storage.database import session_factory
from storage.models import Session


def delete_session(session_id: int):
    with session_factory() as session:
        session_to_delete = session.query(Session).filter_by(id=session_id).first()
        if session_to_delete:
            session.delete(session_to_delete)
            session.commit()
            logging.info('Session is deleted')
        else:
            logging.error(f'Session with ID {id} does not exist')
