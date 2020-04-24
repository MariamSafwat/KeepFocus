from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Date,Table
from sqlalchemy.orm import relationship
from sqlalchemy.orm import sessionmaker




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


class Statistics(Base):
    __tablename__ = "statistics"
    id = Column(Integer, primary_key=True)
    dateAndTime = Column(DateTime, nullable=False)#data and time for screenshot
    timer = Column(BOOLEAN)#Check if the time that screenshot has been taken at the same time that the user wants to notify.
    programe=Column(String, nullable=False)#output from image processing
    productive = Column(String, nullable=False)#check if image is productive or not


class Day(Base):
    __tablename__ = "Day"
    id = Column(Integer, primary_key=True)
    date = Column(Date, nullable=False)
    statistics = relationship("Statistics",
                    secondary=association_table)
    allCatagory = Column(String, nullable=False)
    totalTime = Column(Integer)
    timerOnTime = Column(Integer)


class Programsdata(Base):
    __tablename__ = "programsdata"
    id = Column(Integer, primary_key=True)#id for each program
    name = Column(String, nullable=False)#name of the programe 
    listoftext = Column(String, nullable=False)# list of texts that related to each program
    listofimage = Column(Integer, nullable=False)# list of images that related to each program
    productive = Column(Integer, nullable=False)#input from user 
    

Base.metadata.create_all(engine)
