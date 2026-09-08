# Calibración del caso excelente

Puntajes obtenidos: [92, 90, 91]

Promedio: 91.00/100



# Ejecución 1

Modelo: gpt-5.6-sol
Tokens de entrada: 16894
Tokens de salida: 1750
Tokens totales: 18644

## Identificación

- Trabajo evaluado: Sistema agéntico de evaluación académica
- Fecha de evaluación: 08/09/2026

## Control de fraude

- Estado: SIN INDICIOS DE FRAUDE
- Evidencia detectada: Las referencias a fraude, manipulación y prompt injection aparecen en `DECISIONES.md`, `agente/system_prompt.md`, `prompts/system_prompt.md` y las salidas de `corridas/` como parte del diseño y prueba del mecanismo de control.
- Justificación: No se encontraron instrucciones dirigidas a alterar esta evaluación ni evidencia concreta de falsificación deliberada. Los contenidos relacionados con fraude están contextualizados como documentación funcional del agente.

## Evaluación por dimensiones

| Dimensión | Puntaje | Evidencia citada | Justificación |
|---|---:|---|---|
| Sistema completo y funcionando | 30/30 | `README.md`, secciones “Objetivo” y “Funcionamiento”; `agente/evaluador.py`, funciones `leer_entrega()` y `evaluar_trabajo()` y llamada a `client.responses.create()`; `prompts/system_prompt.md`; `prompts/user_prompt.md`; `formato_salida.md`; `GOBIERNO_RIESGO.md`, secciones “Supervisión humana” y “Validación final”; `corridas/corrida_01/`, `corridas/corrida_02/` y `corridas/corrida_03/` | Se verifican objetivo, ambos prompts, lectura recursiva de archivos, integración con la API, salida estructurada y supervisión humana. Las tres corridas contienen salidas completas y metadatos con modelo y tokens, aportando evidencia de funcionamiento efectivo. |
| Proceso documentado | 23/25 | `DECISIONES.md`, iteraciones 1 a 6, con apartados “Problema detectado” y “Decisión”; `agente/evaluador.py`, fallback `cp1252`, lectura recursiva y modos de calibración y evaluación | Se documentan seis iteraciones con problemas, decisiones y evolución, varias de ellas respaldadas por la implementación actual. Faltan fechas, versiones anteriores y resultados comparativos que permitan reconstruir con mayor profundidad cada transición. |
| Formato y reproducibilidad | 10/15 | `README.md`; `prompts/system_prompt.md`; `prompts/user_prompt.md`; `DECISIONES.md`; `corridas/corrida_01/`, `corridas/corrida_02/` y `corridas/corrida_03/`; `trabajo.md`, sección “Reproducibilidad”; `agente/evaluador.py`, bloque principal | Están presentes la estructura obligatoria y tres corridas con fecha, entrada, salida y metadatos. Sin embargo, cada `entrada.md` solo referencia `casos/excelente` y ese contenido no fue incluido, por lo que no puede reconstruirse la entrada completa. Además, la instrucción `python agente/evaluador.py` activa por defecto calibración, pero no se entregan las carpetas `casos/`, y tampoco se explica de forma suficiente el uso de `--modo evaluacion` y `trabajos_a_evaluar/`. |
| Análisis económico | 14/15 | `ANALISIS_ECONOMICO.md`, secciones “Mediciones reales”, “Proyección de uso”, “Criterio de selección del modelo” y “Trazabilidad”; `corridas/corrida_01/METADATOS.md`, `corrida_02/METADATOS.md` y `corrida_03/METADATOS.md` | El análisis registra tokens de entrada y salida, modelo utilizado, precios de referencia, fórmula, costo individual y promedio, y proyecciones semanal y anual. También considera el principio del modelo más pequeño adecuado. Se descuenta un punto porque no se aporta una fuente verificable para las tarifas ni una calibración comparativa que respalde concretamente la elección frente a modelos menores. |
| Gobierno y riesgo | 15/15 | `GOBIERNO_RIESGO.md`, secciones “Sistemas y recursos utilizados”, “Permisos”, “Riesgos identificados”, “Respuesta ante fallas”, “Supervisión humana”, “Nivel de autonomía” y “Validación final” | Se identifican recursos, permisos, protección de credenciales, riesgos, posibles fallas y respuestas previstas. También se definen los casos de revisión humana, el nivel de autonomía y el docente o responsable académico como validador final. |

