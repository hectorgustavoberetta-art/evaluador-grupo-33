# Calibración del caso intermedio

Puntajes obtenidos: [68, 75, 68]

Promedio: 70.33/100



# Ejecución 1

## Identificación
- Trabajo evaluado: Trabajo práctico — Diseño de un agente evaluador con inteligencia artificial
- Fecha de evaluación: 03/09/2026

## Resultado
- Puntaje total: 68/100
- Nivel alcanzado: Deficiente

## Evaluación por criterios

- Criterio: 1 — Cumplimiento de la consigna
- Puntaje obtenido: 18
- Puntaje máximo: 25
- Evidencia encontrada: El trabajo describe el objetivo del agente, sus entradas, el procedimiento de evaluación, el uso de una rúbrica, la integración mediante API, las pruebas, el formato de salida y las limitaciones. Sin embargo, no incluye el código del programa, ejemplos de ejecución, resultados de las pruebas ni una demostración verificable del agente.
- Justificación: Cumple con la mayor parte de los componentes conceptuales esperables para el diseño de un agente evaluador. No obstante, la afirmación de que se desarrolló una “solución funcional” no está acompañada por artefactos o resultados que permitan comprobar su implementación y funcionamiento.

- Criterio: 2 — Calidad y profundidad del contenido
- Puntaje obtenido: 17
- Puntaje máximo: 25
- Evidencia encontrada: Se explican las funciones principales del agente y se reconocen cuestiones relevantes, como la subjetividad, la variación entre ejecuciones, la claridad de la rúbrica, la trazabilidad y la reproducibilidad. El desarrollo técnico de estos temas es general y no detalla la arquitectura, el procesamiento de entradas, el cálculo de puntajes, la gestión de errores o los mecanismos de validación.
- Justificación: El contenido es pertinente y demuestra una comprensión adecuada del propósito general del sistema. Sin embargo, varios apartados presentan descripciones breves y conceptuales, sin suficiente profundidad técnica o metodológica.

- Criterio: 3 — Fundamentación y evidencia
- Puntaje obtenido: 10
- Puntaje máximo: 20
- Evidencia encontrada: El trabajo justifica conceptualmente el uso de una rúbrica para reducir la subjetividad y el uso de la variable de entorno `OPENAI_API_KEY` para evitar exponer la clave. También reconoce que no se exige una identificación exhaustiva de evidencia y que no se estableció un procedimiento formal para medir la estabilidad de los resultados. No se presentan fuentes, datos, casos de prueba, puntajes obtenidos, comparaciones ni registros de ejecución.
- Justificación: La fundamentación es parcial. Existen explicaciones razonables sobre algunas decisiones, pero faltan evidencias concretas que respalden la efectividad, consistencia y funcionalidad del sistema. La ausencia de trazabilidad exhaustiva para cada decisión evaluativa constituye una debilidad relevante en un agente que debe justificar sus puntajes.

- Criterio: 4 — Estructura, claridad y coherencia
- Puntaje obtenido: 14
- Puntaje máximo: 15
- Evidencia encontrada: El documento está organizado en diez secciones numeradas y sigue una secuencia lógica: introducción, objetivo, funcionamiento, rúbrica, justificación, API, pruebas, salida, limitaciones y conclusión. El lenguaje es claro y las ideas se mantienen relacionadas con el tema central.
- Justificación: La estructura es clara, ordenada y fácil de seguir. La principal limitación es cierta repetición entre el objetivo, el funcionamiento general y la conclusión, pero esto no dificulta significativamente la comprensión.

- Criterio: 5 — Uso adecuado de herramientas, metodología y documentación
- Puntaje obtenido: 9
- Puntaje máximo: 15
- Evidencia encontrada: Se menciona el uso de Python, la API de OpenAI y la variable de entorno `OPENAI_API_KEY`. También se describe una metodología general de seis pasos y la preparación de trabajos de prueba. No se incluyen código, dependencias, instrucciones de instalación y ejecución, estructura de archivos, parámetros del modelo, manejo de errores, resultados de pruebas ni mecanismos de reproducibilidad.
- Justificación: El uso de herramientas y metodología está planteado, pero su documentación es incompleta. La ausencia de materiales técnicos y resultados impide verificar si las herramientas fueron utilizadas correctamente y si el sistema puede reproducirse.

