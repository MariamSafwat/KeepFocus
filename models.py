from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Date,Table
from sqlalchemy.orm import relationship
from sqlalchemy.orm import sessionmaker




engine = create_engine('sqlite:///database.db')
Session = sessionmaker(bind=engine)
session = Session()


Base = declarative_base()

association_table = Table('association', Base.metadata,
    Column('left_id', Integer, ForeignKey('Day.id')),
    Column('right_id', Integer, ForeignKey('statistics.id'))
)


class Statistics(Base):
    __tablename__ = "statistics"
    id = Column(Integer, primary_key=True)
    DateAndTime = Column(DateTime, nullable=False)#data and time for screenshot
    Timebool = Column(Integer)#Check if the time that screenshot has been taken at the same time that the user wants to notify.
    Dictionary=Column(String, nullable=False)#output from image processing
    productive = Column(String, nullable=False)#check if image is productive or not
    



class Day(Base):
    __tablename__ = "Day"
    id = Column(Integer, primary_key=True)
    Date = Column(Date, nullable=False)
    Statistics = relationship("Statistics",
                    secondary=association_table)
    ALlCatagory = Column(String, nullable=False)
    TotalTime = Column(Integer)
    TimerOnTime = Column(Integer)




class Programsdata(Base):
    __tablename__ = "programsdata"
    id = Column(Integer, primary_key=True)#id for each program
    listoftext = Column(String, nullable=False)# list of texts that related to each program
    listofimage = Column(Integer, nullable=False)# list of images that related to each program
    productive = Column(Integer, nullable=False)#input from user 
