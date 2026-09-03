# Calibración del caso intermedio

Puntajes obtenidos: [71, 73, 71]

Promedio: 71.67/100



# Ejecución 1

## Identificación
- Trabajo evaluado: Trabajo práctico — Diseño de un agente evaluador con inteligencia artificial
- Fecha de evaluación: 03/09/2026

## Resultado
- Puntaje total: 71/100
- Nivel alcanzado: Intermedio

## Evaluación por criterios

### Criterio 1
- Criterio: Cumplimiento de la consigna
- Puntaje obtenido: 18
- Puntaje máximo: 25
- Evidencia encontrada: El trabajo describe el objetivo del agente, sus entradas principales, el procedimiento de evaluación, el uso de una rúbrica, la integración mediante API, las pruebas, el formato de salida y las limitaciones. También contempla la asignación de puntajes y la generación de devoluciones.
- Justificación: Cumple con la mayor parte de los componentes esperables para el diseño de un agente evaluador. Sin embargo, la entrega se concentra en una descripción general y no presenta el programa mencionado, ejemplos completos de evaluaciones producidas ni resultados concretos de las pruebas. Por ello, el cumplimiento es mayoritario, pero no completo.

### Criterio 2
- Criterio: Calidad y profundidad del contenido
- Puntaje obtenido: 18
- Puntaje máximo: 25
- Evidencia encontrada: Se explican el propósito del agente, su funcionamiento general, el papel de la rúbrica, la integración con la API, las pruebas y limitaciones como la variabilidad entre ejecuciones y la dependencia de la claridad de la evidencia.
- Justificación: El contenido es pertinente y demuestra una comprensión adecuada del problema. Se reconocen aspectos relevantes, como la subjetividad, la trazabilidad y la reproducibilidad. No obstante, varios apartados son generales: no se desarrollan mecanismos para seleccionar niveles de la rúbrica, resolver ambigüedades, validar el cálculo final o controlar la consistencia de las respuestas.

### Criterio 3
- Criterio: Fundamentación y evidencia
- Puntaje obtenido: 13
- Puntaje máximo: 20
- Evidencia encontrada: El trabajo fundamenta el uso de la rúbrica como medio para establecer criterios comunes y reducir parte de la subjetividad. También justifica el uso de la variable de entorno `OPENAI_API_KEY` para evitar exponer la clave y reconoce que las pruebas sirven para comparar casos de diferente calidad. A la vez, declara que “no se exige una identificación exhaustiva de evidencia para cada decisión”.
- Justificación: Existe fundamentación para varias decisiones, pero la evidencia es limitada. No se incluyen código, registros de ejecución, salidas de prueba, comparaciones de resultados ni mediciones de estabilidad. Además, la decisión de no exigir evidencia exhaustiva debilita la trazabilidad requerida para justificar cada puntaje.

### Criterio 4
- Criterio: Estructura, claridad y coherencia
- Puntaje obtenido: 14
- Puntaje máximo: 15
- Evidencia encontrada: El documento se organiza en diez secciones numeradas, utiliza títulos descriptivos, listas y una secuencia lógica que va desde la introducción y los objetivos hasta las limitaciones y la conclusión.
- Justificación: La presentación es clara, ordenada y fácil de seguir. Existe coherencia entre los objetivos, el funcionamiento descrito y las limitaciones reconocidas. Como aspecto menor, hay cierta repetición entre las secciones “Objetivo” y “Funcionamiento general”, y algunos apartados podrían vincularse de forma más directa con requisitos verificables.

### Criterio 5
- Criterio: Uso adecuado de herramientas, metodología y documentación
- Puntaje obtenido: 8
- Puntaje máximo: 15
- Evidencia encontrada: Se menciona un programa desarrollado en Python, el uso de la API de OpenAI, la variable de entorno `OPENAI_API_KEY` y la preparación de trabajos de prueba. La documentación describe el flujo general del sistema.
- Justificación: El uso de herramientas y metodología está documentado solo parcialmente. No se presenta el código fuente, la estructura del programa, las dependencias, las versiones utilizadas, instrucciones de instalación y ejecución, ejemplos de solicitudes a la API ni resultados de las pruebas. La documentación permite comprender la idea general, pero no verificar ni reproducir completamente el sistema.

