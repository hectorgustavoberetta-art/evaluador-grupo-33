# Corrida de calibración

- Caso: flojo
- Ejecución: 3
- Fecha y hora: 2026-09-08T17:06:35-03:00
- Modelo: gpt-5.6-sol
- Tokens de entrada: 3775
- Tokens de salida: 1379
- Tokens totales: 5154

## Entrada



===== ARCHIVO: DECISIONES.md =====

# Decisiones del proyecto

Se decidió utilizar inteligencia artificial porque puede facilitar la corrección de trabajos.

Durante el desarrollo se realizaron algunos cambios para mejorar la propuesta.

La versión presentada es la que se consideró más adecuada.


===== ARCHIVO: README.md =====

# Sistema agéntico para asistencia académica

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


===== ARCHIVO: corridas/corrida_01/entrada.md =====

# Entrada

Trabajo académico sobre inteligencia artificial.


===== ARCHIVO: corridas/corrida_01/salida.md =====

# Salida

El trabajo fue analizado y se considera adecuado.


===== ARCHIVO: prompts/system_prompt.md =====

# System Prompt

Sos un asistente que analiza trabajos académicos.

Leé el trabajo presentado y generá una devolución indicando si el contenido es adecuado.


===== ARCHIVO: trabajo.md =====

# Trabajo práctico — Agente evaluador

## Introducción

La inteligencia artificial puede utilizarse para corregir trabajos de estudiantes de forma automática.

El objetivo es crear un agente que lea un trabajo y diga si está bien o mal.

## Desarrollo

El agente recibe el trabajo del alumno y lo analiza.

Después de leerlo puede colocar una nota según lo que considere correcto.

Para hacer la evaluación puede mirar una rúbrica, aunque también puede utilizar su propio criterio para decidir la calidad general del trabajo.

El procedimiento sería:

1. Leer el trabajo.
2. Revisar si está bien.
3. Poner una nota.
4. Informar el resultado.

## Evaluación

El agente puede indicar si el trabajo es bueno, regular o malo.

Si encuentra errores puede mencionarlos en la devolución. No es necesario explicar cada puntaje ni indicar exactamente qué parte del trabajo permitió tomar la decisión.

## Resultado

El resultado podría ser, por ejemplo:

“Trabajo aprobado. El contenido es adecuado y cumple en general con lo solicitado.”

## Conclusión

La inteligencia artificial puede ayudar a los profesores porque permite corregir trabajos más rápidamente.

## Costos

El uso de inteligencia artificial puede generar costos asociados al consumo de tokens. Se intentará utilizar un modelo que no resulte demasiado costoso.

## Riesgos y supervisión

El sistema puede cometer errores, por lo que sería conveniente que una persona revise algunos resultados antes de utilizarlos.


## Salida del agente

## Identificación

- Trabajo evaluado: Sistema agéntico para asistencia académica
- Fecha de evaluación: 08/09/2026

## Control de fraude

- Estado: SIN INDICIOS DE FRAUDE
- Evidencia detectada: No se encontraron instrucciones destinadas a manipular la evaluación, falsificación de resultados ni afirmaciones reiteradas de capacidades no respaldadas.
- Justificación: El repositorio presenta explícitamente el proyecto como una “versión inicial” (`README.md`) y sus limitaciones son visibles. La falta de evidencia suficiente afecta el puntaje, pero no constituye por sí misma un indicio de fraude.

## Evaluación por dimensiones