## Fortalezas

- Presenta una estructura clara y coherente.
- Define adecuadamente el propósito general del agente evaluador.
- Identifica los principales componentes del sistema: instrucciones, rúbrica y trabajo a evaluar.
- Incluye una práctica adecuada de seguridad al utilizar `OPENAI_API_KEY` como variable de entorno.
- Reconoce limitaciones importantes, como la variabilidad del modelo, la ambigüedad de la evidencia y la necesidad de revisión.
- Considera elementos relevantes de la devolución, como puntaje, fortalezas, aspectos a mejorar y recomendaciones.

## Aspectos a mejorar

- Falta evidencia verificable de que el agente haya sido implementado y funcione.
- No se incluye el código Python ni documentación técnica suficiente.
- Las pruebas se describen de manera general, pero no se presentan casos, resultados o comparaciones.
- No existe un procedimiento formal para medir consistencia, estabilidad o reproducibilidad.
- La trazabilidad de las calificaciones es insuficiente, ya que el propio trabajo indica que no se exige evidencia exhaustiva para cada decisión.
- No se detallan aspectos técnicos como selección y configuración del modelo, manejo de errores, validación de entradas o cálculo automático del puntaje.
- La afirmación de que el sistema es una “solución funcional” carece de evidencia concreta dentro de la entrega.

## Recomendaciones

1. Incorporar el código completo del programa en Python o un enlace verificable al repositorio.
2. Documentar la instalación, dependencias, configuración de la API y procedimiento de ejecución.
3. Incluir ejemplos completos de entrada y salida generados por el agente.
4. Presentar una tabla de casos de prueba con resultados esperados, resultados obtenidos y análisis de diferencias.
5. Ejecutar cada caso varias veces para medir la variación de los puntajes y documentar la estabilidad.
6. Exigir que cada puntaje esté asociado con evidencia concreta del trabajo evaluado.
7. Definir parámetros de ejecución que favorezcan la reproducibilidad, como el modelo utilizado y su configuración.
8. Agregar validaciones para detectar rúbricas incompletas, trabajos vacíos, respuestas mal formateadas y errores de la API.
9. Separar con mayor precisión la arquitectura, la metodología de evaluación, la implementación y la validación del sistema.

## Conclusión

El trabajo presenta una explicación clara y pertinente del diseño conceptual de un agente evaluador basado en inteligencia artificial. Su principal fortaleza es la organización del contenido y el reconocimiento de limitaciones relevantes. Sin embargo, la falta de código, documentación técnica, resultados de pruebas y evidencia de trazabilidad impide verificar la funcionalidad, consistencia y reproducibilidad del sistema. Por estas omisiones, el trabajo alcanza un nivel Deficiente según los rangos establecidos en la rúbrica.


# Ejecución 2

## Identificación
- Trabajo evaluado: Trabajo práctico — Diseño de un agente evaluador con inteligencia artificial
- Fecha de evaluación: 03/09/2026

## Resultado
- Puntaje total: 75/100
- Nivel alcanzado: Intermedio

## Evaluación por criterios

- Criterio: Cumplimiento de la consigna
- Puntaje obtenido: 19
- Puntaje máximo: 25
- Evidencia encontrada: El trabajo define el objetivo del agente, describe sus entradas, presenta un procedimiento general de evaluación, explica el uso de la rúbrica, menciona la integración mediante API, las pruebas, el formato de salida y las limitaciones. Sin embargo, no incluye el código, ejemplos de ejecución ni una demostración concreta del agente desarrollado.
- Justificación: Cumple con la mayor parte de los elementos esperables para el diseño conceptual de un agente evaluador. La ausencia de evidencias de implementación y funcionamiento impide considerar que el desarrollo del agente esté completamente demostrado.

