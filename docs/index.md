# UBI COPEC API

<div class="grid cards" markdown>

-   :book: __Guía de Uso__

    ---

    Aprende a instalar, configurar y usar la API.

    [:octicons-arrow-right-24: Empezar](guia/instalacion.md)

-   :material-api: __API__

    ---
    
    Explora los modelos, rutas y esquemas de la API.

    [:octicons-arrow-right-24: Documentación API](api/modelos.md)

-   :material-code-braces: __Desarrollo__

    ---

    Contribuye al proyecto y conoce nuestros estándares.

    [:octicons-arrow-right-24: Guía del desarrollador](desarrollo/contribuir.md)

-   :material-information: __Acerca de__

    ---

    Licencia y registro de cambios.

    [:octicons-arrow-right-24: Más información](about/licencia.md)

</div>

## 🎯 Objetivo General

UBI COPEC API es una interfaz de programación de aplicaciones (API) RESTful que proporciona acceso público a información georreferenciada de las ubicaciones de COPEC en Chile. Este proyecto nace con el objetivo de facilitar el acceso a datos estructurados sobre estaciones de servicio, tiendas Pronto, servicios automotrices y otros puntos de interés relacionados con COPEC.

## 🎁 ¿Qué ofrece?

- **Datos Georreferenciados**: Acceso a coordenadas precisas de ubicaciones COPEC
- **API REST Moderna**: Desarrollada con FastAPI, garantizando alto rendimiento
- **Documentación Completa**: Guías detalladas y ejemplos de uso
- **Código Abierto**: 100% open source bajo licencia Apache 2.0

## 👥 ¿A quién va dirigido?

Esta API está diseñada para:

- **Desarrolladores** que necesiten integrar datos de ubicaciones COPEC en sus aplicaciones
- **Investigadores** que requieran datos geográficos del sector energético
- **Empresas** que deseen analizar la distribución de servicios COPEC
- **Estudiantes** interesados en aprender sobre APIs RESTful y geolocalización

## 🚀 Primeros Pasos

```bash
# Clonar el repositorio
git clone https://github.com/tu-usuario/UBI-COPEC.git

# Instalar dependencias
pip install -r requirements.txt

# Iniciar el servidor de desarrollo
uvicorn app.main:app --reload
```

## 📊 Ejemplo de Uso

```python
import requests

# Obtener todas las estaciones Pronto
response = requests.get("http://localhost:8000/places/prontos")
prontos = response.json()

# Imprimir nombres y ubicaciones
for pronto in prontos:
    print(f"{pronto['name']}: {pronto['latitude']}, {pronto['longitude']}")
```

## 🤝 Contribuir al Proyecto

¡Tus contribuciones son bienvenidas! Puedes ayudar:

- Reportando bugs
- Sugiriendo nuevas funcionalidades
- Mejorando la documentación
- Escribiendo código

Consulta nuestra [guía de contribución](desarrollo/contribuir.md) para más detalles.

## 📜 Licencia

Este proyecto está bajo la licencia Apache 2.0. Consulta el archivo [LICENSE](about/licencia.md) para más detalles.