## Fortalezas
- Presenta una estructura clara y una secuencia lógica.
- Define adecuadamente el propósito general del agente evaluador.
- Reconoce la importancia de utilizar una rúbrica para aplicar criterios comunes.
- Incluye una práctica apropiada de seguridad al utilizar `OPENAI_API_KEY` como variable de entorno.
- Identifica limitaciones relevantes, como la variabilidad entre ejecuciones, la ambigüedad de la evidencia y la necesidad de revisión.
- Contempla elementos importantes de la devolución, como puntaje, fortalezas, aspectos a mejorar y recomendaciones.

## Aspectos a mejorar
- Falta evidencia concreta de la implementación técnica mencionada.
- No se incluyen resultados ni registros de los casos de prueba.
- La metodología para asignar puntajes no está suficientemente detallada.
- No se define un procedimiento para medir la estabilidad y consistencia entre ejecuciones.
- La documentación no permite instalar, ejecutar y reproducir el sistema.
- La identificación de evidencia para justificar cada decisión se plantea como no exhaustiva, lo que reduce la trazabilidad de la evaluación.
- No se explican mecanismos para verificar cálculos, límites de puntaje y formato final.

## Recomendaciones
- Incorporar el código fuente del programa y explicar sus módulos o funciones principales.
- Agregar instrucciones de instalación y ejecución, incluyendo versión de Python, dependencias y configuración de la variable de entorno.
- Definir un procedimiento explícito para evaluar cada criterio, localizar evidencia, asignar puntajes y calcular el total.
- Exigir que cada puntaje esté acompañado por evidencia concreta del trabajo evaluado.
- Presentar casos de prueba completos con entrada, salida esperada, salida obtenida y análisis de diferencias.
- Ejecutar cada caso varias veces y registrar la variación de los puntajes para medir estabilidad.
- Implementar validaciones automáticas que controlen los puntajes máximos, la suma total y el nivel de desempeño.
- Incluir un ejemplo completo de devolución generado por el sistema siguiendo el formato requerido.

## Conclusión
El trabajo presenta un diseño comprensible y pertinente de un agente evaluador, con una organización sólida y una identificación adecuada de sus componentes y limitaciones. Sin embargo, la ausencia de implementación verificable, resultados de pruebas y documentación reproducible limita su profundidad, fundamentación y calidad metodológica. En consecuencia, alcanza un nivel **Intermedio**.


# Ejecución 2

## Identificación
- Trabajo evaluado: Trabajo práctico — Diseño de un agente evaluador con inteligencia artificial
- Fecha de evaluación: 03/09/2026

## Resultado
- Puntaje total: 73/100
- Nivel alcanzado: Intermedio

## Evaluación por criterios

### Criterio 1
- Criterio: Cumplimiento de la consigna
- Puntaje obtenido: 19
- Puntaje máximo: 25
- Evidencia encontrada: El trabajo describe el objetivo del agente, sus entradas, el procedimiento de evaluación, el uso de la rúbrica, la integración mediante API, las pruebas, el formato de salida y las limitaciones. No se incluye el código fuente, una ejecución completa ni ejemplos concretos de evaluaciones generadas.
- Justificación: Cumple con la mayor parte del objetivo planteado y aborda los componentes principales de un agente evaluador. Sin embargo, la entrega se concentra en una descripción conceptual y no demuestra completamente la implementación y el funcionamiento efectivo del sistema. Al no haberse proporcionado una consigna independiente y detallada, el cumplimiento se valoró tomando como referencia los objetivos y requisitos declarados en la propia entrega.

