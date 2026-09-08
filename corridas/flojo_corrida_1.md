# Corrida de calibración

- Caso: flojo
- Ejecución: 1
- Fecha y hora: 2026-09-08T17:05:48-03:00
- Modelo: gpt-5.6-sol
- Tokens de entrada: 3775
- Tokens de salida: 1498
- Tokens totales: 5273

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
- Evidencia detectada: No se encontraron instrucciones para alterar la evaluación, evidencias falsificadas ni afirmaciones reiteradas de capacidades avanzadas no demostradas.
- Justificación: El repositorio presenta explícitamente el proyecto como una “versión inicial” en `README.md`, y sus limitaciones son consistentes con los artefactos entregados.

## Evaluación por dimensiones

| Dimensión | Puntaje | Evidencia citada | Justificación |
|---|---:|---|---|
| Sistema completo y funcionando | 7/30 | `README.md`: “utilizar inteligencia artificial para analizar trabajos académicos”; `prompts/system_prompt.md`: “Sos un asistente que analiza trabajos académicos”; `corridas/corrida_01/entrada.md` y `salida.md` | Existe un objetivo, un system prompt y una corrida básica. Sin embargo, no hay `user_prompt.md`, código ejecutable, herramienta o API utilizada de forma verificable, salida estructurada ni evidencia suficiente de funcionamiento efectivo. La supervisión humana solo se plantea como posibilidad. |
| Proceso documentado | 3/25 | `DECISIONES.md`: “Durante el desarrollo se realizaron algunos cambios para mejorar la propuesta” y “La versión presentada es la que se consideró más adecuada” | La documentación es superficial. No identifica iteraciones concretas, problemas, errores, cambios realizados, motivos de las decisiones, aprendizajes ni evolución trazable del sistema. |
| Formato y reproducibilidad | 4/15 | Existen `README.md`, `DECISIONES.md`, `prompts/system_prompt.md` y `corridas/corrida_01/entrada.md`/`salida.md`; `README.md`: “El trabajo principal se encuentra documentado en trabajo.md” | Se cumple parcialmente la estructura, pero falta `prompts/user_prompt.md`. Solo existe una corrida, sin fecha, en lugar de las tres requeridas. Tampoco hay instrucciones de ejecución, configuración, modelo o procedimiento suficiente para reproducir el resultado. |
| Análisis económico | 2/15 | `trabajo.md`, sección “Costos”: “puede generar costos asociados al consumo de tokens” y “se intentará utilizar un modelo que no resulte demasiado costoso” | Solo hay una mención genérica a tokens y costos. No se identifica el modelo, no se estiman tokens de entrada o salida, no se calcula el costo por corrida ni se presentan proyecciones semanales o anuales. Tampoco se compara o justifica la elección de un modelo pequeño. |
| Gobierno y riesgo | 3/15 | `trabajo.md`, sección “Riesgos y supervisión”: “El sistema puede cometer errores” y “sería conveniente que una persona revise algunos resultados” | Se reconoce un riesgo general y la conveniencia de revisión humana, pero no se detallan datos utilizados, permisos, recursos, fallas previsibles, respuesta ante fallos, decisiones que requieren revisión, nivel de autonomía ni responsable de validar el resultado final. |

## Nota final

**NOTA FINAL: 19/100**

## Fortalezas

- El objetivo general del proyecto está expresado con claridad.
- Existe un system prompt verificable.
- Se incluye una corrida con archivos separados de entrada y salida.
- El trabajo reconoce que el agente puede equivocarse y que corresponde incorporar supervisión humana.
- La presentación como “versión inicial” es consistente con el alcance real de los artefactos.

## Aspectos a mejorar

- Implementar y demostrar una herramienta, API o sistema ejecutable real.
- Incorporar `user_prompt.md` y definir una salida estructurada con criterios y puntajes trazables.
- Documentar iteraciones, errores, decisiones y cambios concretos en `DECISIONES.md`.
- Agregar al menos tres corridas completas, fechadas y reproducibles.
- Identificar el modelo y calcular tokens, costo por corrida y proyecciones de uso.
- Definir permisos, riesgos, manejo de fallas y puntos obligatorios de validación humana.
- Eliminar el uso del “propio criterio” del agente indicado en `trabajo.md` y exigir la aplicación exclusiva de una rúbrica verificable.

## Sugerencia concreta

**UNA SUGERENCIA CONCRETA:** implementar una versión mínima ejecutable que aplique una rúbrica fija y guardar tres corridas fechadas con entrada, salida estructurada, modelo utilizado, tokens consumidos, costo calculado y validación final de un responsable humano.
