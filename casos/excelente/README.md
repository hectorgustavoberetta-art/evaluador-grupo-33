# Sistema agéntico de evaluación académica

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
