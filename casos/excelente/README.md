# Sistema agéntico de evaluación académica

## Nota de calibración

Este caso es uno de los tres casos sintéticos obligatorios utilizados para calibrar el agente evaluador (junto con `flojo` y `tramposo`). Representa una entrega de alta calidad, con evidencia verificable completa en las cinco dimensiones de la rúbrica:

- `agente/evaluador.py` y `prompts/` (system y user prompt reales).
- Tres corridas completas y reproducibles en `corridas/`, cada una con entrada, salida y metadatos.
- `ANALISIS_ECONOMICO.md` y `GOBIERNO_RIESGO.md` desarrollados en profundidad.
- `DECISIONES.md` que documenta iteraciones reales, no solo el resultado final.

El propósito de este caso es comprobar que el agente evaluador reconozca y puntúe correctamente un trabajo sólido cuando las afirmaciones están respaldadas por artefactos verificables. La referencia humana previa fue 90/100; el agente asignó 91/100 (diferencia de 1 punto). Ver `calibracion.md` en la raíz del repositorio para el detalle completo del proceso y los resultados.

## Objetivo

Este proyecto implementa un agente capaz de evaluar trabajos académicos mediante una rúbrica estructurada y evidencia verificable presente en el repositorio.

## Componentes

- `agente/`: implementación técnica del evaluador.
- `prompts/`: system prompt y user prompt utilizados por el sistema.
- `corridas/`: tres ejecuciones documentadas con entrada, salida y fecha.
- `DECISIONES.md`: historial de iteraciones, problemas y decisiones del proyecto.
- `ANALISIS_ECONOMICO.md`: metodología para analizar tokens, costos y elección del modelo.
- `GOBIERNO_RIESGO.md`: permisos, riesgos, fallas posibles y supervisión humana.
- `rubrica.md`: rúbrica utilizada por el agente.
- `formato_salida.md`: estructura de la evaluación.
- `requirements.txt`: dependencias del proyecto.
- `trabajo.md`: desarrollo general de la propuesta.

## Funcionamiento

El agente recibe un trabajo, analiza la evidencia disponible, aplica la rúbrica y genera una devolución estructurada con puntajes, evidencia y justificación.

La integración con la API utiliza la variable de entorno `OPENAI_API_KEY`, evitando almacenar credenciales en el código.

## Reproducibilidad

El repositorio conserva los prompts, la implementación, las decisiones de diseño y tres corridas documentadas para permitir la revisión del funcionamiento del sistema.

## Supervisión

El agente propone la evaluación, pero la decisión académica definitiva requiere validación humana.
