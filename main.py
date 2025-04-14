from fastapi import FastAPI
from database import Base, engine
from routers import candidatos,ofertas,ordenes
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(candidatos.router)
app.include_router(ofertas.router)
app.include_router(ordenes.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:5500"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)