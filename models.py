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
    Timebool = Column(Integer)
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
    id = Column(Integer, primary_key=True)
    listoftext = Column(String, nullable=False)
    listofimage = Column(Integer, nullable=False)

