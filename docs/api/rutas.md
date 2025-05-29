# Rutas de la API

## Estructura Base

Todas las rutas están montadas bajo el prefijo `/ubicaciones/`.

## Endpoints Detallados

### GET /ubicaciones/

Retorna todas las ubicaciones disponibles en la base de datos.

```python
@router.get("/", response_model=List[schemas.Ubicacion])
def get_ubicaciones(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
):
    """
    Obtiene todas las ubicaciones con paginación opcional.
    """
```

#### Parámetros Query
- `skip` (opcional): Número de registros a saltar
- `limit` (opcional): Número máximo de registros a retornar

#### Respuesta
```json
[
  {
    "id": "123e4567-e89b-12d3-a456-426614174000",
    "name": "Pronto Las Condes",
    "description": "Estación con servicios 24/7",
    "type": "pronto",
    "latitude": -33.4122,
    "longitude": -70.5823
  }
]
```

### GET /ubicaciones/prontos/

Retorna todas las ubicaciones de tipo Pronto.

```python
@router.get("/prontos/", response_model=List[schemas.Ubicacion])
def get_prontos(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
):
    """
    Obtiene todas las ubicaciones tipo Pronto.
    """
```

### GET /ubicaciones/bencineras/

Retorna todas las ubicaciones de tipo Bencinera.

```python
@router.get("/bencineras/", response_model=List[schemas.Ubicacion])
def get_bencineras(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
):
    """
    Obtiene todas las ubicaciones tipo Bencinera.
    """
```

### GET /ubicaciones/servicios/

Retorna todas las ubicaciones de tipo Servicio.

```python
@router.get("/servicios/", response_model=List[schemas.Ubicacion])
def get_servicios(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
):
    """
    Obtiene todas las ubicaciones tipo Servicio.
    """
```

### GET /ubicaciones/otros/

Retorna todas las ubicaciones de tipo Otro.

```python
@router.get("/otros/", response_model=List[schemas.Ubicacion])
def get_otros(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
):
    """
    Obtiene todas las ubicaciones tipo Otro.
    """
```

## Manejo de Errores

### No Encontrado (404)

Cuando no se encuentran ubicaciones del tipo solicitado:

```json
{
  "detail": "No se encontraron ubicaciones de tipo {tipo}"
}
```

### Error de Validación (422)

Cuando los parámetros de query no son válidos:

```json
{
  "detail": [
    {
      "loc": ["query", "limit"],
      "msg": "ensure this value is greater than 0",
      "type": "value_error.number.not_gt"
    }
  ]
}
```

## Ejemplos de Uso

### Curl

```bash
# Obtener todas las ubicaciones
curl http://localhost:8000/ubicaciones/

# Obtener Prontos con paginación
curl http://localhost:8000/ubicaciones/prontos/?skip=0&limit=10

# Obtener Bencineras
curl http://localhost:8000/ubicaciones/bencineras/
```

### Python Requests

```python
import requests

# Obtener todas las ubicaciones
response = requests.get("http://localhost:8000/ubicaciones/")
ubicaciones = response.json()

# Obtener Prontos con paginación
response = requests.get(
    "http://localhost:8000/ubicaciones/prontos/",
    params={"skip": 0, "limit": 10}
)
prontos = response.json()
```
