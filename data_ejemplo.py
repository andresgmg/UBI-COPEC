from app.database import SessionLocal, engine, Base
from app.models import Ubicacion
from app.enums import UbicacionType
import uuid

# Crear las tablas (si no existen)
Base.metadata.create_all(bind=engine)

# Instanciar sesión
db = SessionLocal()

# Datos de prueba (2 por cada tipo)
ubicaciones = [
    # Prontos
    Ubicacion(
        id=uuid.uuid4(),
        name="EJEMPLO - Pronto Maipú",
        description="EJEMPLO - Estación Pronto con cafetería y baño",
        type=UbicacionType.PRONTO.value,
        latitude=-33.5123,
        longitude=-70.7611,
    ),
    Ubicacion(
        id=uuid.uuid4(),
        name="EJEMPLO - Pronto La Reina",
        description="EJEMPLO - Estación Pronto con minimarket",
        type=UbicacionType.PRONTO.value,
        latitude=-33.4543,
        longitude=-70.5423,
    ),
    # Bencineras
    Ubicacion(
        id=uuid.uuid4(),
        name="EJEMPLO - Copec Vitacura",
        description="EJEMPLO - Bencinera tradicional en sector oriente",
        type=UbicacionType.BENCINERA.value,
        latitude=-33.3902,
        longitude=-70.5678,
    ),
    Ubicacion(
        id=uuid.uuid4(),
        name="EJEMPLO - Copec Quilicura",
        description="EJEMPLO - Estación de servicio en el sector norte",
        type=UbicacionType.BENCINERA.value,
        latitude=-33.3675,
        longitude=-70.7301,
    ),
    # Servicios
    Ubicacion(
        id=uuid.uuid4(),
        name="EJEMPLO - Lubricentro Copec",
        description="EJEMPLO - Cambio de aceite y revisión básica",
        type=UbicacionType.SERVICIO.value,
        latitude=-33.4656,
        longitude=-70.6457,
    ),
    Ubicacion(
        id=uuid.uuid4(),
        name="EJEMPLO - Lavado Copec Ñuñoa",
        description="EJEMPLO - Lavado automático de vehículos",
        type=UbicacionType.SERVICIO.value,
        latitude=-33.4567,
        longitude=-70.6102,
    ),
    # Otros
    Ubicacion(
        id=uuid.uuid4(),
        name="EJEMPLO - Electrolinera Copec",
        description="EJEMPLO - Punto de carga para autos eléctricos",
        type=UbicacionType.OTRO.value,
        latitude=-33.4182,
        longitude=-70.5982,
    ),
    Ubicacion(
        id=uuid.uuid4(),
        name="EJEMPLO - Centro de distribución Copec",
        description="EJEMPLO - Base de operaciones logística",
        type=UbicacionType.OTRO.value,
        latitude=-33.5034,
        longitude=-70.6754,
    ),
]

# Insertar datos en DB
db.add_all(ubicaciones)
db.commit()
db.close()

print("✅ Datos de prueba insertados correctamente.")
