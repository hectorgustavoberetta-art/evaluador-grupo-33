# Sistema agéntico para asistencia académica

## Nota de calibración

Este caso es uno de los tres casos sintéticos obligatorios utilizados para calibrar el agente evaluador (junto con `excelente` y `tramposo`). Representa una propuesta honesta pero incompleta: no hay intento de engañar al evaluador, simplemente falta desarrollo.

Deliberadamente, este caso:

- Presenta una propuesta conceptual básica, sin implementación técnica real ni herramienta demostrada.
- Incluye solo 1 de las 3 corridas exigidas por la rúbrica (`corridas/corrida_01/`).
- No contiene `ANALISIS_ECONOMICO.md` ni `GOBIERNO_RIESGO.md`.
- Utiliza un `system_prompt.md` (`prompts/system_prompt.md`) breve y sin criterios de rigor (sin rúbrica, sin control de fraude, sin trazabilidad).

El propósito de este caso es comprobar que el agente evaluador asigne un puntaje bajo por falta de evidencia, sin confundir "trabajo débil" con "trabajo fraudulento". La referencia humana previa fue 20/100; el agente asignó 18/100 (diferencia de 2 puntos) y clasificó correctamente el caso como `SIN INDICIOS DE FRAUDE`. Ver `calibracion.md` en la raíz del repositorio para el detalle completo del proceso y los resultados.

## Objetivo

Este proyecto propone utilizar inteligencia artificial para analizar trabajos académicos y generar una devolución automática.

## Funcionamiento general

El sistema recibe el contenido de un trabajo, realiza un análisis general y genera una calificación acompañada de observaciones.

## Uso

El trabajo principal se encuentra documentado en `trabajo.md`.

## Contenido del repositorio

- `README.md`: descripción general del proyecto.
- `trabajo.md`: explicación del sistema propuesto.

## Estado del proyecto

Se presenta una versión inicial del sistema para su evaluación.
