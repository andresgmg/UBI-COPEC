# Esquemas de la API

Los esquemas definen la estructura de los datos que la API acepta y retorna. Están implementados usando Pydantic para validación y serialización.

## Esquemas Base

### UbicacionBase

El esquema base define los campos comunes para todas las operaciones con ubicaciones.

```python
class UbicacionBase(BaseModel):
    name: str
    description: Optional[str] = None
    type: str
    latitude: float
    longitude: float
```

#### Validaciones
- `name`: String no vacío
- `description`: String opcional
- `type`: Debe ser uno de los valores definidos en `UbicacionType`
- `latitude`: Float entre -90 y 90
- `longitude`: Float entre -180 y 180

## Esquemas de Operación

### UbicacionCreate

Usado para crear nuevas ubicaciones.

```python
class UbicacionCreate(UbicacionBase):
    pass
```

### Ubicacion

Esquema completo que incluye el ID, usado para respuestas.

```python
class Ubicacion(UbicacionBase):
    id: UUID

    class Config:
        orm_mode = True
```

## Enumeraciones

### UbicacionType

Define los tipos válidos de ubicaciones.

```python
class UbicacionType(str, Enum):
    PRONTO = "pronto"
    BENCINERA = "bencinera"
    SERVICIO = "servicio"
    OTRO = "otro"
```

## Ejemplos

### Crear Ubicación

Request Body:
```json
{
  "name": "Pronto Las Condes",
  "description": "Estación con servicios 24/7",
  "type": "pronto",
  "latitude": -33.4122,
  "longitude": -70.5823
}
```

### Respuesta Ubicación

```json
{
  "id": "123e4567-e89b-12d3-a456-426614174000",
  "name": "Pronto Las Condes",
  "description": "Estación con servicios 24/7",
  "type": "pronto",
  "latitude": -33.4122,
  "longitude": -70.5823
}
```

## Validaciones y Errores

### Errores de Validación

1. **Tipo Inválido**
```json
{
  "detail": [
    {
      "loc": ["body", "type"],
      "msg": "value is not a valid enumeration member",
      "type": "type_error.enum"
    }
  ]
}
```

2. **Coordenadas Inválidas**
```json
{
  "detail": [
    {
      "loc": ["body", "latitude"],
      "msg": "ensure this value is less than or equal to 90",
      "type": "value_error.number.not_le"
    }
  ]
}
```

### Conversión de Tipos

Los esquemas manejan automáticamente la conversión entre:
- Strings UUID ↔ UUID objects
- Strings de fecha/hora ↔ datetime objects
- Strings de enumeración ↔ Enum members

## Uso con FastAPI

```python
@router.post("/", response_model=schemas.Ubicacion)
def create_ubicacion(
    ubicacion: schemas.UbicacionCreate,
    db: Session = Depends(get_db)
):
    db_ubicacion = models.Ubicacion(**ubicacion.dict())
    db.add(db_ubicacion)
    db.commit()
    db.refresh(db_ubicacion)
    return db_ubicacion
```
