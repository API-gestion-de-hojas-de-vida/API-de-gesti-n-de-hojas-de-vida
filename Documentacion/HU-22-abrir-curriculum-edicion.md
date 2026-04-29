## 🔁 Flujo Esperado

- El usuario autenticado accede al listado de sus hojas de vida y selecciona una para editar.
- El sistema verifica que la hoja de vida pertenezca al usuario autenticado.
- El sistema verifica que no haya otra sesión activa editando la misma hoja de vida simultáneamente para evitar conflictos de concurrencia.
- Si la hoja de vida tiene estado "finalizada", el sistema la cambia automáticamente a "borrador" y notifica al usuario que deberá volver a finalizar tras los cambios.
- El sistema consulta todos los datos relacionados a la hoja de vida incluyendo perfil, todos los bloques de experiencia ordenados, todos los bloques de educación ordenados, habilidades y la plantilla asignada.
- El sistema verifica si la plantilla asignada sigue activa. Si fue desactivada, notifica al usuario y le permite continuar editando pero le solicita seleccionar una nueva plantilla antes de finalizar.
- El sistema retorna todos los datos en el mismo formato en que fueron guardados para inyección directa en el formulario del frontend.
- El sistema activa el mecanismo de autoguardado cada 2 minutos para evitar pérdida de información.
- El sistema registra en el historial de versiones que se inició una nueva sesión de edición con fecha y hora.

## ✅ Criterios de Aceptación

### 1. 🔍 Estructura y lógica del servicio

- [ ] Se expone un endpoint GET para cargar la hoja de vida en modo edición.
- [ ] Se valida que la hoja de vida pertenezca al usuario autenticado antes de retornar datos.
- [ ] Se controla la concurrencia para evitar que dos sesiones editen la misma hoja simultáneamente.
- [ ] Si la hoja está finalizada, se cambia automáticamente a estado borrador al abrir en modo edición.
- [ ] Se retornan todos los datos relacionados incluyendo perfil, experiencia, educación, habilidades y plantilla.
- [ ] Los bloques de experiencia y educación se retornan en el orden definido por el usuario.
- [ ] Se verifica si la plantilla asignada sigue activa y se notifica si fue desactivada.
- [ ] Se activa autoguardado cada 2 minutos mientras el usuario tenga la sesión de edición abierta.
- [ ] Se registra en historial de versiones el inicio de la sesión de edición con fecha y hora.
- [ ] Se retorna un token de sesión de edición para controlar la concurrencia y el autoguardado.
