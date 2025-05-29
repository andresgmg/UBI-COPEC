from fastapi import FastAPI
from app.routes import places
from app.database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="API UBICACIONES COPEC",
    description="API REST pública de lugares asociados a COPEC en Chile",
    version="1.0.0",
)

app.include_router(places.router)