### Criterio 2
- Criterio: Calidad y profundidad del contenido
- Puntaje obtenido: 18
- Puntaje máximo: 25
- Evidencia encontrada: Se explican el propósito del agente, su funcionamiento general, el papel de la rúbrica, la integración con la API y algunas limitaciones, como la variación entre ejecuciones y la dependencia de la claridad de la evidencia.
- Justificación: El contenido es pertinente y demuestra una comprensión adecuada del problema. No obstante, varios apartados son generales. Faltan detalles sobre el diseño del prompt, el tratamiento de errores, la validación de puntajes, la consistencia entre ejecuciones y la forma exacta en que se procesan los archivos.

### Criterio 3
- Criterio: Fundamentación y evidencia
- Puntaje obtenido: 13
- Puntaje máximo: 20
- Evidencia encontrada: El trabajo justifica el uso de la rúbrica como medio para reducir la subjetividad, explica el uso de `OPENAI_API_KEY` para evitar exponer credenciales y reconoce limitaciones vinculadas con la estabilidad y la ambigüedad. También señala que se prepararon diferentes trabajos de prueba.
- Justificación: Existe fundamentación para varias decisiones generales, pero la evidencia es incompleta. No se presentan resultados de pruebas, comparaciones de puntajes, registros de ejecución, ejemplos de respuestas ni métricas de estabilidad. La afirmación de que el sistema constituye una “solución funcional” no está acompañada por evidencia técnica verificable.

### Criterio 4
- Criterio: Estructura, claridad y coherencia
- Puntaje obtenido: 14
- Puntaje máximo: 15
- Evidencia encontrada: El documento está organizado en diez secciones numeradas, con títulos claros y una secuencia que va desde la introducción y los objetivos hasta la implementación, las pruebas, las limitaciones y la conclusión.
- Justificación: La presentación es ordenada, coherente y fácil de seguir. El lenguaje es claro y los apartados mantienen relación con el objetivo general. Como aspecto menor, existe cierta repetición entre las secciones de objetivo, funcionamiento general y conclusión.

### Criterio 5
- Criterio: Uso adecuado de herramientas, metodología y documentación
- Puntaje obtenido: 9
- Puntaje máximo: 15
- Evidencia encontrada: Se menciona el desarrollo en Python, el uso de la API de OpenAI, la configuración de la clave mediante `OPENAI_API_KEY` y la preparación de casos de prueba. También se admite que no se estableció un procedimiento formal para medir la estabilidad.
- Justificación: El uso de herramientas y metodología está descrito parcialmente, pero no puede verificarse de forma completa. No se adjuntan código fuente, dependencias, comandos de instalación y ejecución, estructura del programa, manejo de errores, parámetros del modelo ni documentación suficiente para reproducir el sistema. Por ello, la metodología y la documentación resultan incompletas.

## Fortalezas
- Presenta una estructura clara, ordenada y comprensible.
- Define correctamente el propósito general del agente evaluador.
- Reconoce la importancia de emplear una rúbrica común para favorecer evaluaciones consistentes.
- Incluye una práctica adecuada de seguridad al utilizar una variable de entorno para la clave de API.
- Identifica limitaciones relevantes, como la variabilidad del modelo y la dependencia de la calidad de la evidencia.
- Contempla componentes importantes de la devolución: puntaje, criterios, fortalezas, aspectos a mejorar y recomendaciones.

## Aspectos a mejorar
- Falta evidencia concreta de la implementación funcional mencionada.
- La documentación no permite reproducir el sistema completamente.
- No se presentan el código Python, la configuración utilizada ni ejemplos de llamadas a la API.
- Las pruebas se describen de manera general, sin casos, resultados esperados, resultados obtenidos o criterios de aceptación.
- No se explica cómo se controla que los puntajes respeten los máximos de la rúbrica y sumen correctamente.
- La trazabilidad entre evidencia, criterio, justificación y puntaje no está desarrollada en detalle.
- No existe un procedimiento formal para evaluar la estabilidad entre múltiples ejecuciones.

