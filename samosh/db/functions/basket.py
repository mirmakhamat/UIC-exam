from sqlalchemy.orm import sessionmaker
from db.engine import engine
from db.table import BasketTable
from db.functions import user as user_functions


def get_user_basket(telegram_id):
    Session = sessionmaker(bind=engine)
    session = Session()
    user = user_functions.get_user_data(telegram_id)

    products = session.query(BasketTable).filter(
        BasketTable.user_id == user.id).all()

    return products


def add_product_to_basket(telegram_id, product_id, count):
    Session = sessionmaker(bind=engine)
    session = Session()
    user = user_functions.get_user_data(telegram_id)
    product = session.query(BasketTable).filter(
        BasketTable.product_id == product_id,
        BasketTable.user_id == user.id).first()
    if product:
        product.count = count
    else:
        new_product = BasketTable(
            user_id=user.id, product_id=product_id, count=count)

        session.add(new_product)
    session.commit()


def change_product_count(product_id, count) -> bool:
    Session = sessionmaker(bind=engine)
    session = Session()
    product = session.query(BasketTable).filter(
        BasketTable.id == product_id).first()

    if product.count > 1 or (product.count == 1 and count != -1):
        product.count += count
        session.commit()
        return True

    return False


def del_product(product_id):
    Session = sessionmaker(bind=engine)
    session = Session()
    product = session.query(BasketTable).filter(
        BasketTable.id == product_id).first()

    session.delete(product)
    session.commit()
