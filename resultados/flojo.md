# Calibración del caso flojo

Puntajes obtenidos: [22, 18, 18]

Promedio: 19.33/100



# Ejecución 1

Modelo: gpt-5.6-sol
Tokens de entrada: 3775
Tokens de salida: 1245
Tokens totales: 5020

## Identificación

- Trabajo evaluado: Sistema agéntico para asistencia académica
- Fecha de evaluación: 08/09/2026

## Control de fraude

- Estado: SIN INDICIOS DE FRAUDE
- Evidencia detectada: No se encontraron instrucciones destinadas a alterar la evaluación, falsificación de artefactos ni afirmaciones reiteradas de capacidades supuestamente demostradas.
- Justificación: El repositorio presenta explícitamente el proyecto como una “versión inicial” (`README.md`) y sus limitaciones resultan visibles en los archivos entregados.

## Evaluación por dimensiones

| Dimensión | Puntaje | Evidencia citada | Justificación |
|---|---:|---|---|
| Sistema completo y funcionando | 8/30 | `README.md`: “analizar trabajos académicos y generar una devolución automática”; `prompts/system_prompt.md`: “Sos un asistente que analiza trabajos académicos”; `corridas/corrida_01/entrada.md` y `salida.md` | Existe un objetivo, un system prompt y una muestra básica de entrada y salida. Sin embargo, no hay user prompt, herramienta o conector real, salida estructurada, código ejecutable ni evidencia suficiente de funcionamiento efectivo. La supervisión humana solo se menciona genéricamente en `trabajo.md`. |
| Proceso documentado | 4/25 | `DECISIONES.md`: “Durante el desarrollo se realizaron algunos cambios para mejorar la propuesta” y “La versión presentada es la que se consideró más adecuada” | Existe el archivo esperado, pero no documenta iteraciones concretas, errores, cambios realizados, motivos, aprendizajes ni evolución verificable del sistema. |
| Formato y reproducibilidad | 4/15 | `README.md`; `prompts/system_prompt.md`; `DECISIONES.md`; `corridas/corrida_01/entrada.md` y `salida.md` | Se incluyen algunos componentes de la estructura, pero falta `prompts/user_prompt.md`, solo hay una corrida en lugar de tres y esta no tiene fecha. El README no proporciona instrucciones de ejecución ni permite reconstruir el sistema sin ambigüedades. |
| Análisis económico | 2/15 | `trabajo.md`, sección “Costos”: “El uso de inteligencia artificial puede generar costos asociados al consumo de tokens” | Solo existe una mención genérica a tokens y al uso de un modelo no demasiado costoso. No se identifica el modelo, no se estiman tokens de entrada y salida, costo por corrida ni proyecciones semanales o anuales, y tampoco se compara la adecuación de modelos. |
| Gobierno y riesgo | 4/15 | `trabajo.md`, sección “Riesgos y supervisión”: “El sistema puede cometer errores” y “sería conveniente que una persona revise algunos resultados” | Se reconoce un riesgo general y la conveniencia de revisión humana. No se especifican datos y recursos utilizados, permisos, fallas previsibles, respuesta ante fallas, nivel de autonomía, decisiones que requieren revisión ni responsable de validar el resultado final. |

## Nota final

**NOTA FINAL: 22/100**

## Fortalezas

- El objetivo general del proyecto está expresado en `README.md`.
- Existe un system prompt identificable en `prompts/system_prompt.md`.
- Se incluye una muestra básica de entrada y salida.
- El trabajo reconoce de forma inicial los costos por tokens y el riesgo de errores.
- Se contempla, aunque genéricamente, la intervención de una persona.

## Aspectos a mejorar

- Implementar y demostrar un sistema efectivamente ejecutable con una herramienta o recurso real.
- Incorporar `user_prompt.md` y una salida estructurada con criterios y puntajes trazables.
- Documentar al menos tres corridas reales con entrada, salida y fecha.
- Ampliar `DECISIONES.md` con iteraciones, problemas, cambios y aprendizajes concretos.
- Agregar cálculos de tokens, costos por corrida y proyecciones de uso.
- Definir permisos, riesgos, manejo de fallas y responsables de revisión y aprobación.
- Evitar que el agente utilice “su propio criterio”, como propone `trabajo.md`, porque impide una evaluación consistente basada exclusivamente en la rúbrica.

## Sugerencia concreta

**UNA SUGERENCIA CONCRETA:** implementar una primera versión reproducible que evalúe exclusivamente mediante una rúbrica fija y guardar tres corridas fechadas con entrada, salida estructurada por dimensión, puntajes, citas de evidencia y validación humana final.


