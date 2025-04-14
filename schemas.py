from pydantic import BaseModel
from datetime import date

class CandidatoBase(BaseModel):
    nombre: str
    apellido: str
    tipo_documento: str
    cedula: str
    fecha_nacimiento: date | None = None
    rh: str
    ciudad_expedicion: str
    ciudad_nacimiento: str
    ciudad_domicilio: str

class CandidatoCreate(CandidatoBase):
    pass

class Candidato(CandidatoBase):
    id: int

    class Config:
        from_attributes = True


class OfertaBase(BaseModel):
    cliente: str
    cargo: str
    descripcion: str
    ciudad: str
    

class OfertaCreate(OfertaBase):
    pass

class Oferta(OfertaBase):
    id: int

    class Config:
        from_attributes = True



class OrdenBase(BaseModel):
    cliente: str
    cargo: str
    examenes: str


class OrdenCreate(OrdenBase):
    pass

class Orden(OrdenBase):
    id: int

    class Config:
        from_attributes = True