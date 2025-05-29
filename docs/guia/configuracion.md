# Configuración

## Variables de Entorno

La API utiliza las siguientes variables de entorno que puedes configurar:

- `DATABASE_URL`: URL de conexión a la base de datos SQLite (por defecto: `sqlite:///data/copec.db`)
- `DEBUG`: Modo debug para desarrollo (por defecto: `False`)
- `API_PREFIX`: Prefijo para todas las rutas de la API (por defecto: `/`)
- `PORT`: Puerto donde se ejecutará la aplicación (por defecto: `8000`)

## Base de Datos

### Estructura

La base de datos SQLite está organizada con las siguientes tablas:

```sql
CREATE TABLE ubicacion (
    id UUID PRIMARY KEY,
    name VARCHAR NOT NULL,
    description TEXT,
    type VARCHAR NOT NULL,
    latitude FLOAT NOT NULL,
    longitude FLOAT NOT NULL
);
```

### Datos de Ejemplo

Puedes cargar datos de ejemplo usando el script proporcionado:

```bash
python data_ejemplo.py
```

Este script creará:
- 2 ubicaciones tipo Pronto
- 2 ubicaciones tipo Bencinera
- 2 ubicaciones tipo Servicio
- 2 ubicaciones tipo Otro

## Configuración de CORS

Por defecto, la API permite solicitudes desde cualquier origen. Puedes modificar esto en `app/main.py`:

```python
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Modificar según necesidades
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

## Logging

La API utiliza el sistema de logging estándar de Python. La configuración se puede ajustar en `app/main.py`:

```python
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
```
