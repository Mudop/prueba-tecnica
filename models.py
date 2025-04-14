from sqlalchemy import Column, Integer, String, Date
from database import Base

class Candidato(Base):
    __tablename__="candidatos"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String)
    apellido = Column(String)
    tipo_documento = Column(String)
    cedula = Column(String, unique=True, index=True)
    fecha_nacimiento = Column(Date, nullable=True)
    rh = Column(String)
    ciudad_expedicion= Column(String)
    ciudad_nacimiento= Column(String)
    ciudad_domicilio= Column(String)
    