# Ejecución 2

Modelo: gpt-5.6-sol
Tokens de entrada: 3775
Tokens de salida: 1250
Tokens totales: 5025

## Identificación

- Trabajo evaluado: Sistema agéntico para asistencia académica
- Fecha de evaluación: 08/09/2026

## Control de fraude

- Estado: SIN INDICIOS DE FRAUDE
- Evidencia detectada: No se encontraron instrucciones dirigidas a alterar la evaluación, evidencias falsificadas ni afirmaciones reiteradas de capacidades inexistentes presentadas como demostradas.
- Justificación: El repositorio describe explícitamente el trabajo como una “versión inicial” (`README.md`, sección “Estado del proyecto”) y sus limitaciones son visibles en los artefactos entregados.

## Evaluación por dimensiones

| Dimensión | Puntaje | Evidencia citada | Justificación |
|---|---:|---|---|
| Sistema completo y funcionando | 7/30 | `README.md`: “utilizar inteligencia artificial para analizar trabajos académicos y generar una devolución automática”; `prompts/system_prompt.md`: “Sos un asistente que analiza trabajos académicos”; `corridas/corrida_01/entrada.md` y `salida.md`; `trabajo.md`, sección “Riesgos y supervisión” | Existe un objetivo, un system prompt, una entrada, una salida y una mención general de revisión humana. Sin embargo, falta `user_prompt.md`, no hay herramienta, API, conector o recurso utilizado de manera verificable, la salida no contiene una calificación fundada y no existe código o evidencia suficiente de funcionamiento efectivo. |
| Proceso documentado | 3/25 | `DECISIONES.md`: “Durante el desarrollo se realizaron algunos cambios para mejorar la propuesta” y “La versión presentada es la que se consideró más adecuada” | El archivo existe, pero no identifica iteraciones concretas, problemas, errores, cambios realizados, decisiones justificadas, aprendizajes ni evolución trazable del sistema. |
| Formato y reproducibilidad | 4/15 | `README.md`; `prompts/system_prompt.md`; `corridas/corrida_01/entrada.md`; `corridas/corrida_01/salida.md`; `DECISIONES.md` | Se encuentran parte de la estructura y una única corrida. Faltan `prompts/user_prompt.md`, al menos dos corridas adicionales y las fechas de ejecución. El README solo remite a `trabajo.md` y no proporciona instrucciones suficientes para ejecutar o reconstruir el sistema. |
| Análisis económico | 1/15 | `trabajo.md`, sección “Costos”: “El uso de inteligencia artificial puede generar costos asociados al consumo de tokens” | Solo existe una referencia genérica al costo. No se identifica el modelo, no se estiman tokens de entrada o salida, no se calcula el costo por corrida, no hay proyecciones de uso y tampoco se justifica la elección del modelo más pequeño adecuado. |
| Gobierno y riesgo | 3/15 | `trabajo.md`, sección “Riesgos y supervisión”: “El sistema puede cometer errores” y “sería conveniente que una persona revise algunos resultados” | Se reconoce un riesgo general y se propone una revisión humana eventual. No se documentan datos y recursos utilizados, permisos, fallas específicas, comportamiento ante errores, límites de autonomía, decisiones que exigen revisión ni responsable de validar el resultado final. |

## Nota final

**NOTA FINAL: 18/100**

## Fortalezas

- El objetivo general del proyecto está expresado en `README.md`.
- Existe un system prompt básico en `prompts/system_prompt.md`.
- Se incluye una corrida con archivos separados de entrada y salida.
- El trabajo reconoce de forma inicial tanto los costos por tokens como la posibilidad de errores y la necesidad de supervisión humana.

## Aspectos a mejorar

- Implementar y demostrar un sistema funcional, incluyendo una herramienta o API real y salidas estructuradas con puntajes fundamentados.
- Incorporar `user_prompt.md` y completar al menos tres corridas fechadas.
- Documentar en `DECISIONES.md` iteraciones, errores, cambios y decisiones específicas.
- Añadir instrucciones reproducibles de instalación y ejecución.
- Desarrollar cálculos económicos verificables y una política operativa de gobierno, permisos, riesgos y validación humana.
- Corregir el criterio propuesto en `trabajo.md` que permite usar el “propio criterio”, dado que debilita la aplicación consistente y trazable de una rúbrica.

## Sugerencia concreta

