from sqlalchemy import Column,Integer,String,Float
from database import Base
class fastapi_app(Base):
    __tablename__='Fishtestdata'
    id=Column(Integer,primary_key=True,index=True)
    Species=Column(String(20))
    Weight=Column(Float)
    Length1=Column(Float)
    Length2=Column(Float)
    Length3= Column(Float)
    Height=Column(Float)
    Width=Column(Float)