- Criterio: Calidad y profundidad del contenido
- Puntaje obtenido: 18
- Puntaje máximo: 25
- Evidencia encontrada: Se explican el objetivo, el funcionamiento general, la función de la rúbrica, la integración con la API de OpenAI, las pruebas y las limitaciones. El trabajo reconoce problemas de subjetividad, variabilidad y reproducibilidad. No obstante, las secciones presentan descripciones generales y no profundizan en la arquitectura, el procesamiento de entradas, el cálculo de puntajes o el tratamiento de errores.
- Justificación: El contenido es pertinente y demuestra una comprensión adecuada del propósito del agente, pero su desarrollo es principalmente conceptual. Faltan detalles técnicos y operativos que permitan comprender con profundidad cómo se implementó y validó el sistema.

- Criterio: Fundamentación y evidencia
- Puntaje obtenido: 13
- Puntaje máximo: 20
- Evidencia encontrada: El trabajo fundamenta el uso de la rúbrica como mecanismo para establecer criterios comunes y reducir parte de la subjetividad. También justifica el empleo de la variable de entorno `OPENAI_API_KEY` para evitar exponer la clave. Sin embargo, no presenta fragmentos de código, resultados de pruebas, ejemplos de evaluaciones, métricas ni comparaciones concretas entre ejecuciones.
- Justificación: Existe una fundamentación adecuada de las principales decisiones generales, pero la evidencia que permitiría verificar el funcionamiento y los resultados es limitada. El propio trabajo indica que no se exige una identificación exhaustiva de evidencia, lo cual reduce la trazabilidad de las decisiones del agente.

- Criterio: Estructura, claridad y coherencia
- Puntaje obtenido: 15
- Puntaje máximo: 15
- Evidencia encontrada: El documento se organiza en diez secciones claramente identificadas: introducción, objetivo, funcionamiento, rúbrica, justificación, integración mediante API, pruebas, formato de salida, limitaciones y conclusión. Las ideas siguen una secuencia lógica y el lenguaje es claro.
- Justificación: La estructura es ordenada, coherente y fácil de seguir. Cada sección cumple una función definida y existe correspondencia entre el objetivo inicial y las conclusiones.

- Criterio: Uso adecuado de herramientas, metodología y documentación
- Puntaje obtenido: 10
- Puntaje máximo: 15
- Evidencia encontrada: Se menciona el desarrollo en Python, el uso de la API de OpenAI y el almacenamiento seguro de la clave mediante `OPENAI_API_KEY`. También se describe un procedimiento general y la preparación de casos de prueba. No se aporta código, configuración, dependencias, instrucciones de ejecución, diseño de los casos de prueba ni resultados obtenidos.
- Justificación: Las herramientas y la metodología seleccionadas son adecuadas, pero su utilización solo se documenta de manera general. La documentación técnica y de validación es insuficiente para reproducir o verificar el sistema.

## Fortalezas

- Presenta una organización clara y una secuencia lógica.
- Define correctamente el propósito y las funciones principales del agente evaluador.
- Reconoce la importancia de aplicar una rúbrica común para mejorar la consistencia.
- Incluye una práctica adecuada de seguridad al utilizar la variable de entorno `OPENAI_API_KEY`.
- Identifica limitaciones relevantes, como la variabilidad entre ejecuciones, la dependencia de la claridad de la rúbrica y la necesidad de revisión ante situaciones ambiguas.
- Considera componentes importantes de la devolución, como puntaje, fortalezas, aspectos a mejorar y recomendaciones.

## Aspectos a mejorar

- Falta evidencia concreta de que el agente fue efectivamente implementado y ejecutado.
- La arquitectura y el flujo técnico están descriptos de manera superficial.
- No se documentan las instrucciones exactas utilizadas, el tratamiento de archivos, el modelo seleccionado ni los parámetros de la API.
- Los casos de prueba no están identificados ni acompañados por entradas, resultados esperados y resultados obtenidos.
- No existe un procedimiento formal para evaluar consistencia, estabilidad o reproducibilidad.
- La decisión de no exigir evidencia exhaustiva para cada puntaje debilita la trazabilidad de la evaluación.
- No se incluyen instrucciones de instalación, ejecución, manejo de errores o dependencias.

## Recomendaciones

