# Guía de Instalación

## Requisitos Previos

- Python 3.8 o superior
- pip (gestor de paquetes de Python)
- Git

## Pasos de Instalación

### 1. Clonar el Repositorio

```bash
git clone https://github.com/tu-usuario/UBI-COPEC.git
cd UBI-COPEC
```

### 2. Crear Entorno Virtual

=== "Windows"
    ```bash
    python -m venv env
    env\Scripts\activate
    ```

=== "Linux/macOS"
    ```bash
    python -m venv env
    source env/bin/activate
    ```

### 3. Instalar Dependencias

```bash
pip install -r requirements.txt
```

### 4. Configurar Base de Datos

```bash
python data_ejemplo.py
```

### 5. Iniciar Servidor

```bash
uvicorn app.main:app --reload
```

## Verificación de la Instalación

1. Abre tu navegador y visita: `http://localhost:8000/docs`
2. Deberías ver la documentación interactiva de la API
3. Prueba un endpoint, por ejemplo: `http://localhost:8000/places/prontos`

## Solución de Problemas

### Error: No se puede crear la base de datos
- Verifica que tengas permisos de escritura en el directorio `data/`
- Asegúrate de que SQLite esté instalado en tu sistema

### Error: No se puede iniciar el servidor
- Verifica que el puerto 8000 no esté en uso
- Asegúrate de estar en el entorno virtual correcto