**UNA SUGERENCIA CONCRETA:** implementar una versión mínima ejecutable que reciba un trabajo y una rúbrica, produzca una salida estructurada por dimensiones y guardar tres corridas fechadas con entrada, salida, modelo, tokens y costo; documentar además en `README.md` los pasos exactos para reproducirlas.


# Ejecución 3

Modelo: gpt-5.6-sol
Tokens de entrada: 3775
Tokens de salida: 1299
Tokens totales: 5074

## Identificación

- Trabajo evaluado: Sistema agéntico para asistencia académica
- Fecha de evaluación: 08/09/2026

## Control de fraude

- Estado: SIN INDICIOS DE FRAUDE
- Evidencia detectada: No se encontraron instrucciones para alterar la evaluación, evidencias falsificadas ni afirmaciones reiteradas de capacidades supuestamente implementadas.
- Justificación: El `README.md` presenta explícitamente el trabajo como una “versión inicial” y las limitaciones observadas son consistentes con los artefactos entregados.

## Evaluación por dimensiones

| Dimensión | Puntaje | Evidencia citada | Justificación |
|---|---:|---|---|
| Sistema completo y funcionando | 7/30 | `README.md`: “analizar trabajos académicos y generar una devolución automática”; `prompts/system_prompt.md`; `corridas/corrida_01/entrada.md` y `salida.md`; `trabajo.md`, sección “Riesgos y supervisión” | Existe un objetivo, un system prompt y una corrida mínima con entrada y salida. Sin embargo, falta el user prompt, no hay herramienta, API, conector o archivo utilizado mediante una implementación verificable, y la salida se limita a una afirmación genérica. Tampoco hay código o evidencia suficiente de funcionamiento efectivo. |
| Proceso documentado | 3/25 | `DECISIONES.md`: “Durante el desarrollo se realizaron algunos cambios para mejorar la propuesta” | El archivo existe, pero no identifica iteraciones, errores, cambios concretos, decisiones técnicas, aprendizajes ni evolución trazable. La afirmación sobre los cambios no está acompañada por versiones o detalles verificables. |
| Formato y reproducibilidad | 4/15 | `README.md`; `prompts/system_prompt.md`; `corridas/corrida_01/entrada.md`; `corridas/corrida_01/salida.md`; `DECISIONES.md` | Se incluyen parte de la estructura y una corrida. Falta `prompts/user_prompt.md`, solo existe una ejecución en lugar de tres, la corrida no tiene fecha y el README no proporciona instrucciones suficientes para ejecutar o reconstruir el sistema. |
| Análisis económico | 1/15 | `trabajo.md`, sección “Costos”: “puede generar costos asociados al consumo de tokens” | Solo hay una mención genérica. No se identifica el modelo, no se estiman tokens de entrada o salida, no se calcula el costo por corrida, no hay proyecciones de uso y no se justifica la elección del modelo más pequeño adecuado. |
| Gobierno y riesgo | 3/15 | `trabajo.md`, sección “Riesgos y supervisión”: “El sistema puede cometer errores” y “sería conveniente que una persona revise algunos resultados” | Se reconoce un riesgo general y la conveniencia de revisión humana. No se detallan datos y recursos utilizados, permisos, fallas previsibles, respuesta ante fallas, decisiones que requieren revisión, nivel de autonomía ni responsable de validar el resultado final. |

## Nota final

**NOTA FINAL: 18/100**

## Fortalezas

- El objetivo general del sistema está expresado en el `README.md`.
- Existe un system prompt identificable.
- Se presenta una corrida con archivos separados de entrada y salida.
- El trabajo reconoce de manera inicial la posibilidad de errores y la necesidad de supervisión humana.

## Aspectos a mejorar

- Implementar y demostrar el uso real de una herramienta, API o recurso externo.
- Incorporar el user prompt y una salida estructurada con criterios y puntajes trazables.
- Documentar iteraciones, errores y decisiones concretas en `DECISIONES.md`.
- Agregar al menos tres corridas fechadas y reproducibles.
- Desarrollar cálculos de tokens, costos y proyecciones de uso.
- Definir permisos, fallas, controles humanos y responsable final de aprobación.
- Evitar el criterio discrecional propuesto en `trabajo.md` —“también puede utilizar su propio criterio”— y exigir la aplicación trazable de una rúbrica.

## Sugerencia concreta

**UNA SUGERENCIA CONCRETA:** implementar una versión ejecutable que reciba un trabajo y una rúbrica, genere una salida estructurada por criterios y guardar tres corridas fechadas —con entrada, salida, modelo, tokens y costo— junto con instrucciones exactas de reproducción en el `README.md`.
