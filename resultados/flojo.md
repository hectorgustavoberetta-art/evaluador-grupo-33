# Calibración del caso flojo

Puntajes obtenidos: [19, 20, 19]

Promedio: 19.33/100



# Ejecución 1

Modelo: gpt-5.6-sol
Tokens de entrada: 3775
Tokens de salida: 1498
Tokens totales: 5273

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


# Ejecución 2

Modelo: gpt-5.6-sol
Tokens de entrada: 3775
Tokens de salida: 1278
Tokens totales: 5053

## Identificación

- Trabajo evaluado: Sistema agéntico para asistencia académica
- Fecha de evaluación: 08/09/2026

## Control de fraude

- Estado: SIN INDICIOS DE FRAUDE
- Evidencia detectada: No se encontraron instrucciones destinadas a alterar la evaluación, falsificación de resultados ni afirmaciones reiteradas de capacidades implementadas sin respaldo.
- Justificación: La entrega se presenta explícitamente como una versión inicial y sus limitaciones resultan visibles en los archivos del repositorio.

## Evaluación por dimensiones

| Dimensión | Puntaje | Evidencia citada | Justificación |
|---|---:|---|---|
| Sistema completo y funcionando | 7/30 | `README.md`, sección “Objetivo”; `prompts/system_prompt.md`; `corridas/corrida_01/entrada.md` y `salida.md`; `trabajo.md`, sección “Riesgos y supervisión” | Existe un objetivo, un system prompt y una corrida básica. Sin embargo, falta el user prompt, no hay herramientas o conectores reales, la salida no presenta una estructura de evaluación suficiente y la supervisión humana es vaga. La única corrida no demuestra de manera verificable un funcionamiento efectivo: contiene una entrada genérica y una respuesta sin nota, criterios ni evidencia. |
| Proceso documentado | 3/25 | `DECISIONES.md`: “Durante el desarrollo se realizaron algunos cambios para mejorar la propuesta” y “La versión presentada es la que se consideró más adecuada” | La documentación afirma que hubo cambios, pero no identifica iteraciones, errores, decisiones concretas, modificaciones de alcance ni aprendizajes. No es posible reconstruir la evolución real del sistema. |
| Formato y reproducibilidad | 4/15 | `README.md`; `prompts/system_prompt.md`; `corridas/corrida_01/entrada.md` y `salida.md`; `DECISIONES.md` | Están presentes el README, la carpeta de prompts, un system prompt, una corrida y el archivo de decisiones. Faltan `prompts/user_prompt.md`, tres corridas reales con fecha y procedimientos suficientes de instalación o ejecución. El README solo remite a `trabajo.md`, por lo que un tercero no puede reproducir el sistema. |
| Análisis económico | 2/15 | `trabajo.md`, sección “Costos”: “El uso de inteligencia artificial puede generar costos asociados al consumo de tokens” y “Se intentará utilizar un modelo que no resulte demasiado costoso” | Solo se mencionan genéricamente tokens y costos. No se identifica el modelo, no se estiman tokens de entrada o salida, no se calcula el costo por corrida ni se realizan proyecciones semanales o anuales. Tampoco se compara o justifica verificablemente la elección del modelo. |
| Gobierno y riesgo | 4/15 | `trabajo.md`, sección “Riesgos y supervisión”: “El sistema puede cometer errores” y “sería conveniente que una persona revise algunos resultados” | Se reconoce un riesgo general y se propone cierta revisión humana. No se definen sistemas y datos utilizados, permisos, fallas específicas, respuesta ante errores, nivel de autonomía, decisiones que requieren revisión ni responsable de validar el resultado final. |

## Nota final

**NOTA FINAL: 20/100**

## Fortalezas

- El objetivo general del sistema está expresado en `README.md`.
- Existe un system prompt verificable en `prompts/system_prompt.md`.
- Se incluye una corrida básica con entrada y salida.
- El trabajo reconoce que el agente puede equivocarse y que corresponde alguna intervención humana.

## Aspectos a mejorar

- Implementar y demostrar un sistema ejecutable con una herramienta o API real.
- Incorporar el user prompt y una salida estructurada basada exclusivamente en una rúbrica.
- Documentar iteraciones, errores y decisiones concretas en `DECISIONES.md`.
- Agregar al menos tres corridas fechadas, completas y reproducibles.
- Desarrollar cálculos de tokens, costos y proyecciones de uso.
- Definir permisos, límites de autonomía, mecanismos de fallo y responsable de aprobación final.

## Sugerencia concreta

**UNA SUGERENCIA CONCRETA:** implementar una versión ejecutable que aplique una rúbrica fija y guardar tres corridas fechadas con entrada completa, salida estructurada, modelo utilizado, consumo de tokens y costo; luego documentar en `DECISIONES.md` qué falló y qué se modificó entre cada corrida.


# Ejecución 3

Modelo: gpt-5.6-sol
Tokens de entrada: 3775
Tokens de salida: 1379
Tokens totales: 5154

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
