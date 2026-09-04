# DECISIONES — Historial del proyecto

## Iteración 1 — Diseño inicial

Se definió como objetivo construir un agente evaluador capaz de corregir trabajos académicos utilizando una rúbrica explícita.

La primera versión se concentró en leer un único archivo y devolver una calificación general.

### Problema detectado

La salida era demasiado general y no permitía reconstruir por qué se asignaba cada puntaje.

### Decisión

Se incorporó una estructura obligatoria de salida con evidencia, justificación y puntaje por dimensión.

---

## Iteración 2 — Uso de evidencia verificable

Se observó que el agente podía aceptar afirmaciones presentes en un README sin comprobar si estaban respaldadas por archivos reales.

### Problema detectado

Una descripción convincente podía recibir puntaje aun cuando el repositorio no contuviera los artefactos mencionados.

### Decisión

Se modificó el system prompt para exigir evidencia verificable y para no otorgar puntaje por capacidades declaradas pero no demostradas.

---

## Iteración 3 — Lectura de repositorios completos

La versión inicial evaluaba principalmente archivos individuales.

### Problema detectado

El Trabajo Final exige evaluar repositorios con múltiples archivos y carpetas.

### Decisión

Se adaptó el evaluador para recorrer carpetas y leer de manera recursiva los archivos relevantes del repositorio.

---

## Iteración 4 — Compatibilidad de archivos

Durante las pruebas se detectaron errores al leer algunos archivos generados en Windows.

### Problema detectado

Algunos documentos utilizaban codificación `cp1252` en lugar de UTF-8.

### Decisión

Se incorporó una segunda lectura automática con `cp1252` cuando falla la decodificación UTF-8.

---

## Iteración 5 — Control de fraude

Se prepararon casos adversariales para comprobar si un trabajo podía intentar manipular al evaluador.

### Problema detectado

Una instrucción dentro del trabajo podía intentar ordenar al agente que ignorara la rúbrica o asignara una nota específica.

### Decisión

Se incorporó un control de fraude con tres estados:

- SIN INDICIOS DE FRAUDE;
- POSIBLE FRAUDE;
- FRAUDE DETECTADO.

Solo se declara fraude cuando existe evidencia concreta y suficiente.

---

## Iteración 6 — Alineación con la rúbrica oficial

La primera versión de la rúbrica utilizaba criterios generales de calidad académica.

### Problema detectado

Esos criterios no coincidían exactamente con la rúbrica oficial del Trabajo Final.

### Decisión

Se reemplazó la rúbrica por las cinco dimensiones oficiales:

1. Sistema completo y funcionando.
2. Proceso documentado.
3. Formato y reproducibilidad.
4. Análisis económico.
5. Gobierno y riesgo.

También se actualizó el system prompt y el formato de salida para utilizar esas mismas dimensiones.

---

## Estado actual

El sistema puede leer trabajos, aplicar una rúbrica estructurada, citar evidencia, generar una salida consistente, detectar intentos de manipulación y trabajar sobre carpetas que representan repositorios.

Las decisiones anteriores se conservan para que el proceso de construcción pueda ser revisado y reproducido.
