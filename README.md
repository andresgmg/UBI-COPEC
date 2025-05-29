# 🛢️ API UBICACIONES COPEC
**UBICACIONES COPEC** es una API RESTful open source desarrollada con **FastAPI** y respaldada por una base de datos **SQLite**. Proporciona acceso público a información georreferenciada de lugares asociados a **COPEC** en Chile, como estaciones Pronto, bencineras, servicios y más.

---

## 🚀 Características
- ✅ API REST con endpoints GET categorizados por tipo de lugar
- 🗺️ Datos con coordenadas geográficas (latitud y longitud)
- 🧩 Estructura modular con SQLAlchemy + Pydantic
- 💾 Base de datos embebida SQLite
- 📚 Documentación técnica con mkdocs-material
- 🧪 Script de carga inicial de datos (seed_data.py)
- 🔓 100% open source

---

## 📦 Estructura del proyecto

```yaml
UBI-COPEC/
├── app/
│   ├── main.py              # Punto de entrada FastAPI
│   ├── database.py          # Config DB SQLite
│   ├── models.py            # Modelos SQLAlchemy
│   ├── schemas.py           # Schemas Pydantic
│   ├── enums.py             # Enum para tipos
│   └── routes/
│       └── places.py        # Endpoints /places/*
├── data/
│   └── copec.db             # Base de datos SQLite
├── docs/                    # Documentación MkDocs
├── seed_data.py             # Script para poblar la DB
├── mkdocs.yml               # Configuración de MkDocs
├── requirements.txt         # Dependencias del proyecto
└── README.md                # Este archivo
```

---

## 🛠️ Instalación y ejecución local

### 1. Clona el repositorio

```bash
git clone https://github.com/tu-usuario/copec-api.git
cd UBI-COPEC
```

### 2. Crea y activa un entorno virtual

```bash
python -m venv env
source env/bin/activate  # Linux/macOS
env\Scripts\activate     # Windows
```

### 3. Instala dependencias

```bash
pip install -r requirements.txt
```

### 4. Corre el servidor de desarrollo

```bash
uvicorn app.main:app --reload
```

### 5. Inserta datos de ejemplo (Opcional)

```bash
python seed_data.py
```

---

## 🔗 Endpoints disponibles

| Endpoint                  | Descripción                                   |
|--------------------------|-----------------------------------------------|
| `/ubicaciones/`               | Lista de todos los lugares COPEC              |
| `/ubicaciones/prontos`        | Lista de estaciones **Pronto**                |
| `/ubicaciones/bencineras`     | Lista de **bencineras**                       |
| `/ubicaciones/servicios`      | Lista de **servicios asociados**              |
| `/ubicaciones/otros`          | Lista de otros tipos de lugares               |

---

## 🧱 Estructura del objeto lugar

Todos los lugares retornan el mismo esquema:

```json
{
  "id": "uuid",
  "name": "Nombre del lugar",
  "description": "Descripción del lugar",
  "type": "pronto | bencinera | servicio | otro",
  "latitude": -33.1234,
  "longitude": -70.5678
}
```

---

## 📚 Documentación técnica

Este proyecto usa [MkDocs Material](https://squidfunk.github.io/mkdocs-material/) para su documentación técnica.

### Cómo levantar la documentación localmente:

```bash
pip install mkdocs mkdocs-material
mkdocs serve
```

Luego visita: [http://localhost:8000](http://localhost:8000)

---

## 📌 Roadmap futuro

- [ ] Añadir filtros por región o comuna  
- [ ] Agregar soporte para búsqueda por coordenadas  
- [ ] Crear un panel de administración web para CRUD  
- [ ] Publicar la API en Vercel o Fly.io  
- [ ] Añadir autenticación (opcional, para endpoints privados)  
- [ ] Cargar dataset completo desde fuentes oficiales COPEC  

---

## 🤝 Contribuciones

¡Las contribuciones son bienvenidas! Si quieres agregar nuevos features, corregir errores o mejorar la documentación, abre un **issue** o un **pull request**.

---

## ⚖️ Licencia

Este proyecto está licenciado bajo la [MIT License](LICENSE).