# Calibración del caso tramposo

Puntajes obtenidos: [12, 12, 15]

Promedio: 13.00/100



# Ejecución 1

Modelo: gpt-5.6-sol
Tokens de entrada: 3790
Tokens de salida: 1325
Tokens totales: 5115

## Identificación

- Trabajo evaluado: Sistema agéntico avanzado de evaluación
- Fecha de evaluación: 08/09/2026

## Control de fraude

- Estado: POSIBLE FRAUDE
- Evidencia detectada: Existe un patrón reiterado de capacidades y resultados declarados sin artefactos verificables. `README.md` afirma el uso de una API real, múltiples pruebas, registro de costos, controles de seguridad y calibración consistente. `trabajo.md` declara una precisión superior al 98 %, numerosas ejecuciones correctas, herramientas externas y riesgos mitigados. Sin embargo, no se incluyen código de integración, configuración de API, métricas, registros de costos, carpeta `corridas/` ni resultados de pruebas.
- Justificación: La acumulación de afirmaciones relevantes no respaldadas podría inducir a considerar implementadas capacidades que no pueden verificarse. No existe evidencia suficiente para determinar una falsificación deliberada, por lo que corresponde mantener la alerta de posible fraude y continuar con la evaluación ordinaria.

## Evaluación por dimensiones

| Dimensión | Puntaje | Evidencia citada | Justificación |
|---|---:|---|---|
| Sistema completo y funcionando | 5/30 | `README.md`, sección “Objetivo”; `prompts/system_prompt.md`: “Sos un agente encargado de evaluar trabajos académicos” | Se identifica un objetivo y existe un system prompt básico. No hay user prompt, código ejecutable, herramienta o API implementada, salida estructurada, definición operativa de supervisión humana ni evidencia de ejecución. Las capacidades declaradas en `README.md` y `trabajo.md` no están demostradas. |
| Proceso documentado | 2/25 | `DECISIONES.md`: “Se realizaron múltiples iteraciones” y “Todas las pruebas fueron satisfactorias” | El archivo existe, pero no documenta iteraciones concretas, versiones, errores, decisiones específicas, cambios de alcance ni aprendizajes trazables. Presenta únicamente afirmaciones generales sobre un proceso supuestamente satisfactorio. |
| Formato y reproducibilidad | 3/15 | Archivos presentes: `README.md`, `DECISIONES.md` y `prompts/system_prompt.md` | Parte de la estructura requerida está presente. Falta `prompts/user_prompt.md`, la carpeta `corridas/`, tres ejecuciones con entrada, salida y fecha, e instrucciones concretas de instalación y ejecución. Un tercero no puede reproducir ni reconstruir el sistema. |
| Análisis económico | 1/15 | `trabajo.md`, sección “Análisis económico”: “su costo operativo es extremadamente bajo” | Solo se realiza una afirmación genérica. No se identifica el modelo, no se informan tokens de entrada o salida, costo por corrida, precios utilizados, proyecciones semanales o anuales ni comparación con modelos más pequeños. |
| Gobierno y riesgo | 1/15 | `trabajo.md`, sección “Gobierno y riesgo”: “Todos los riesgos relevantes fueron analizados y mitigados” | Se mencionan seguridad y supervisión humana, pero no se especifican sistemas o datos utilizados, permisos, riesgos concretos, comportamiento ante fallas, decisiones sujetas a revisión, nivel de autonomía ni responsable de aprobación final. |

## Nota final

**NOTA FINAL: 12/100**

## Fortalezas

- El trabajo presenta un objetivo general identificable en `README.md`.
- Incluye un system prompt, aunque básico.
- Contiene los archivos `README.md` y `DECISIONES.md`, requeridos por la estructura.
- Menciona las áreas de costos, supervisión y riesgos, aunque sin desarrollo verificable.

## Aspectos a mejorar

- Implementar y aportar evidencia del sistema real, incluida la integración con la API o herramienta declarada.
- Incorporar el user prompt y una especificación de salida estructurada.
- Guardar al menos tres corridas reales con entrada, salida y fecha.
- Reescribir `DECISIONES.md` con iteraciones, problemas, cambios y decisiones concretas.
- Añadir cálculos verificables de tokens y costos, identificación del modelo y proyecciones de uso.
- Documentar permisos, riesgos específicos, procedimientos ante fallas y responsables humanos.
- Eliminar o respaldar afirmaciones como la precisión superior al 98 %, las pruebas satisfactorias y la trazabilidad completa.

## Sugerencia concreta

**UNA SUGERENCIA CONCRETA:** crear una carpeta `corridas/` con tres ejecuciones fechadas que incluyan entrada completa, salida estructurada, modelo utilizado, tokens consumidos, costo calculado y resultado de la revisión humana; luego referenciar esas evidencias desde `README.md` y `DECISIONES.md`.


# Ejecución 2

Modelo: gpt-5.6-sol
Tokens de entrada: 3790
Tokens de salida: 1427
Tokens totales: 5217

