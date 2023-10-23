from sqlalchemy.orm import sessionmaker
from db.engine import engine
from db.table import UsersTable


def register(telegram_id, first_name, last_name):
    Session = sessionmaker(bind=engine)
    session = Session()

    user = session.query(UsersTable).filter(
        UsersTable.telegram_id == telegram_id).first()
    if user:
        user.first_name = first_name
        user.last_name = last_name
    else:
        new_user = UsersTable(telegram_id=telegram_id,
                              first_name=first_name, last_name=last_name)
        session.add(new_user)

    session.commit()


def get_user_data(telegram_id):
    Session = sessionmaker(bind=engine)
    session = Session()
    user = session.query(UsersTable).filter(
        UsersTable.telegram_id == telegram_id).first()
    return user