import json
from database import SessionLocal
from models import Candidato
from datetime import datetime


def import_json():
    db=SessionLocal()
    with open("data/JSON.txt", "r", encoding="utf-8") as f:
       data = json.load(f)


    for item in data:
        nuevo =Candidato(
            nombre=item.get("nombre" , ""),
            apellido=item.get("apellido", ),
            tipo_documento=item.get("clasE_DOCTO" , ""),
            cedula=item.get("doctO_IDENT", ),
            fecha_nacimiento=None,
            rh=item.get("grupO_RH" , ""),
            ciudad_expedicion=item.get("ciudad_n", ),
            ciudad_nacimiento=item.get("ciudad_e", ),
           ciudad_domicilio=item.get("ciudad_d", ),
            
        )
        db.add(nuevo)

    db.commit()
    db.close()
    print("se importo los datos")

if __name__ == "__main__":
  import_json()