from sqlalchemy.orm import sessionmaker
from db.engine import engine
from db.table import CategoriesTable


def get_all_categories():
    Session = sessionmaker(bind=engine)
    session = Session()
    categories = session.query(CategoriesTable).all()
    return categories

def get_category_by_name(name):
    Session = sessionmaker(bind=engine)
    session = Session()
    category = session.query(CategoriesTable).filter(
        CategoriesTable.name == name).first()
    return category