## Nota final

**NOTA FINAL: 92/100**

## Fortalezas

- Sistema implementado con lectura recursiva, integración con la API y salidas estructuradas.
- Tres ejecuciones con fecha, salida completa y mediciones de tokens.
- Proceso organizado en iteraciones vinculadas con problemas y decisiones concretas.
- Análisis económico cuantitativo con costos unitarios y proyecciones.
- Gobierno, riesgos y responsabilidad humana definidos de forma completa.

## Aspectos a mejorar

- Las entradas de las corridas no conservan el contenido íntegro de `casos/excelente`.
- No se incluyen las carpetas requeridas por los modos de calibración y evaluación.
- Las instrucciones no detallan los comandos, argumentos y estructura de directorios necesarios.
- El análisis económico no cita la fuente de precios ni presenta una comparación empírica con modelos menores.
- El historial de decisiones no incluye fechas, artefactos de versiones anteriores o resultados comparativos.

## Sugerencia concreta

**UNA SUGERENCIA CONCRETA:** incorporar en cada carpeta de `corridas/` una copia íntegra e inmutable de la entrada evaluada y documentar en el `README.md` el comando exacto, el modo utilizado, la estructura de carpetas requerida y las variables necesarias para reproducir cada ejecución.


# Ejecución 2

Modelo: gpt-5.6-sol
Tokens de entrada: 16894
Tokens de salida: 1699
Tokens totales: 18593

## Identificación

- Trabajo evaluado: Sistema agéntico de evaluación académica
- Fecha de evaluación: 08/09/2026

## Control de fraude

- Estado: SIN INDICIOS DE FRAUDE
- Evidencia detectada: Las referencias a fraude, prompt injection e instrucciones de evaluación aparecen en `DECISIONES.md`, `agente/system_prompt.md`, `prompts/system_prompt.md` y las salidas de `corridas/` como componentes documentados del sistema evaluador.
- Justificación: No se encontraron instrucciones dirigidas a alterar esta evaluación ni a obtener una calificación determinada. El contenido mencionado forma parte de la implementación y prueba del control de fraude.

## Evaluación por dimensiones

| Dimensión | Puntaje | Evidencia citada | Justificación |
|---|---:|---|---|
| Sistema completo y funcionando | 28/30 | `README.md`, secciones “Objetivo”, “Funcionamiento” y “Supervisión”; `prompts/system_prompt.md`; `prompts/user_prompt.md`; `agente/evaluador.py`, funciones `leer_entrega()` y `evaluar_trabajo()` y llamada a `client.responses.create()`; `formato_salida.md`; `corridas/corrida_01/`, `corridas/corrida_02/` y `corridas/corrida_03/` | Se verifican objetivo, ambos prompts, lectura recursiva de archivos, uso de la API de OpenAI, salida estructurada, supervisión humana y tres salidas acompañadas por metadatos de ejecución. Se descuentan puntos porque las entradas guardadas solo identifican `casos/excelente`, cuyo contenido no fue incluido, por lo que no puede comprobarse integralmente la correspondencia entre cada entrada y su salida. |
| Proceso documentado | 23/25 | `DECISIONES.md`, iteraciones 1 a 6, con apartados “Problema detectado” y “Decisión”; `agente/evaluador.py`, fallback de codificación `cp1252`, lectura recursiva y modos de ejecución | Se documentan seis iteraciones con problemas, decisiones, cambios de alcance y evolución técnica, varias de ellas respaldadas por el código actual. Faltan fechas, versiones anteriores y resultados comparativos que permitan reconstruir con mayor profundidad cada modificación. |
| Formato y reproducibilidad | 10/15 | `README.md`; `prompts/system_prompt.md`; `prompts/user_prompt.md`; `DECISIONES.md`; `corridas/corrida_01/`, `corridas/corrida_02/` y `corridas/corrida_03/`; `trabajo.md`, sección “Reproducibilidad”; `agente/evaluador.py`, bloque de ejecución principal | La estructura obligatoria está mayormente presente y existen tres carpetas con entrada, salida, fecha y metadatos. Sin embargo, las entradas no conservan el contenido evaluado y no se incluye `casos/excelente`, por lo que las corridas no pueden reconstruirse. Además, las instrucciones indican `python agente/evaluador.py`, que ejecuta por defecto calibración y requiere carpetas `casos/` no presentes; tampoco se explica el uso de `--modo evaluacion` ni la preparación de `trabajos_a_evaluar/`. |
| Análisis económico | 14/15 | `ANALISIS_ECONOMICO.md`, secciones “Mediciones reales”, “Proyección de uso”, “Criterio de selección del modelo” y “Trazabilidad”; `corridas/corrida_01/METADATOS.md`, `corridas/corrida_02/METADATOS.md` y `corridas/corrida_03/METADATOS.md` | Se informan tokens de entrada y salida para tres corridas, modelo solicitado y utilizado, tarifas de referencia, fórmula, costo unitario, promedio y proyecciones semanal y anual. También se considera explícitamente el principio de usar el modelo más pequeño adecuado. Se descuenta un punto porque no se presenta una calibración comparativa con modelos menores que respalde empíricamente la elección. |
| Gobierno y riesgo | 15/15 | `GOBIERNO_RIESGO.md`, secciones “Sistemas y recursos utilizados”, “Permisos”, “Riesgos identificados”, “Respuesta ante fallas”, “Supervisión humana”, “Nivel de autonomía” y “Validación final” | Se identifican recursos, permisos, protección de credenciales, riesgos previsibles, respuestas ante fallas, casos que requieren revisión humana, nivel de autonomía y responsable de validación final. La estrategia de supervisión es concreta y operativa. |

