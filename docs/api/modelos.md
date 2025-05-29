# Modelos de la API

## Modelo Base de Datos

### Ubicacion

El modelo principal de la aplicación es `Ubicacion`, que representa una ubicación física de COPEC.

```python
class Ubicacion(Base):
    __tablename__ = "ubicacion"

    id = Column(UUID, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(Text, nullable=True)
    type = Column(String, nullable=False)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
```

#### Campos
- `id`: Identificador único UUID
- `name`: Nombre de la ubicación
- `description`: Descripción detallada (opcional)
- `type`: Tipo de ubicación (PRONTO, BENCINERA, SERVICIO, OTRO)
- `latitude`: Latitud geográfica
- `longitude`: Longitud geográfica

## Schemas Pydantic

### UbicacionBase

Schema base que define los campos comunes:

```python
class UbicacionBase(BaseModel):
    name: str
    description: Optional[str] = None
    type: str
    latitude: float
    longitude: float
```

### UbicacionCreate

Schema usado para crear nuevas ubicaciones:

```python
class UbicacionCreate(UbicacionBase):
    pass
```

### Ubicacion

Schema completo que incluye el ID:

```python
class Ubicacion(UbicacionBase):
    id: UUID

    class Config:
        orm_mode = True
```

## Enumeraciones

### UbicacionType

Define los tipos válidos de ubicaciones:

```python
class UbicacionType(str, Enum):
    PRONTO = "pronto"
    BENCINERA = "bencinera"
    SERVICIO = "servicio"
    OTRO = "otro"
```

## Validaciones

Los modelos incluyen las siguientes validaciones:

1. **Coordenadas Geográficas**
   - Latitud: entre -90 y 90
   - Longitud: entre -180 y 180

2. **Tipos de Ubicación**
   - Solo se permiten los valores definidos en `UbicacionType`

3. **Campos Requeridos**
   - `name`
   - `type`
   - `latitude`
   - `longitude`

## Ejemplos de Uso

### Crear una Nueva Ubicación

```python
nueva_ubicacion = Ubicacion(
    id=uuid.uuid4(),
    name="Pronto Las Condes",
    description="Estación con servicios 24/7",
    type=UbicacionType.PRONTO,
    latitude=-33.4122,
    longitude=-70.5823
)
```

### Consultar Ubicaciones por Tipo

```python
ubicaciones_pronto = db.query(Ubicacion).filter(
    Ubicacion.type == UbicacionType.PRONTO
).all()
```