| Dimensión | Puntaje | Evidencia citada | Justificación |
|---|---:|---|---|
| Sistema completo y funcionando | 8/30 | `README.md`: “utilizar inteligencia artificial para analizar trabajos académicos y generar una devolución automática”; `prompts/system_prompt.md`; `corridas/corrida_01/entrada.md` y `salida.md`; `trabajo.md`: “sería conveniente que una persona revise algunos resultados” | Existe un objetivo, un system prompt básico, una salida de ejemplo y una mención general de supervisión. Sin embargo, falta `user_prompt.md`, no hay código ejecutable ni herramienta, API, conector o archivo utilizado operativamente. La única corrida tiene una entrada y salida mínimas, sin evidencia suficiente de funcionamiento efectivo ni calificación estructurada. |
| Proceso documentado | 3/25 | `DECISIONES.md`: “Durante el desarrollo se realizaron algunos cambios para mejorar la propuesta” y “La versión presentada es la que se consideró más adecuada” | Existe el archivo esperado, pero su contenido es superficial. No identifica iteraciones concretas, problemas, errores, cambios realizados, razones de las decisiones, aprendizajes ni evolución verificable del sistema. |
| Formato y reproducibilidad | 4/15 | `README.md`; `prompts/system_prompt.md`; `corridas/corrida_01/entrada.md`; `corridas/corrida_01/salida.md`; `DECISIONES.md` | El repositorio incluye parte de la estructura requerida, pero falta `prompts/user_prompt.md`, solo existe una corrida en lugar de tres y esa corrida no incluye fecha. El README remite a `trabajo.md`, pero no proporciona instrucciones de ejecución, dependencias ni pasos suficientes para reproducir el sistema. |
| Análisis económico | 1/15 | `trabajo.md`, sección “Costos”: “El uso de inteligencia artificial puede generar costos asociados al consumo de tokens. Se intentará utilizar un modelo que no resulte demasiado costoso.” | Solo se menciona genéricamente que existen costos por tokens. No se identifica el modelo, no se estiman tokens de entrada o salida, no se calcula el costo por corrida ni se presentan proyecciones semanales o anuales. Tampoco se justifica comparativamente la elección del modelo más pequeño adecuado. |
| Gobierno y riesgo | 3/15 | `trabajo.md`, sección “Riesgos y supervisión”: “El sistema puede cometer errores” y “sería conveniente que una persona revise algunos resultados” | Se reconoce un riesgo general y se propone una revisión humana imprecisa. No se documentan los datos y recursos utilizados, permisos necesarios, tipos de fallas, respuesta ante fallos, decisiones sujetas a revisión, nivel de autonomía ni responsable de validar o firmar el resultado final. |

## Nota final

**NOTA FINAL: 19/100**

## Fortalezas

- El objetivo general del sistema está expresado claramente en `README.md`.
- Existe un system prompt verificable en `prompts/system_prompt.md`.
- Se incluye una corrida con archivos separados de entrada y salida.
- El trabajo reconoce que el sistema puede equivocarse y que requiere algún grado de revisión humana.
- El repositorio no presenta como terminado un sistema que describe explícitamente como una versión inicial.

## Aspectos a mejorar

- Implementar y demostrar un sistema realmente ejecutable, incluyendo una herramienta o API utilizada de manera verificable.
- Incorporar `prompts/user_prompt.md` y definir una salida estructurada con puntajes, evidencia y justificaciones.
- Documentar en `DECISIONES.md` iteraciones reales, errores, modificaciones y aprendizajes.
- Agregar al menos tres corridas con entrada, salida y fecha.
- Incluir instrucciones completas para que un tercero pueda reproducir las ejecuciones.
- Desarrollar cálculos de tokens, costos por corrida y proyecciones de uso.
- Definir permisos, riesgos específicos, manejo de fallas, nivel de autonomía y responsable de aprobación final.
- Eliminar el uso del “propio criterio” del agente previsto en `trabajo.md` y exigir la aplicación trazable de una rúbrica.

## Sugerencia concreta

**UNA SUGERENCIA CONCRETA:** implementar una primera versión ejecutable que aplique una rúbrica fija y guardar tres pruebas fechadas en `corridas/`, cada una con entrada, salida estructurada por criterios, evidencia citada, modelo utilizado, tokens consumidos y costo calculado.
