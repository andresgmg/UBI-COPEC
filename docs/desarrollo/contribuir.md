# Guía de Contribución

## 🤝 ¿Cómo Contribuir?

¡Gracias por tu interés en contribuir a UBI COPEC API! Este proyecto es open source y todas las contribuciones son bienvenidas.

## 📝 Proceso de Contribución

1. **Fork el Repositorio**
   - Visita el [repositorio en GitHub](https://github.com/tu-usuario/UBI-COPEC)
   - Haz click en el botón "Fork"

2. **Clona tu Fork**
   ```bash
   git clone https://github.com/TU-USERNAME/UBI-COPEC.git
   cd UBI-COPEC
   ```

3. **Crea una Rama**
   ```bash
   git checkout -b feature/tu-feature
   ```

4. **Realiza tus Cambios**
   - Escribe código limpio y mantenible
   - Sigue las convenciones de estilo del proyecto
   - Añade tests si es necesario
   - Actualiza la documentación si es necesario

5. **Commit tus Cambios**
   ```bash
   git add .
   git commit -m "feat: descripción de tus cambios"
   ```
   Usamos [Conventional Commits](https://www.conventionalcommits.org/):
   - `feat:` para nuevas características
   - `fix:` para correcciones de bugs
   - `docs:` para cambios en documentación
   - `test:` para añadir o modificar tests
   - `refactor:` para refactorización de código

6. **Push a tu Fork**
   ```bash
   git push origin feature/tu-feature
   ```

7. **Crea un Pull Request**
   - Ve a tu fork en GitHub
   - Click en "New Pull Request"
   - Describe tus cambios
   - Referencia cualquier issue relacionado

## 🧪 Tests

Antes de enviar tu PR, asegúrate de que:

1. Todos los tests pasan:
   ```bash
   pytest
   ```

2. El código sigue el estilo del proyecto:
   ```bash
   flake8
   black .
   ```

## 📋 Checklist PR

- [ ] He seguido las guías de contribución
- [ ] He añadido tests si era necesario
- [ ] He actualizado la documentación si era necesario
- [ ] He verificado que todos los tests pasan
- [ ] He seguido las convenciones de commit

## 🐛 Reportar Bugs

- Usa el [issue tracker](https://github.com/tu-usuario/UBI-COPEC/issues)
- Describe el bug con detalle
- Incluye pasos para reproducirlo
- Menciona tu entorno (OS, Python version, etc.)

## 💡 Proponer Mejoras

- Abre un issue describiendo tu propuesta
- Explica por qué sería útil
- Discute posibles implementaciones
- Espera feedback antes de empezar a trabajar

## 📜 Código de Conducta

Este proyecto sigue el [Contributor Covenant](https://www.contributor-covenant.org/). Al participar, se espera que respetes este código.
