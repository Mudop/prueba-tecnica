from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
import schemas, crud
from database import SessionLocal

router = APIRouter(prefix="/candidatos", tags=["Candidatos"])


def get_db():
    db = SessionLocal()
    try: 
        yield db
    finally:
        db.close()

@router.get("/", response_model=list[schemas.Candidato])
def listar_candidatos(db: Session=Depends(get_db)):
    return crud.get_candidatos(db)



@router.post("/", response_model=schemas.Candidato)
def crear_candidato(candidato: schemas.CandidatoCreate, db: Session = Depends(get_db)):
    return crud.create_candidato(db,candidato)
