from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
import schemas, crud
from database import SessionLocal

router = APIRouter(prefix="/ordenes", tags=["Ordenes"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=list[schemas.Orden])
def listar_ordenes(db: Session = Depends(get_db)):
    return crud.get_ordenes(db)

@router.post("/", response_model=schemas.Orden)
def crear_orden(orden: schemas.OrdenCreate, db: Session = Depends(get_db)):
    return crud.create_orden(db, orden)