# Endpoints de la API

## Estructura Base

Todos los endpoints retornan ubicaciones con la siguiente estructura:

```json
{
  "id": "uuid",
  "name": "string",
  "description": "string",
  "type": "string",
  "latitude": "float",
  "longitude": "float"
}
```

## Endpoints Disponibles

### GET /ubicaciones/
Retorna todas las ubicaciones disponibles.

**Ejemplo de uso:**
```bash
curl http://localhost:8000/ubicaciones/
```

### GET /ubicaciones/prontos/
Retorna solo las ubicaciones de tipo Pronto.

**Ejemplo de uso:**
```bash
curl http://localhost:8000/ubicaciones/prontos/
```

### GET /ubicaciones/bencineras/
Retorna solo las ubicaciones de tipo Bencinera.

**Ejemplo de uso:**
```bash
curl http://localhost:8000/ubicaciones/bencineras/
```

### GET /ubicaciones/servicios/
Retorna solo las ubicaciones de tipo Servicio.

**Ejemplo de uso:**
```bash
curl http://localhost:8000/ubicaciones/servicios/
```

### GET /ubicaciones/otros/
Retorna las ubicaciones de tipo Otro.

**Ejemplo de uso:**
```bash
curl http://localhost:8000/ubicaciones/otros/
```

## Paginación

Todos los endpoints soportan paginación mediante query parameters:

- `skip`: Número de registros a saltar
- `limit`: Número máximo de registros a retornar

**Ejemplo:**
```bash
curl http://localhost:8000/ubicaciones/?skip=0&limit=10
```

## Manejo de Errores

La API utiliza los siguientes códigos de estado HTTP:

- `200`: Éxito
- `404`: Recurso no encontrado
- `422`: Error de validación
- `500`: Error interno del servidor

Ejemplo de respuesta de error:
```json
{
  "detail": "Descripción del error"
}
```
