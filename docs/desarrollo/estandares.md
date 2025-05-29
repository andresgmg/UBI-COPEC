# Estándares de Desarrollo

## 📝 Estilo de Código

### Python

Seguimos [PEP 8](https://www.python.org/dev/peps/pep-0008/) con algunas modificaciones:

```python
# Correcto
def get_ubicacion_by_id(ubicacion_id: UUID) -> Optional[Ubicacion]:
    return db.query(Ubicacion).filter(Ubicacion.id == ubicacion_id).first()

# Incorrecto
def getUbicacionById(ubicacionId):
    return db.query(Ubicacion).filter(Ubicacion.id==ubicacionId).first()
```

### Convenciones de Nombrado

- **Variables y funciones**: snake_case
- **Clases**: PascalCase
- **Constantes**: MAYÚSCULAS_CON_GUIONES
- **Módulos**: minúsculas_con_guiones
- **Tipos**: PascalCase

## 🏗️ Arquitectura

### Estructura de Carpetas

```
app/
├── main.py           # Punto de entrada
├── database.py       # Configuración DB
├── models.py         # Modelos SQLAlchemy
├── schemas.py        # Schemas Pydantic
├── enums.py         # Enumeraciones
└── routes/          # Endpoints API
    └── places.py    # Rutas de ubicaciones
```

### Patrones de Diseño

1. **Dependency Injection**
```python
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
```

2. **Repository Pattern**
```python
class UbicacionRepository:
    def __init__(self, db: Session):
        self.db = db
    
    def get_all(self) -> List[Ubicacion]:
        return self.db.query(Ubicacion).all()
```

## 🧪 Testing

### Estructura de Tests

```
tests/
├── conftest.py      # Fixtures compartidos
├── test_api.py      # Tests de API
└── test_models.py   # Tests de modelos
```

### Ejemplo de Test

```python
def test_get_ubicaciones(client, db):
    response = client.get("/ubicaciones/")
    assert response.status_code == 200
    assert len(response.json()) > 0
```

## 📚 Documentación

### Docstrings

Usamos el formato Google para docstrings:

```python
def get_ubicacion_by_type(type: str) -> List[Ubicacion]:
    """Obtiene ubicaciones filtradas por tipo.

    Args:
        type (str): Tipo de ubicación (PRONTO, BENCINERA, etc)

    Returns:
        List[Ubicacion]: Lista de ubicaciones del tipo especificado

    Raises:
        ValueError: Si el tipo no es válido
    """
```

### Comentarios

- Usar comentarios para explicar "por qué", no "qué"
- Mantener comentarios actualizados
- Escribir en español por consistencia

## 🔒 Seguridad

### Validación de Datos

```python
from pydantic import BaseModel, validator

class UbicacionCreate(BaseModel):
    name: str
    latitude: float
    longitude: float

    @validator('latitude')
    def validate_latitude(cls, v):
        if not -90 <= v <= 90:
            raise ValueError('Latitud inválida')
        return v
```

### Manejo de Errores

```python
from fastapi import HTTPException

def get_ubicacion(id: UUID):
    ubicacion = db.get(id)
    if not ubicacion:
        raise HTTPException(
            status_code=404,
            detail="Ubicación no encontrada"
        )
    return ubicacion
```

## 🚀 Performance

- Usar índices en la base de datos
- Implementar caché cuando sea necesario
- Paginar resultados grandes
- Optimizar consultas N+1