## Recomendaciones
1. Incorporar el código fuente completo o, al menos, los módulos principales encargados de leer archivos, construir la solicitud, invocar la API y procesar la respuesta.
2. Agregar instrucciones reproducibles de instalación y ejecución, incluyendo versión de Python, dependencias y comandos necesarios.
3. Documentar el modelo utilizado y sus parámetros relevantes, como temperatura y formato de respuesta.
4. Incluir ejemplos completos de entrada y salida que demuestren la aplicación de cada criterio de la rúbrica.
5. Presentar una tabla de pruebas con caso evaluado, resultado esperado, resultado obtenido y observaciones.
6. Ejecutar cada caso varias veces y comparar los puntajes para medir la estabilidad del agente.
7. Implementar validaciones automáticas para controlar los puntajes máximos, la suma total y la correspondencia con el nivel de desempeño.
8. Exigir que cada puntaje esté acompañado por evidencia textual concreta del trabajo evaluado.

## Conclusión
El trabajo presenta una propuesta pertinente y bien organizada para un agente evaluador basado en inteligencia artificial. Demuestra comprensión adecuada de sus componentes generales y reconoce limitaciones relevantes. Sin embargo, la ausencia de código, resultados verificables y documentación reproducible limita la profundidad y la demostración efectiva de la solución. En función de la rúbrica, alcanza un nivel **Intermedio**.


# Ejecución 3

## Identificación
- Trabajo evaluado: Trabajo práctico — Diseño de un agente evaluador con inteligencia artificial
- Fecha de evaluación: 03/09/2026

## Resultado
- Puntaje total: 71/100
- Nivel alcanzado: Intermedio

## Evaluación por criterios

### Criterio 1
- Criterio: Cumplimiento de la consigna
- Puntaje obtenido: 19
- Puntaje máximo: 25
- Evidencia encontrada: El trabajo describe el objetivo del agente, sus entradas, el procedimiento general de evaluación, el uso de la rúbrica, la integración mediante API, las pruebas, el formato de salida y las limitaciones. Sin embargo, no incluye el código del programa, ejemplos completos de evaluaciones generadas ni resultados verificables de las pruebas.
- Justificación: Cumple con la mayor parte de los componentes esperables para el diseño conceptual de un agente evaluador. No obstante, la entrega no permite comprobar plenamente la implementación ni el funcionamiento declarado, por lo que presenta omisiones relevantes de carácter técnico y práctico.

### Criterio 2
- Criterio: Calidad y profundidad del contenido
- Puntaje obtenido: 18
- Puntaje máximo: 25
- Evidencia encontrada: Se explican el objetivo del agente, su funcionamiento general, la finalidad de la rúbrica, la integración con la API y algunas limitaciones. El trabajo reconoce problemas de variabilidad, ambigüedad, trazabilidad y reproducibilidad.
- Justificación: El contenido es pertinente y demuestra una comprensión adecuada del problema. Sin embargo, varios apartados son generales y descriptivos. No se profundiza en la lógica de asignación de puntajes, el manejo de evidencia insuficiente, la validación de resultados, el control de consistencia ni el tratamiento de errores de la API.

### Criterio 3
- Criterio: Fundamentación y evidencia
- Puntaje obtenido: 12
- Puntaje máximo: 20
- Evidencia encontrada: El trabajo fundamenta el uso de una rúbrica como mecanismo para establecer criterios comunes y reducir la subjetividad. También justifica el uso de la variable de entorno `OPENAI_API_KEY` para evitar exponer la clave. No se presentan código, registros de ejecución, respuestas producidas por el agente, tablas comparativas, métricas ni resultados concretos de las pruebas.
- Justificación: Existe fundamentación conceptual para algunas decisiones, pero la evidencia es parcial. Las afirmaciones sobre el funcionamiento y las pruebas no están acompañadas por resultados que permitan verificarlas. Además, el propio trabajo señala que “no se exige una identificación exhaustiva de evidencia”, lo que limita la trazabilidad de las decisiones evaluativas.