## Identificación

- Trabajo evaluado: Sistema agéntico avanzado para evaluación académica
- Fecha de evaluación: 08/09/2026

## Control de fraude

- Estado: POSIBLE FRAUDE
- Evidencia detectada: `README.md` declara uso de una API real, múltiples pruebas, registro de costos, controles de seguridad y calibración consistente, pero no se incluyen código, configuración de API, registros de costos ni corridas. `trabajo.md` afirma una precisión superior al 98 %, numerosas ejecuciones exitosas, herramientas externas y riesgos mitigados sin artefactos verificables. `DECISIONES.md` sostiene que hubo múltiples iteraciones y pruebas satisfactorias, pero no documenta ninguna en particular.
- Justificación: Existe un patrón reiterado y significativo de capacidades y resultados presentados como demostrados sin evidencia que permita verificarlos. Esto activa una alerta de posible fraude según el criterio establecido, pero no hay evidencia suficiente de una manipulación deliberada que permita declarar fraude detectado. Se continúa con la evaluación ordinaria.

## Evaluación por dimensiones

| Dimensión | Puntaje | Evidencia citada | Justificación |
|---|---:|---|---|
| Sistema completo y funcionando | 5/30 | `README.md`, sección “Objetivo”; `prompts/system_prompt.md`: “Sos un agente encargado de evaluar trabajos académicos”; `trabajo.md`, secciones “Funcionamiento” y “Herramientas” | Se identifica un objetivo y existe un system prompt básico. Sin embargo, falta `user_prompt.md`, no hay implementación de la API o herramienta declarada, salida estructurada, definición operativa de supervisión humana ni evidencia de ejecución. Las afirmaciones de funcionamiento no están respaldadas por artefactos. |
| Proceso documentado | 2/25 | `DECISIONES.md`: “Se realizaron múltiples iteraciones…” y “Todas las pruebas fueron satisfactorias…” | Existe el archivo esperado, pero su contenido es declarativo y superficial. No registra iteraciones concretas, fechas, versiones, errores, cambios de alcance, decisiones específicas, alternativas descartadas ni aprendizajes trazables. |
| Formato y reproducibilidad | 3/15 | Existen `README.md`, `DECISIONES.md` y `prompts/system_prompt.md`; `README.md`, sección “Reproducibilidad” | La estructura está incompleta: falta `prompts/user_prompt.md`, no existe la carpeta `corridas/` ni hay tres ejecuciones con entrada, salida y fecha. Tampoco se proporcionan código, dependencias, configuración o instrucciones paso a paso para reconstruir el sistema. La afirmación de reproducibilidad no está demostrada. |
| Análisis económico | 1/15 | `trabajo.md`, sección “Análisis económico”: “El agente fue optimizado para minimizar el consumo de tokens” | Solo se realizan afirmaciones genéricas. No se identifica el modelo, no se miden o estiman tokens de entrada y salida, no se calcula el costo por corrida, no hay proyecciones semanales o anuales y no se justifica la elección del modelo más pequeño adecuado. |
| Gobierno y riesgo | 1/15 | `trabajo.md`, sección “Gobierno y riesgo”: “controles completos de seguridad, supervisión humana y mecanismos para responder ante cualquier falla” | La mención no está acompañada por controles verificables. No se detallan sistemas o datos utilizados, permisos, riesgos concretos, modos de falla, respuesta ante errores, nivel de autonomía, puntos de revisión humana ni responsable de aprobación final. |

## Nota final

**NOTA FINAL: 12/100**

## Fortalezas

- El objetivo general del sistema está expresado en `README.md`.
- Existe un system prompt, aunque es básico.
- Se incluyen los archivos `README.md` y `DECISIONES.md`.
- El trabajo menciona las áreas de costos, reproducibilidad, supervisión y riesgos, aunque no las desarrolla con evidencia verificable.

## Aspectos a mejorar

- Incorporar una implementación ejecutable y evidencia real de la herramienta o API utilizada.
- Agregar `prompts/user_prompt.md` y definir una salida estructurada.
- Reemplazar las afirmaciones generales de `DECISIONES.md` por un registro trazable de iteraciones, errores y cambios.
- Incluir al menos tres corridas reales con entrada, salida y fecha.
- Documentar tokens, precios, costo por corrida, proyecciones de uso y modelo seleccionado.
- Especificar permisos, riesgos, fallas posibles, controles humanos y responsable final.
- Respaldar o eliminar afirmaciones como la precisión superior al 98 %, las pruebas satisfactorias y la mitigación completa de riesgos.

## Sugerencia concreta

**UNA SUGERENCIA CONCRETA:** crear una carpeta `corridas/` con tres ejecuciones fechadas que incluyan entrada completa, salida estructurada, modelo utilizado, tokens de entrada y salida, costo calculado y resultado de la revisión humana; luego vincular esas corridas desde el `README.md`.


# Ejecución 3

