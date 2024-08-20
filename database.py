from sqlalchemy import create_engine, Column, Integer, String, Float, Date, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from config import DATABASE_URL


engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()


class SimCardActivation(Base):
    __tablename__= 'sim_card_activations'
    
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    tariff_plan = Column(String)
    activation_date = Column(Date)
    revenue = Column(Float)
    
Base.metadata.create_all(engine)