from sqlalchemy import Column, String, Integer, create_engine
from sqlalchemy.orm import declarative_base, scoped_session, sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.engine import URL

server = 'UNITNB015\CONNECTION'
database = 'connection'
user = 'sa'
password = '85356325Ll@'

connnection_string = f'DRIVER=ODBC Driver 17 for SQL Server;SERVER={server};DATABASE={database};UID={user};PWD={password}'
url = URL.create('mssql+pyodbc',query={'odbc_connect':connnection_string})


engine = create_engine(url=url, echo=True)

session = scoped_session(sessionmaker(
    engine,
    future = True,
    autocommit=False
))

base = declarative_base()
base.query = session.query_property()

class Telefones(base):
    __tablename__ = 'telefones'
    id = Column(Integer,primary_key=True)
    ddd = Column(Integer)
    fone = Column(Integer)
    dataentrada = Column(String)
    dataatualizacao = Column(String)
    valido = Column(String)
    numeroJob = Column(String)
    telefone_validando = Column(Integer)



    def __repr__(self):
        return f'{self.id}|{self.ddd}|{self.telefone}|{self.dataentrada}|{self.dataatualizacao}|{self.status}'
    

    def save(self):
        session.add(self)
        session.commit()
    


def create_datebase():
        base.metadata.drop_all(bind=engine)
        base.metadata.create_all(bind=engine)





if __name__ == '__main__':
    create_datebase()