## Identificación

- Trabajo evaluado: Sistema agéntico de evaluación académica
- Fecha de evaluación: 04/09/2026

## Control de fraude

- Estado: SIN INDICIOS DE FRAUDE
- Evidencia detectada: Las referencias a manipulación y prompt injection en `DECISIONES.md`, `agente/system_prompt.md` y `corridas/corrida_03/` están presentadas como mecanismos y casos de prueba del control de fraude. No se encontraron instrucciones destinadas a alterar esta evaluación.
- Justificación: El contenido adversarial se encuentra documentado como parte del diseño y validación del sistema, no como un intento de modificar la aplicación de la rúbrica.

## Evaluación por dimensiones

| Dimensión | Puntaje | Evidencia citada | Justificación |
|---|---:|---|---|
| Sistema completo y funcionando | 28/30 | `README.md`, secciones “Objetivo” y “Funcionamiento”; `agente/evaluador.py`, funciones `leer_entrega()` y `evaluar_trabajo()`; `agente/system_prompt.md`; `prompts/user_prompt.md`; `formato_salida.md`; `GOBIERNO_RIESGO.md`, secciones “Supervisión humana” y “Validación final”; `corridas/corrida_01/METADATOS.md` y `salida.md` | Se verifican un objetivo claro, ambos prompts, integración con la API de OpenAI, lectura recursiva del repositorio, salida estructurada, supervisión humana y una ejecución completa con modelo y tokens registrados. Se descuentan puntos porque solo la corrida 01 conserva una salida completa y existe duplicación no idéntica del system prompt entre `agente/system_prompt.md` —el utilizado por el código— y `prompts/system_prompt.md`. |
| Proceso documentado | 23/25 | `DECISIONES.md`, iteraciones 1 a 6, especialmente “Problema detectado” y “Decisión” de cada iteración; `agente/evaluador.py`, fallback `cp1252`, lectura recursiva y modos de ejecución | El proceso presenta seis iteraciones con problemas, decisiones y evolución técnica claramente organizados. Varias decisiones tienen respaldo en la implementación actual. Faltan fechas, resultados cuantitativos y versiones anteriores o comparaciones que permitan reconstruir con mayor profundidad la evolución. |
| Formato y reproducibilidad | 9/15 | `README.md`; `prompts/system_prompt.md`; `prompts/user_prompt.md`; `DECISIONES.md`; `corridas/corrida_01/`, `corridas/corrida_02/` y `corridas/corrida_03/`; `trabajo.md`, sección “Reproducibilidad”; `agente/evaluador.py`, bloque `if __name__ == "__main__"` | La estructura principal está presente y existen tres carpetas de corridas con entrada, salida y fecha. Sin embargo, las corridas 02 y 03 contienen resúmenes declarativos, no las respuestas estructuradas completas ni metadatos de ejecución. Tampoco están los repositorios de entrada necesarios para reconstruirlas. El comando documentado ejecuta por defecto calibración, pero no se incluyen las carpetas `casos/`; además, no se explica el uso de `--modo evaluacion` ni la preparación de `trabajos_a_evaluar/`. |
| Análisis económico | 7/15 | `ANALISIS_ECONOMICO.md`, secciones “Cálculo por corrida”, “Proyección de uso” y “Criterio de selección del modelo”; `corridas/corrida_01/METADATOS.md`, modelo y tokens medidos; `agente/evaluador.py`, `model="gpt-5.6"` | Existe una medición verificable de tokens para una corrida, identificación del modelo, fórmulas de costo y consideración del principio de usar el modelo más pequeño. No se informan precios, costo monetario por corrida, frecuencia de uso ni proyecciones semanales y anuales calculadas. La elección de `gpt-5.6` tampoco se justifica mediante una comparación concreta con modelos menores. |
| Gobierno y riesgo | 15/15 | `GOBIERNO_RIESGO.md`, secciones “Sistemas y recursos utilizados”, “Permisos”, “Riesgos identificados”, “Respuesta ante fallas”, “Supervisión humana”, “Nivel de autonomía” y “Validación final” | Se identifican recursos y datos utilizados, permisos, protección de credenciales, riesgos previsibles, respuestas ante fallas, límites de autonomía, situaciones que requieren revisión humana y el docente o responsable académico como validador final. La estrategia de supervisión es concreta y completa. |

## Nota final

**NOTA FINAL: 82/100**

## Fortalezas

- Implementación verificable de lectura recursiva, manejo de codificaciones e integración con la API.
- Corrida 01 completa, con salida estructurada, fecha, modelo y consumo de tokens.
- Historial de construcción organizado en iteraciones, problemas y decisiones.
- Definición completa de permisos, riesgos, fallas, autonomía y validación humana.
- Separación explícita entre rúbrica, formato de salida, prompts e implementación.

## Aspectos a mejorar

- Las corridas 02 y 03 no conservan las salidas reales completas ni sus metadatos de consumo.
- No se incluyen los casos de prueba utilizados, por lo que las ejecuciones no pueden reconstruirse.
- Las instrucciones no explican correctamente los modos de ejecución ni las carpetas requeridas por el código.
- El análisis económico carece de costos y proyecciones numéricas.
- Existen dos versiones diferentes del system prompt, pero no se documenta claramente que el programa utiliza `agente/system_prompt.md`.

## Sugerencia concreta

**UNA SUGERENCIA CONCRETA:** completar cada carpeta de `corridas/` con el repositorio de entrada o una copia íntegra de su contenido, la respuesta real completa, los metadatos de tokens, el costo monetario calculado y el comando exacto utilizado, incluyendo el modo y la estructura de carpetas requerida.