### Criterio 4
- Criterio: Estructura, claridad y coherencia
- Puntaje obtenido: 14
- Puntaje máximo: 15
- Evidencia encontrada: El documento está dividido en diez secciones numeradas, utiliza títulos, listas y una secuencia que va desde la introducción hasta la conclusión. El vocabulario es claro y las ideas mantienen coherencia temática.
- Justificación: La estructura es clara, ordenada y fácil de seguir. Como aspecto menor, existe cierta reiteración entre las secciones “Objetivo” y “Funcionamiento general”, y podrían separarse con mayor precisión la descripción conceptual, la implementación y los resultados de las pruebas.

### Criterio 5
- Criterio: Uso adecuado de herramientas, metodología y documentación
- Puntaje obtenido: 8
- Puntaje máximo: 15
- Evidencia encontrada: Se indica que el sistema utiliza Python, la API de OpenAI y la variable de entorno `OPENAI_API_KEY`. También se presenta un procedimiento general y se menciona la preparación de casos de prueba. Sin embargo, no se incluyen código fuente, dependencias, versiones, instrucciones de instalación y ejecución, estructura de archivos, configuración del modelo, parámetros utilizados ni un protocolo formal de pruebas.
- Justificación: El uso de herramientas y metodología está descrito de manera parcial, pero no puede verificarse ni reproducirse con la documentación presentada. La falta de artefactos técnicos y de instrucciones operativas impide considerar suficiente la documentación.

## Fortalezas
- Presenta una estructura clara y una redacción comprensible.
- Define correctamente el propósito general del agente evaluador.
- Reconoce la importancia de aplicar una rúbrica común para mejorar la consistencia.
- Incluye una práctica adecuada de seguridad al proponer el uso de `OPENAI_API_KEY` como variable de entorno.
- Identifica limitaciones relevantes, como la variabilidad entre ejecuciones, la ambigüedad de la evidencia y la necesidad de revisión.
- Considera componentes importantes de la devolución, como puntaje, fortalezas, aspectos a mejorar y recomendaciones.

## Aspectos a mejorar
- Falta incorporar el código fuente o una evidencia verificable de la implementación.
- No se documentan los pasos necesarios para instalar, configurar y ejecutar el sistema.
- Las pruebas se describen de manera general, sin casos completos, resultados ni criterios de comparación.
- No se explica cómo se garantiza que los puntajes respeten los máximos de cada criterio ni cómo se calcula y valida el total.
- La trazabilidad es insuficiente, especialmente porque no se exige evidencia exhaustiva para cada decisión.
- No se detallan el modelo, los parámetros de generación, el manejo de errores, las dependencias ni las versiones empleadas.
- No existe un procedimiento formal para medir estabilidad y consistencia entre múltiples ejecuciones.

## Recomendaciones
- Incorporar el programa en Python y explicar sus componentes principales.
- Agregar instrucciones reproducibles de instalación, configuración y ejecución, incluyendo dependencias y versiones.
- Documentar el modelo utilizado, sus parámetros y la forma en que se construyen y envían las solicitudes a la API.
- Exigir que cada puntaje esté acompañado por evidencia concreta extraída del trabajo evaluado.
- Añadir validaciones automáticas para controlar máximos por criterio, suma total y correspondencia con el nivel de desempeño.
- Presentar varios casos de prueba completos con entradas, salidas, puntajes esperados y análisis de diferencias.
- Ejecutar cada caso varias veces y comparar los resultados para medir estabilidad.
- Documentar el manejo de errores, como ausencia de archivos, rúbricas incompletas, respuestas inválidas o fallos de conexión con la API.

## Conclusión
El trabajo presenta un diseño conceptual claro y pertinente de un agente evaluador y demuestra una comprensión adecuada de sus componentes generales. Su principal debilidad es la falta de evidencia técnica y experimental que permita verificar y reproducir la solución. Por ello, alcanza un nivel **Intermedio**, con necesidad de fortalecer la implementación, la trazabilidad, las pruebas y la documentación técnica.
