## Identificación

- Trabajo evaluado: Sistema agéntico de evaluación académica
- Fecha de evaluación: 04/09/2026

## Control de fraude

- Estado: SIN INDICIOS DE FRAUDE
- Evidencia detectada: Las referencias a instrucciones para ignorar la rúbrica aparecen en `DECISIONES.md`, `agente/system_prompt.md` y `corridas/corrida_03/` como parte de un control y una prueba adversarial documentada.
- Justificación: No se encontraron instrucciones dirigidas a manipular esta evaluación. El contenido adversarial está presentado explícitamente como caso de prueba del sistema.

## Evaluación por dimensiones

| Dimensión | Puntaje | Evidencia citada | Justificación |
|---|---:|---|---|
| Sistema completo y funcionando | 28/30 | `README.md`, secciones “Objetivo” y “Funcionamiento”; `agente/evaluador.py`, funciones `leer_entrega()` y `evaluar_trabajo()` y llamada a `client.responses.create()`; `agente/system_prompt.md`; `prompts/user_prompt.md`; `formato_salida.md`; `GOBIERNO_RIESGO.md`, secciones “Supervisión humana” y “Validación final”; `corridas/corrida_01/` y `corridas/corrida_02/` | Se verifican objetivo, system prompt, user prompt, lectura recursiva de archivos, integración real con la API, salida estructurada, supervisión humana y dos ejecuciones con modelo y tokens registrados. Se descuentan puntos porque las entradas no conservan el contenido completo del caso evaluado y la corrida 03 solo presenta resúmenes, lo que limita la verificación integral del funcionamiento. Además, existen dos versiones no idénticas del system prompt, aunque el código utiliza `agente/system_prompt.md`. |
| Proceso documentado | 23/25 | `DECISIONES.md`, iteraciones 1 a 6, con apartados “Problema detectado” y “Decisión”; `agente/evaluador.py`, implementación de lectura recursiva, fallback `cp1252` y control por modos | El proceso contiene seis iteraciones claramente organizadas, con problemas, decisiones, cambios de alcance y evolución técnica. Varias decisiones están respaldadas por la implementación actual. Faltan fechas, versiones anteriores y resultados comparativos que permitan reconstruir con mayor profundidad cada iteración. |
| Formato y reproducibilidad | 9/15 | `README.md`; `prompts/system_prompt.md`; `prompts/user_prompt.md`; `DECISIONES.md`; `corridas/corrida_01/`, `corridas/corrida_02/` y `corridas/corrida_03/`; `trabajo.md`, sección “Reproducibilidad”; `agente/evaluador.py`, bloque de ejecución principal | La estructura obligatoria principal está presente. Las corridas 01 y 02 incluyen fecha, referencia de entrada, salida completa y metadatos. Sin embargo, no se incluyen los repositorios `casos/excelente` usados como entrada, y la corrida 03 no conserva la instrucción adversarial concreta, una salida real completa ni metadatos de tokens. Asimismo, el comando documentado ejecuta por defecto calibración, pero no se entregan las carpetas `casos/`; tampoco se explica suficientemente el uso de `--modo evaluacion` y `trabajos_a_evaluar/`. Por ello, las tres ejecuciones no pueden reconstruirse sin ambigüedades. |
| Análisis económico | 7/15 | `ANALISIS_ECONOMICO.md`, secciones “Cálculo por corrida”, “Proyección de uso” y “Criterio de selección del modelo”; `corridas/corrida_01/METADATOS.md` y `corridas/corrida_02/METADATOS.md`; `agente/evaluador.py`, `model="gpt-5.6"` | Se registran tokens de entrada y salida en dos corridas, se identifica el modelo y se documentan fórmulas de costo y el principio de usar el modelo más pequeño adecuado. No se consignan precios, costo monetario por corrida, frecuencia estimada, proyecciones semanales o anuales calculadas ni una comparación concreta que justifique la elección de `gpt-5.6` frente a modelos menores. |
| Gobierno y riesgo | 15/15 | `GOBIERNO_RIESGO.md`, secciones “Sistemas y recursos utilizados”, “Permisos”, “Riesgos identificados”, “Respuesta ante fallas”, “Supervisión humana”, “Nivel de autonomía” y “Validación final” | Se identifican los recursos y datos utilizados, permisos necesarios, protección de credenciales, riesgos previsibles, respuestas ante fallas, situaciones que requieren revisión humana, límites de autonomía y responsable de la validación final. La estrategia de supervisión es concreta y completa. |

## Nota final

**NOTA FINAL: 82/100**

## Fortalezas

- Implementación verificable de lectura recursiva, manejo alternativo de codificación e integración con la API.
- Prompts, rúbrica y formato de salida separados y disponibles.
- Dos corridas con salidas completas y mediciones de tokens.
- Historial de construcción organizado en iteraciones, problemas y decisiones.
- Definición completa de permisos, riesgos, fallas, autonomía y validación humana.

## Aspectos a mejorar

- La corrida 03 no conserva la entrada adversarial literal ni la respuesta real completa.
- No se incluyen los casos usados como entrada, lo que impide reconstruir las ejecuciones.
- Las instrucciones no explican con precisión los modos de ejecución y las carpetas requeridas por el código.
- El análisis económico carece de costos monetarios y proyecciones numéricas.
- Existen dos versiones diferentes del system prompt sin una explicación clara sobre su sincronización.

## Sugerencia concreta

**UNA SUGERENCIA CONCRETA:** completar cada carpeta de `corridas/` con una copia íntegra de la entrada, la respuesta real completa, el comando exacto de ejecución, el modelo y tokens consumidos, y el cálculo monetario por corrida con su proyección semanal y anual.