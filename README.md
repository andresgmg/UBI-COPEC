# UBI-COPEC
Proyecto de REST API, Open Source de Ubicaciones COPEC

## Estructura inicial del proyecto

UBI-COPEC/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── models.py          # SQLAlchemy models
│   ├── schemas.py         # Pydantic schemas
│   ├── database.py        # Conexión a SQLite
│   ├── enums.py           # Enumeraciones (type)
│   └── routes/
│       ├── __init__.py
│       ├── places.py      # Endpoints de lugares
├── data/
│   └── copec.db           # Base de datos SQLite
├── mkdocs.yml             # Configuración MkDocs
├── docs/
│   └── index.md           # Documentación inicial
├── requirements.txt       # Requisitos Python
└── README.md              # Descripción del proyecto