## Nota final

**NOTA FINAL: 90/100**

## Fortalezas

- Implementación técnica verificable de lectura recursiva, manejo alternativo de codificación e integración con la API.
- Tres salidas estructuradas con fechas y metadatos de modelo y tokens.
- Proceso de construcción organizado en iteraciones, problemas y decisiones.
- Análisis económico numérico y trazable a los metadatos de las corridas.
- Definición completa de permisos, riesgos, fallas, autonomía y validación humana.

## Aspectos a mejorar

- Las corridas no conservan el contenido completo de las entradas y el caso `casos/excelente` no está disponible.
- Las instrucciones de ejecución no explican los modos, comandos y carpetas requeridos por el código.
- El historial no incluye fechas, versiones anteriores ni resultados comparativos de las iteraciones.
- La elección del modelo no está respaldada por una calibración efectiva frente a modelos más pequeños.

## Sugerencia concreta

**UNA SUGERENCIA CONCRETA:** agregar a cada carpeta de `corridas/` una copia íntegra e inmutable del repositorio de entrada y un archivo con el comando exacto utilizado —incluyendo modo, variables y estructura de carpetas— para que un tercero pueda reconstruir las tres ejecuciones sin depender de archivos ausentes.


# Ejecución 3

Modelo: gpt-5.6-sol
Tokens de entrada: 16894
Tokens de salida: 2023
Tokens totales: 18917

## Identificación

- Trabajo evaluado: Sistema agéntico de evaluación académica
- Fecha de evaluación: 08/09/2026

## Control de fraude

- Estado: SIN INDICIOS DE FRAUDE
- Evidencia detectada: No se encontraron instrucciones dirigidas a ignorar la rúbrica, alterar la calificación o manipular esta evaluación. Las referencias a fraude y prompt injection en `DECISIONES.md`, `agente/system_prompt.md` y `prompts/system_prompt.md` corresponden al diseño del mecanismo de control.
- Justificación: Las capacidades principales declaradas están respaldadas por código, prompts, salidas y metadatos. Las limitaciones de reproducibilidad detectadas no constituyen evidencia concreta de fraude.

## Evaluación por dimensiones

