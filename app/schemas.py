from pydantic import BaseModel
from uuid import UUID
from .enums import PlaceType


class PlaceBase(BaseModel):
    name: str
    description: str
    type: PlaceType
    latitude: float
    longitude: float


class PlaceCreate(PlaceBase):
    pass


class PlaceResponse(PlaceBase):
    id: UUID

    class Config:
        orm_mode = True
