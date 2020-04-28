from sqlalchemy import create_engine,event
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Date,Table, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.orm import sessionmaker
from sqlite3 import Connection as SQLite3Connection
from sqlalchemy.engine import Engine




engine = create_engine('sqlite:///database.db',echo=True)
# the ORM must have asession to make middle-ground between the objects in Python and the engine that actually communicates with the database. 
Session = sessionmaker(bind=engine)
session = Session()

#map which table in the db will be related to each class in our files
Base = declarative_base()

# one to many relation table between day and statistics
association_table = Table('association', Base.metadata,
    Column('left_id', Integer, ForeignKey('Day.id')),
    Column('right_id', Integer, ForeignKey('statistics.id'))
)

@event.listens_for(Engine, "connect")
def _set_sqlite_pragma(dbapi_connection, connection_record):
    if isinstance(dbapi_connection, SQLite3Connection):
        cursor = dbapi_connection.cursor()
        cursor.execute("PRAGMA foreign_keys=ON;")
        cursor.close()

class Statistics(Base):
    __tablename__ = "statistics"
    id = Column(Integer, primary_key=True)
    dateAndTime = Column(DateTime, nullable=False)#data and time for screenshot
    timer = Column(Boolean)#Check if the time that screenshot has been taken at the same time that the user wants to notify.
    programe=Column(String, nullable=False)#output from image processing
    productive = Column(String, nullable=False)#check if image is productive or not


class Day(Base):
    __tablename__ = "Day"
    id = Column(Integer, primary_key=True)
    date = Column(Date, nullable=False)
    statistics = relationship("Statistics",
                    secondary=association_table)
    allPrograms = Column(String, nullable=False)
    totalTime = Column(Integer)
    timerOnTime = Column(Integer)


class Programsdata(Base):
    NEUTRAL =0
    PRODUCTIVE = 1
    DISTRACTIVE = 2

    STATUS = ((NEUTRAL,"NEUTRAL"),(PRODUCTIVE,"PRODUCTIVE"),(DISTRACTIVE,"DISTRACTIVE"))

    __tablename__ = "Programsdata"
    id = Column(Integer, primary_key=True)#id for each program
    name = Column(String, nullable=False)#name of the programe 
    listoftext = Column(String, nullable=False)# list of texts that related to each program
    listofimage = Column(String, nullable=False)# list of images that related to each program
    productive = Column(Integer, nullable=False)#input from user 
    prog_category = Column(Integer,ForeignKey('Category.id'))

class Category(Base):
    __tablename__ = "Category"
    id = Column(Integer, primary_key=True)
    name=Column(String, nullable=False)
    programs = relationship("Programsdata", backref='Category')


Base.metadata.create_all(engine)

