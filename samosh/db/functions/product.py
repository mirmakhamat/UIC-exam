from sqlalchemy.orm import sessionmaker
from db.engine import engine
from db.table import ProductsTable

def get_products_by_category(category_id):
    Session = sessionmaker(bind=engine)
    session = Session()
    products = session.query(ProductsTable).filter(
        ProductsTable.category_id == category_id).all()
    return products


def get_product_by_id(id):
    Session = sessionmaker(bind=engine)
    session = Session()
    category = session.query(ProductsTable).filter(
        ProductsTable.id == id).first()
    return category

def get_product_by_name(name):
    Session = sessionmaker(bind=engine)
    session = Session()
    category = session.query(ProductsTable).filter(
        ProductsTable.name == name).first()
    return category