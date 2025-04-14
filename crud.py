from sqlalchemy.orm import Session
import models, schemas

def create_candidato(db: Session, candidato: schemas.CandidatoCreate):
    db_candidato = models.Candidato(**candidato.dict())
    db.add(db_candidato)
    db.commit()
    db.refresh(db_candidato)
    return db_candidato

def get_candidatos(db: Session):
    return db.query(models.Candidato).all()

def get_candidato_by_id(db: Session, candidato_id: int):
    return db.query(models.Candidato).filter(models.Candidato.id == candidato_id).first()

def update_candidato(db: Session, candidato_id: int, candidato_data: schemas.CandidatoCreate):
    candidato = get_candidato_by_id(db, candidato_id)
    if candidato:
        for key, value in candidato_data.dict().items():
            setattr(candidato, key, value)
        db.commit()
        db.refresh(candidato)
    return candidato

def delete_candidato(db: Session, candidato_id: int):
    candidato = get_candidato_by_id(db, candidato_id)
    if candidato:
        db.delete(candidato)
        db.commit()
    return candidato


def create_oferta(db: Session, oferta: schemas.OfertaCreate):
    db_oferta = models.Oferta(**oferta.dict())
    db.add(db_oferta)
    db.commit()
    db.refresh(db_oferta)
    return db_oferta

def get_ofertas(db: Session):
    return db.query(models.Oferta).all()

def get_oferta_by_id(db: Session, oferta_id: int):
    return db.query(models.Oferta).filter(models.Oferta.id == oferta_id).first()

def update_oferta(db: Session, oferta_id: int, oferta_data: schemas.OfertaCreate):
    oferta = get_oferta_by_id(db, oferta_id)
    if oferta:
        for key, value in oferta_data.dict().items():
            setattr(oferta, key, value)
        db.commit()
        db.refresh(oferta)
    return oferta

def delete_oferta(db: Session, oferta_id: int):
    oferta = get_oferta_by_id(db, oferta_id)
    if oferta:
        db.delete(oferta)
        db.commit()
    return oferta


def create_orden(db: Session, orden: schemas.OrdenCreate):
    db_orden = models.Orden(**orden.dict())
    db.add(db_orden)
    db.commit()
    db.refresh(db_orden)
    return db_orden

def get_ordenes(db: Session):
    return db.query(models.Orden).all()

def get_orden_by_id(db: Session, orden_id: int):
    return db.query(models.Orden).filter(models.Orden.id == orden_id).first()

def update_orden(db: Session, orden_id: int, orden_data: schemas.OrdenCreate):
    orden = get_orden_by_id(db, orden_id)
    if orden:
        for key, value in orden_data.dict().items():
            setattr(orden, key, value)
        db.commit()
        db.refresh(orden)
    return orden

def delete_orden(db: Session, orden_id: int):
    orden = get_orden_by_id(db, orden_id)
    if orden:
        db.delete(orden)
        db.commit()
    return orden