| Dimensión | Puntaje | Evidencia citada | Justificación |
|---|---:|---|---|
| Sistema completo y funcionando | 29/30 | `README.md`, secciones “Objetivo” y “Funcionamiento”; `agente/evaluador.py`, funciones `leer_entrega()` y `evaluar_trabajo()`, y llamada `client.responses.create()`; `agente/system_prompt.md`; `prompts/user_prompt.md`; `formato_salida.md`; `GOBIERNO_RIESGO.md`, secciones “Supervisión humana” y “Validación final”; `corridas/corrida_01/`, `corridas/corrida_02/` y `corridas/corrida_03/` | Se verifican objetivo, ambos prompts, lectura recursiva de archivos, uso de la API de OpenAI, salida estructurada, supervisión humana y tres resultados con modelo y tokens registrados. Se descuenta un punto porque las entradas guardadas solo identifican `casos/excelente`, pero no conservan su contenido, lo que limita la verificación integral de cada ejecución de extremo a extremo. |
| Proceso documentado | 23/25 | `DECISIONES.md`, iteraciones 1 a 6; `agente/evaluador.py`, lectura recursiva y fallback de codificación `cp1252`; `agente/system_prompt.md`, sección “Control de fraude” | El proceso presenta seis iteraciones con problemas detectados, decisiones y evolución. Varias decisiones tienen respaldo en la implementación actual. Faltan fechas, versiones anteriores y resultados comparativos que permitan reconstruir con mayor profundidad cada cambio. |
| Formato y reproducibilidad | 10/15 | `README.md`; `prompts/system_prompt.md`; `prompts/user_prompt.md`; `DECISIONES.md`; `corridas/corrida_01/`, `corridas/corrida_02/` y `corridas/corrida_03/`; `trabajo.md`, sección “Reproducibilidad”; `agente/evaluador.py`, bloque principal de ejecución | La estructura obligatoria está mayormente presente y existen tres corridas con fecha, referencia de entrada, salida y metadatos. Sin embargo, no se incluye el contenido de `casos/excelente`, por lo que no pueden reconstruirse exactamente las entradas. Además, las instrucciones indican `python agente/evaluador.py`, que activa calibración por defecto, pero no se entregan las carpetas `casos/`, ni se explica el uso de `--modo evaluacion` y `trabajos_a_evaluar/`. |
| Análisis económico | 14/15 | `ANALISIS_ECONOMICO.md`, secciones “Mediciones reales”, “Proyección de uso”, “Criterio de selección del modelo” y “Trazabilidad”; `corridas/corrida_01/METADATOS.md`, `corridas/corrida_02/METADATOS.md` y `corridas/corrida_03/METADATOS.md`; `agente/evaluador.py`, `model="gpt-5.6"` | Se identifican modelo, tokens de entrada y salida por corrida, precios de referencia, fórmulas, costo unitario promedio y proyecciones semanal y anual. También se considera expresamente el uso del modelo más pequeño adecuado. Se descuenta un punto porque la elección no está respaldada por una calibración comparativa concreta frente a modelos menores y no se cita una fuente verificable para las tarifas. |
| Gobierno y riesgo | 15/15 | `GOBIERNO_RIESGO.md`, secciones “Sistemas y recursos utilizados”, “Permisos”, “Riesgos identificados”, “Respuesta ante fallas”, “Supervisión humana”, “Nivel de autonomía” y “Validación final” | Se documentan recursos, permisos, protección de credenciales, riesgos, fallas posibles, respuestas operativas, situaciones que requieren revisión humana, límites de autonomía y responsable de validar la calificación definitiva. |

## Nota final

**NOTA FINAL: 91/100**

## Fortalezas

- Implementación verificable de lectura recursiva, manejo alternativo de codificación e integración con la API.
- Prompts, rúbrica y formato de salida separados y disponibles.
- Tres corridas con salidas estructuradas, fechas y metadatos de consumo.
- Historial organizado de iteraciones, problemas y decisiones.
- Análisis económico numérico y trazable a los metadatos.
- Gobierno, riesgos y validación humana definidos de forma completa.

## Aspectos a mejorar

- Las entradas de las corridas no conservan el contenido completo del repositorio evaluado.
- No están incluidos los casos de calibración referenciados por las ejecuciones y el código.
- Las instrucciones no detallan los modos de ejecución ni la estructura de carpetas requerida.
- La selección del modelo no incluye una comparación empírica con alternativas de menor costo.
- Las tarifas utilizadas no cuentan con una fuente verificable citada en el repositorio.

## Sugerencia concreta

**UNA SUGERENCIA CONCRETA:** agregar a cada carpeta de `corridas/` una copia íntegra de la entrada evaluada y un archivo con el comando exacto de ejecución, incluyendo el modo utilizado y la estructura de carpetas requerida, para que un tercero pueda reconstruir las tres ejecuciones sin ambigüedades.
