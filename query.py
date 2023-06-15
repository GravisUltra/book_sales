import sqlalchemy
from sqlalchemy.orm import sessionmaker

from models import create_tables, Publisher, Shop, Book, Stock, Sale
from dsn import DSN

engine = sqlalchemy.create_engine(DSN)
create_tables(engine)

Session = sessionmaker(bind=engine)
session = Session()

# Выводит название магазинов (shop), в которых представлены книги конкретного издателя,
# получая имя или идентификатор издателя (publisher), через input().
q = session.query(Shop)
print(q)