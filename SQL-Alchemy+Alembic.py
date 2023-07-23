from sqlalchemy import create_engine, select, MetaData, Table, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import inspect
dbPath = "datafile.db"
engine = create_engine("sqlite:///%s" % dbPath)
metadata = MetaData(engine)
people = Table("people", metadata, Column("id", Integer, primary_key = True), Column("name", String), Column("count", Integer))

Base = declarative_base()
class People(Base):
    __tablename__ = "people"
    id = Column(Integer, primary_key = True)
    name = Column(String)
    count = Column("count", Integer)

Session = sessionmaker(bind = engine)
session = Session()
metadata.create_all(engine)

inspector = inspect(engine)
print(inspector.get_table_names())
