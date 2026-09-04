## Identificación

- Trabajo evaluado: Sistema agéntico de evaluación académica
- Fecha de evaluación: 04/09/2026

## Control de fraude

- Estado: SIN INDICIOS DE FRAUDE
- Evidencia detectada: No se encontraron instrucciones destinadas a modificar la calificación ni a ignorar la rúbrica. Las referencias a prompt injection en `DECISIONES.md`, `agente/system_prompt.md` y `corridas/corrida_03/` forman parte del diseño y prueba del control de fraude.
- Justificación: El material adversarial está documentado como caso de prueba del sistema y no constituye un intento de manipular esta evaluación.

## Evaluación por dimensiones

| Dimensión | Puntaje | Evidencia citada | Justificación |
|---|---:|---|---|
| Sistema completo y funcionando | 23/30 | `README.md`, secciones “Objetivo” y “Funcionamiento”; `prompts/system_prompt.md`; `prompts/user_prompt.md`; `agente/evaluador.py`, funciones `leer_entrega()` y `evaluar_trabajo()`; `formato_salida.md`; `GOBIERNO_RIESGO.md`, secciones “Supervisión humana” y “Validación final” | Existen objetivo, prompts, integración programada con la API de OpenAI, lectura recursiva de archivos, salida estructurada y supervisión humana. Sin embargo, las salidas de `corridas/` son resúmenes declarativos y no respuestas completas de la API con puntajes y evidencias. Además, `prompts/user_prompt.md` no es cargado explícitamente por `evaluador.py`. Por ello, el funcionamiento efectivo cuenta con evidencia incompleta. |
| Proceso documentado | 23/25 | `DECISIONES.md`, iteraciones 1 a 6: salida general, verificación de evidencia, lectura recursiva, compatibilidad `cp1252`, control de fraude y alineación con la rúbrica | El historial presenta seis iteraciones con problemas, decisiones y evolución técnica. Varias decisiones están respaldadas por el código y los prompts actuales. Faltan fechas, resultados comparativos y artefactos de versiones anteriores que permitan reconstruir con mayor profundidad cada cambio. |
| Formato y reproducibilidad | 10/15 | `README.md`; `prompts/system_prompt.md`; `prompts/user_prompt.md`; `DECISIONES.md`; `corridas/corrida_01/`, `corridas/corrida_02/` y `corridas/corrida_03/`; `trabajo.md`, sección “Reproducibilidad” | La estructura principal y tres pares de entrada/salida con fecha están presentes. No obstante, las salidas no contienen las evaluaciones estructuradas reales que afirman haber generado, sino descripciones resumidas. Asimismo, el comando indicado ejecuta por defecto el modo calibración, pero no se proporcionan las carpetas `casos/`; tampoco se documenta el uso de `--modo evaluacion` ni se incluye `trabajos_a_evaluar/`. Esto impide reproducir sin ambigüedades las corridas. |
| Análisis económico | 5/15 | `ANALISIS_ECONOMICO.md`, secciones “Cálculo por corrida”, “Proyección de uso” y “Criterio de selección del modelo”; `agente/evaluador.py`, llamada con `model="gpt-5.6"` | Se documentan fórmulas de cálculo, componentes del costo, proyecciones y el principio de seleccionar el modelo más pequeño. Sin embargo, no hay mediciones o estimaciones concretas de tokens, precios, costo por corrida, frecuencia semanal ni costo anual. El documento tampoco identifica concretamente el modelo implementado ni justifica comparativamente su elección. |
| Gobierno y riesgo | 15/15 | `GOBIERNO_RIESGO.md`, secciones “Sistemas y recursos utilizados”, “Permisos”, “Riesgos identificados”, “Respuesta ante fallas”, “Supervisión humana”, “Nivel de autonomía” y “Validación final” | Se identifican recursos, permisos, credenciales, riesgos previsibles, respuestas ante fallas, situaciones que requieren revisión humana, nivel de autonomía y responsable de validación final. La estrategia de supervisión es concreta y coherente con el funcionamiento propuesto. |

## Nota final

**NOTA FINAL: 76/100**

## Fortalezas

- Implementación técnica verificable de lectura recursiva de repositorios e integración con la API.
- Prompts, rúbrica y formato de salida disponibles como archivos separados.
- Historial de iteraciones organizado por problema y decisión.
- Gobierno y supervisión humana definidos de manera completa.
- Manejo explícito de codificaciones y protección de la clave mediante variable de entorno.

## Aspectos a mejorar

- Las tres corridas no conservan las respuestas reales completas ni evidencian puntajes, citas y nota final.
- Las instrucciones de ejecución no coinciden completamente con la estructura entregada: faltan `casos/` y `trabajos_a_evaluar/`.
- El análisis económico define un procedimiento, pero no presenta ninguna medición o proyección numérica.
- El `user_prompt.md` documentado no se carga desde el programa.
- No se presentan resultados concretos de la calibración mencionada en `trabajo.md`.

## Sugerencia concreta

**UNA SUGERENCIA CONCRETA:** reemplazar las salidas resumidas de `corridas/` por tres respuestas reales completas de la API y agregar, para cada corrida, el modelo, los tokens de entrada y salida, el costo calculado y el comando exacto utilizado para reproducirla.