1. Incorporar el código fuente o, al menos, los fragmentos principales de la integración con la API.
2. Documentar la arquitectura del sistema y el flujo completo desde la recepción del trabajo hasta la generación de la devolución.
3. Especificar el modelo utilizado, los parámetros de configuración, las dependencias y los pasos necesarios para ejecutar el programa.
4. Exigir que cada puntaje esté acompañado por evidencia concreta extraída del trabajo evaluado.
5. Presentar una tabla de pruebas con entradas, resultados esperados, resultados obtenidos y análisis de diferencias.
6. Ejecutar cada caso varias veces y comparar los puntajes para medir la estabilidad de los resultados.
7. Incorporar controles para validar el formato de salida, los límites máximos de cada criterio y la suma del puntaje total.
8. Documentar el tratamiento de errores, como archivos faltantes, rúbricas incompletas, respuestas inválidas de la API o ausencia de evidencia.

## Conclusión

El trabajo presenta un diseño conceptual claro, pertinente y bien estructurado de un agente evaluador con inteligencia artificial. Expone adecuadamente sus componentes principales y reconoce limitaciones relevantes. Sin embargo, la falta de código, resultados verificables, documentación técnica detallada y un procedimiento formal de validación limita la demostración de su funcionamiento y reproducibilidad. Por estas razones, alcanza un nivel Intermedio.


# Ejecución 3

## Identificación
- Trabajo evaluado: Trabajo práctico — Diseño de un agente evaluador con inteligencia artificial
- Fecha de evaluación: 03/09/2026

## Resultado
- Puntaje total: 68/100
- Nivel alcanzado: Deficiente

## Evaluación por criterios

### Criterio 1
- Criterio: Cumplimiento de la consigna
- Puntaje obtenido: 18/25
- Puntaje máximo: 25
- Evidencia encontrada: El trabajo describe el objetivo del agente, su funcionamiento general, el uso de la rúbrica, la integración mediante la API de OpenAI, las pruebas, el formato de salida y las limitaciones. No incluye el código del programa, ejemplos de ejecución ni resultados concretos de las pruebas.
- Justificación: Cumple con la mayor parte del propósito general de diseñar un agente evaluador y aborda sus componentes principales. Sin embargo, la presentación se concentra en una descripción conceptual. La afirmación de que el sistema constituye una “solución funcional” no puede verificarse con los elementos entregados. Además, no se proporcionó una consigna independiente con requisitos técnicos más específicos, por lo que el cumplimiento solo puede valorarse a partir del objetivo declarado en el propio trabajo.

### Criterio 2
- Criterio: Calidad y profundidad del contenido
- Puntaje obtenido: 17/25
- Puntaje máximo: 25
- Evidencia encontrada: Se explican el flujo general del agente, la función de la rúbrica, el manejo de la clave mediante `OPENAI_API_KEY`, la existencia de casos de prueba y limitaciones como la variabilidad entre ejecuciones. El propio trabajo reconoce oportunidades de mejora en “trazabilidad, documentación técnica, validación de resultados y reproducibilidad”.
- Justificación: El contenido es pertinente y demuestra una comprensión adecuada de los componentes básicos de un agente evaluador. No obstante, varios aspectos están desarrollados de manera general. Faltan detalles sobre la arquitectura del programa, la construcción de solicitudes a la API, el procesamiento de respuestas, el cálculo de puntajes, el control de errores y los mecanismos utilizados para asegurar evaluaciones consistentes.

### Criterio 3
- Criterio: Fundamentación y evidencia
- Puntaje obtenido: 11/20
- Puntaje máximo: 20
- Evidencia encontrada: El trabajo fundamenta el uso de la rúbrica como medio para establecer criterios comunes y señala que la variable de entorno evita exponer la clave. También reconoce que no se exige “una identificación exhaustiva de evidencia para cada decisión” y que no se estableció un procedimiento formal para medir la estabilidad de los resultados.
- Justificación: Existe fundamentación conceptual, pero la evidencia es insuficiente para comprobar el funcionamiento y la calidad del sistema. No se presentan fragmentos de código, salidas generadas, tablas comparativas, resultados de casos de prueba ni mediciones de consistencia. La falta de trazabilidad exhaustiva también debilita la justificación de los puntajes, dado que un agente evaluador debe vincular cada decisión con evidencia concreta.

