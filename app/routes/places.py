from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app import models, schemas
from typing import List

router = APIRouter(prefix="/places", tags=["Places"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/", response_model=List[schemas.PlaceResponse])
def get_all_places(db: Session = Depends(get_db)):
    return db.query(models.Place).all()


@router.get("/prontos", response_model=List[schemas.PlaceResponse])
def get_prontos(db: Session = Depends(get_db)):
    return db.query(models.Place).filter(models.Place.type == "pronto").all()


@router.get("/bencineras", response_model=List[schemas.PlaceResponse])
def get_bencineras(db: Session = Depends(get_db)):
    return db.query(models.Place).filter(models.Place.type == "bencinera").all()


@router.get("/servicios", response_model=List[schemas.PlaceResponse])
def get_servicios(db: Session = Depends(get_db)):
    return db.query(models.Place).filter(models.Place.type == "servicio").all()


@router.get("/otros", response_model=List[schemas.PlaceResponse])
def get_otros(db: Session = Depends(get_db)):
    return db.query(models.Place).filter(models.Place.type == "otro").all()
