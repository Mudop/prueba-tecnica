from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
import schemas, crud
from database import SessionLocal

router = APIRouter(prefix="/ofertas", tags=["Ofertas"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=list[schemas.Oferta])
def listar_ofertas(db: Session = Depends(get_db)):
    return crud.get_ofertas(db)

@router.post("/", response_model=schemas.Oferta)
def crear_oferta(oferta: schemas.OfertaCreate, db: Session = Depends(get_db)):
    return crud.create_oferta(db, oferta)