### Criterio 4
- Criterio: Estructura, claridad y coherencia
- Puntaje obtenido: 14/15
- Puntaje máximo: 15
- Evidencia encontrada: El documento está dividido en diez secciones numeradas y sigue una secuencia lógica: introducción, objetivo, funcionamiento, rúbrica, justificación, API, pruebas, formato de salida, limitaciones y conclusión. Se utilizan listas para presentar procesos y componentes.
- Justificación: La estructura es clara, ordenada y fácil de seguir. Las ideas mantienen coherencia entre las diferentes secciones. Como aspecto menor, existe cierta reiteración entre el objetivo, el funcionamiento general y la conclusión.

### Criterio 5
- Criterio: Uso adecuado de herramientas, metodología y documentación
- Puntaje obtenido: 8/15
- Puntaje máximo: 15
- Evidencia encontrada: Se menciona el uso de Python, la API de OpenAI y la variable de entorno `OPENAI_API_KEY`. También se describe un procedimiento general de seis pasos y se informa la preparación de trabajos de prueba. No se adjuntan código, dependencias, instrucciones de instalación o ejecución, configuración del modelo, parámetros, archivos utilizados ni resultados de pruebas.
- Justificación: Las herramientas y la metodología elegidas son apropiadas, particularmente el manejo de la clave mediante una variable de entorno. Sin embargo, su uso solo se documenta de manera declarativa. La ausencia de documentación técnica y evidencia de implementación impide reproducir, revisar o validar el sistema.

## Fortalezas
- Presenta una estructura clara y una redacción comprensible.
- Identifica correctamente los componentes básicos de un agente evaluador.
- Reconoce la importancia de utilizar una rúbrica para reducir la subjetividad.
- Propone una práctica adecuada de seguridad al utilizar `OPENAI_API_KEY`.
- Incluye limitaciones relevantes, como la variabilidad del modelo y la dependencia de la claridad de la rúbrica.
- Reconoce de manera explícita las debilidades relacionadas con trazabilidad, validación y reproducibilidad.

## Aspectos a mejorar
- Falta evidencia concreta que demuestre que el agente fue implementado y funciona.
- La explicación técnica de la integración con la API es insuficiente.
- No se documentan los casos de prueba ni sus resultados.
- No se explica cómo se valida el formato de salida ni cómo se controlan puntajes inválidos.
- No existe un procedimiento formal para medir la estabilidad entre ejecuciones.
- La identificación no exhaustiva de evidencia contradice la necesidad de producir evaluaciones trazables y fundamentadas.
- La afirmación de que se trata de una solución funcional no está respaldada por evidencia verificable.

## Recomendaciones
1. Incorporar el código fuente o, como mínimo, fragmentos relevantes que muestren la carga de instrucciones, rúbrica y trabajo, la llamada a la API y el procesamiento de la respuesta.
2. Agregar instrucciones de instalación y ejecución, dependencias, versión de Python, modelo utilizado y parámetros de configuración.
3. Presentar al menos tres casos de prueba de diferente calidad, junto con sus entradas, puntajes, devoluciones y análisis de resultados.
4. Ejecutar cada caso varias veces y comparar los puntajes para medir la estabilidad y reproducibilidad.
5. Exigir que cada criterio de evaluación incluya evidencia concreta, puntaje y justificación.
6. Implementar validaciones automáticas para comprobar que los puntajes no superen los máximos y que la suma total sea correcta.
7. Documentar el manejo de errores de la API, respuestas incompletas, archivos faltantes y ausencia de evidencia.
8. Sustituir afirmaciones generales sobre la funcionalidad por resultados verificables de ejecución.

## Conclusión
El trabajo presenta una descripción clara y pertinente del diseño general de un agente evaluador, con una adecuada organización y una identificación correcta de varias limitaciones. Sin embargo, carece de evidencia técnica, resultados de pruebas y documentación suficiente para verificar que la solución sea funcional, reproducible y trazable. Estas omisiones reducen significativamente la fundamentación y la evaluación del uso de herramientas, por lo que alcanza 68/100 y se ubica en el nivel Deficiente.