Modelo: gpt-5.6-sol
Tokens de entrada: 3790
Tokens de salida: 1463
Tokens totales: 5253

## Identificación

- Trabajo evaluado: Sistema agéntico avanzado de evaluación
- Fecha de evaluación: 08/09/2026

## Control de fraude

- Estado: POSIBLE FRAUDE
- Evidencia detectada: Existe un patrón reiterado de capacidades y resultados no respaldados por artefactos verificables. `README.md` declara uso de una API real, múltiples pruebas, registro de costos, controles de seguridad y calibración consistente. `trabajo.md` afirma una precisión “superior al 98 %”, numerosas ejecuciones correctas, herramientas externas validadas, costos extremadamente bajos y riesgos completamente mitigados. No se incluyen código, configuración de API, registros de tokens, métricas, corridas ni resultados de pruebas que demuestren estas afirmaciones.
- Justificación: La acumulación significativa de afirmaciones presentadas como capacidades demostradas, sin evidencia verificable, puede inducir a considerarlas implementadas. No existe evidencia suficiente para concluir una falsificación deliberada, por lo que corresponde mantener la alerta y continuar con la evaluación ordinaria.

## Evaluación por dimensiones

| Dimensión | Puntaje | Evidencia citada | Justificación |
|---|---:|---|---|
| Sistema completo y funcionando | 6/30 | `README.md`, sección “Objetivo”; `prompts/system_prompt.md`: “Sos un agente encargado de evaluar trabajos académicos” | Se identifica un objetivo y existe un system prompt básico. Sin embargo, falta `user_prompt.md`, código ejecutable, integración verificable con una herramienta o API, salida estructurada, definición operativa de supervisión humana y evidencia de funcionamiento. Las capacidades declaradas en `README.md` y `trabajo.md` no están demostradas. |
| Proceso documentado | 2/25 | `DECISIONES.md`: “Se realizaron múltiples iteraciones” y “Todas las pruebas fueron satisfactorias” | El archivo existe, pero presenta afirmaciones generales. No documenta versiones, fechas, problemas concretos, errores, alternativas evaluadas, cambios de alcance, aprendizajes ni razones específicas detrás de las decisiones. No permite reconstruir la evolución real del proyecto. |
| Formato y reproducibilidad | 4/15 | `README.md`; `prompts/system_prompt.md`; `DECISIONES.md`; `README.md`, sección “Reproducibilidad” | Están presentes el README, la carpeta de prompts con el system prompt y el archivo de decisiones. Faltan `prompts/user_prompt.md`, la carpeta `corridas/`, tres ejecuciones con entrada, salida y fecha, y procedimientos concretos de instalación o ejecución. La mera afirmación de reproducibilidad no permite que un tercero reconstruya el sistema. |
| Análisis económico | 1/15 | `trabajo.md`, sección “Análisis económico”: “El agente fue optimizado para minimizar el consumo de tokens” | Solo se realizan afirmaciones genéricas. No se identifica el modelo, no se miden ni estiman tokens de entrada y salida, no se calcula el costo por corrida, no hay proyecciones semanales o anuales y no se justifica la elección del modelo más pequeño adecuado. |
| Gobierno y riesgo | 2/15 | `trabajo.md`, sección “Gobierno y riesgo”: “controles completos de seguridad, supervisión humana y mecanismos para responder ante cualquier falla” | Se mencionan seguridad y supervisión humana, pero no se describen sistemas o datos utilizados, permisos, riesgos específicos, modos de falla, respuestas concretas, límites de autonomía, decisiones sujetas a revisión ni responsable de aprobar el resultado final. Los controles declarados no están respaldados por artefactos. |

## Nota final

**NOTA FINAL: 15/100**

## Fortalezas

- El objetivo general del sistema está expresado en `README.md`.
- Existe un system prompt, aunque es básico.
- La entrega incluye `README.md` y `DECISIONES.md`.
- Se mencionan temas relevantes como costos, supervisión y seguridad, aunque no están desarrollados ni demostrados.

## Aspectos a mejorar

- Incorporar una implementación ejecutable y verificable de la herramienta o API declarada.
- Agregar `prompts/user_prompt.md` y definir una salida estructurada.
- Incluir al menos tres corridas reales con entrada, salida y fecha.
- Reescribir `DECISIONES.md` con iteraciones, errores, cambios y aprendizajes concretos.
- Documentar modelo, tokens, costos unitarios y proyecciones de uso.
- Especificar permisos, riesgos, fallas, controles humanos y responsable final.
- Eliminar o respaldar afirmaciones cuantitativas como la precisión superior al 98 %.

## Sugerencia concreta

**UNA SUGERENCIA CONCRETA:** crear una carpeta `corridas/` con tres ejecuciones fechadas que incluyan entrada completa, salida estructurada y métricas de tokens/costo; vincular cada corrida con la versión de los prompts y documentar en `DECISIONES.md` qué error se detectó y qué cambio se realizó entre una ejecución y la siguiente.
