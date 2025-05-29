from sqlalchemy import Column, String, Float, UUID

import uuid
from .database import Base


class Ubicacion(Base):
    __tablename__ = "ubicaciones"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, nullable=False)
    description = Column(String)
    type = Column(String, nullable=False)  # Enum en validación, no en DB
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
