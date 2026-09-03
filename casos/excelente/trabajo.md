# Trabajo práctico — Diseño de un agente evaluador con inteligencia artificial

## 1. Introducción

El presente trabajo propone el diseño e implementación de un agente de inteligencia artificial capaz de evaluar trabajos académicos de manera objetiva, consistente, trazable y reproducible.

El agente utiliza una rúbrica explícita como única referencia para asignar puntajes. Cada decisión debe estar respaldada por evidencia concreta encontrada en el trabajo evaluado y acompañada por una justificación comprensible.

El sistema fue diseñado para evitar evaluaciones basadas únicamente en impresiones generales y para permitir que otra persona pueda reconstruir el razonamiento utilizado para otorgar cada puntaje.

## 2. Objetivo

El objetivo general es construir un agente evaluador capaz de:

1. Leer diferentes trabajos académicos.
2. Interpretar una rúbrica previamente definida.
3. Analizar cada criterio de evaluación por separado.
4. Identificar evidencias concretas dentro del trabajo.
5. Asignar un puntaje para cada criterio.
6. Justificar cada puntaje.
7. Calcular el puntaje total.
8. Generar una devolución estructurada.
9. Mantener criterios consistentes entre diferentes evaluaciones.

## 3. Arquitectura del agente

El sistema se organiza en cuatro componentes principales:

- `system_prompt.md`: define el rol, las restricciones y el procedimiento del agente.
- `rubrica.md`: contiene los criterios, niveles de desempeño y puntajes máximos.
- `formato_salida.md`: establece la estructura obligatoria de la devolución.
- `evaluador.py`: ejecuta el agente y conecta el sistema con la API de OpenAI.

Los trabajos que deben ser evaluados se almacenan como archivos independientes, lo que permite utilizar el mismo agente con diferentes entregas sin modificar la rúbrica.

## 4. Metodología de evaluación

El agente sigue una metodología de ocho etapas:

1. Leer completamente el trabajo presentado.
2. Identificar los requisitos de la consigna.
3. Leer todos los criterios de la rúbrica.
4. Analizar cada criterio de manera independiente.
5. Localizar evidencia concreta relacionada con cada criterio.
6. Asignar un puntaje dentro del rango permitido.
7. Justificar la relación entre evidencia, criterio y puntaje.
8. Calcular el resultado total y producir una devolución final.

Esta secuencia busca reducir la arbitrariedad y garantizar que todas las evaluaciones utilicen el mismo procedimiento.

## 5. Uso estricto de la rúbrica

La rúbrica constituye la fuente principal para tomar decisiones.

El agente no debe inventar criterios, modificar los puntajes máximos ni introducir requisitos que no hayan sido establecidos previamente.

Cada criterio debe ser analizado de forma independiente y el puntaje asignado debe corresponder al nivel de cumplimiento demostrado por la evidencia encontrada.

Si no existe evidencia suficiente para justificar un determinado nivel, el agente debe asignar un puntaje inferior en lugar de completar la información mediante suposiciones.

## 6. Trazabilidad

La trazabilidad es un requisito central del sistema.

Para cada criterio, la salida debe incluir:

- criterio evaluado;
- puntaje obtenido;
- puntaje máximo;
- evidencia encontrada;
- justificación del puntaje.

Esto permite reconstruir la relación:

**criterio → evidencia → justificación → puntaje**

De esta forma, la evaluación puede ser revisada por un docente o por otro evaluador.

## 7. Consistencia

El agente debe aplicar los mismos criterios a todos los trabajos.

No debe modificar la exigencia según el estudiante ni utilizar información externa para compensar información faltante.

Para comprobar la consistencia se prepararon tres casos de calibración:

- caso deficiente;
- caso intermedio;
- caso excelente.

Los casos contienen diferentes niveles de desarrollo y permiten verificar si el agente discrimina adecuadamente entre trabajos de distinta calidad.

## 8. Integración mediante API

El agente utiliza la API de OpenAI desde un programa desarrollado en Python.

La comunicación se realiza mediante el SDK oficial de OpenAI y la Responses API.

El programa envía al modelo:

- las instrucciones del agente;
- la rúbrica;
- el formato de salida;
- el trabajo que debe evaluarse.

La respuesta generada por el modelo se recupera posteriormente y se presenta como resultado de la evaluación.

Este diseño permite utilizar el agente sobre múltiples trabajos sin tener que copiar manualmente los contenidos en una interfaz conversacional.

## 9. Seguridad de la API y manejo de tokens

La clave de acceso a la API no se incluye dentro del código fuente.

El programa obtiene la clave mediante la variable de entorno:

`OPENAI_API_KEY`

En GitHub Codespaces, esta variable se configura como un secreto del repositorio.

De esta forma, la clave no queda expuesta en el código ni en el historial de Git.

El consumo de tokens depende de cuatro elementos principales:

- tamaño del system prompt;
- extensión de la rúbrica;
- longitud del trabajo evaluado;
- extensión de la respuesta solicitada.

Para controlar costos se busca evitar información redundante en los prompts y mantener las instrucciones suficientemente precisas.

## 10. Implementación

El programa `evaluador.py` realiza las siguientes acciones:

1. carga la clave de API desde una variable de entorno;
2. lee el `system_prompt.md`;
3. lee la `rubrica.md`;
4. lee el `formato_salida.md`;
5. carga el trabajo seleccionado;
6. construye las instrucciones de evaluación;
7. realiza una solicitud a la API;
8. recupera la respuesta;
9. presenta el resultado de la evaluación.

Además, el sistema incorpora explícitamente la fecha de evaluación utilizando la zona horaria definida para evitar que el modelo invente una fecha.

## 11. Pruebas y calibración

El agente se prueba utilizando tres trabajos deliberadamente diferentes.

El caso deficiente contiene información incompleta, escasa justificación y poca trazabilidad.

El caso intermedio presenta una estructura adecuada y utiliza la rúbrica, pero desarrolla parcialmente algunos componentes.

El caso excelente incorpora una metodología completa, trazabilidad, arquitectura técnica, integración mediante API, seguridad de credenciales, consideración del consumo de tokens, pruebas y documentación.

La expectativa de calibración es que los puntajes sigan el orden:

**Deficiente < Intermedio < Excelente**

Si los resultados no respetan esta relación, deben revisarse los casos de calibración, el prompt o la rúbrica antes de utilizar el agente sobre trabajos reales.

## 12. Reproducibilidad

El proyecto se almacena en un repositorio Git.

Los archivos necesarios para ejecutar el sistema se encuentran documentados y las dependencias se especifican en `requirements.txt`.

Una ejecución puede reproducirse mediante:

1. clonar o abrir el repositorio;
2. instalar las dependencias;
3. configurar `OPENAI_API_KEY`;
4. seleccionar el trabajo a evaluar;
5. ejecutar `python agente/evaluador.py`.

Esto permite que otro integrante del equipo pueda ejecutar el mismo agente utilizando la misma configuración.

## 13. Limitaciones

El uso de un modelo de lenguaje no elimina completamente la variabilidad.

Dos ejecuciones pueden presentar pequeñas diferencias en la redacción o en la interpretación de evidencias ambiguas.

Por ese motivo, la rúbrica debe estar claramente definida, las instrucciones deben restringir la evaluación y los casos de calibración deben utilizarse para comprobar el comportamiento del agente.

El sistema tampoco debe reemplazar automáticamente el juicio docente cuando exista evidencia insuficiente o una situación que requiera interpretación especializada.

## 14. Formato de salida

La evaluación final debe incluir:

- identificación del trabajo;
- fecha de evaluación;
- puntaje total;
- nivel alcanzado;
- evaluación individual de cada criterio;
- evidencia encontrada;
- justificación;
- fortalezas;
- aspectos a mejorar;
- recomendaciones.

## 15. Conclusión

El agente evaluador desarrollado combina una rúbrica explícita, un procedimiento estructurado, trazabilidad de las decisiones, integración mediante API y mecanismos básicos de seguridad y reproducibilidad.

La utilización de casos de calibración permite comprobar si el sistema discrimina adecuadamente entre distintos niveles de calidad.

El objetivo no es solamente obtener una calificación automática, sino construir una evaluación que pueda ser comprendida, revisada y reproducida por otras personas.


## 16. Evidencia de pruebas y resultados de calibración

Para verificar el comportamiento del agente se realizaron ejecuciones reales mediante la API sobre los tres casos de calibración preparados.

En una primera ronda de pruebas se obtuvieron los siguientes resultados:

- Caso deficiente: 38/100.
- Caso intermedio: 57/100.
- Caso excelente, versión inicial: 81/100.

Los resultados respetaron el orden esperado:

**Deficiente < Intermedio < Excelente**

Esto permitió comprobar que el agente no asigna una calificación uniforme, sino que discrimina entre trabajos con diferente grado de desarrollo.

La evaluación de la versión inicial del caso excelente permitió además identificar oportunidades de mejora. El agente señaló principalmente menor fundamentación y evidencia, junto con aspectos de documentación técnica y metodológica que podían desarrollarse con mayor profundidad.

A partir de esa devolución se realizó una segunda versión del caso excelente, manteniendo sin modificaciones la rúbrica utilizada para evaluarlo. Esta decisión permite utilizar la calibración como un proceso de validación del sistema y no como un mecanismo para modificar los criterios con el objetivo de obtener artificialmente una calificación superior.

### Criterios de aceptación de la calibración

Se consideran indicadores favorables del funcionamiento del agente:

1. que el caso deficiente obtenga un puntaje inferior al caso intermedio;
2. que el caso intermedio obtenga un puntaje inferior al caso excelente;
3. que las diferencias de puntaje estén justificadas mediante evidencias del contenido;
4. que el agente utilice los mismos criterios y puntajes máximos en los tres casos;
5. que las devoluciones permitan identificar qué aspectos explican las diferencias entre los resultados.

### Evidencia técnica de ejecución

Las pruebas se realizaron ejecutando:

`python agente/evaluador.py`

El programa cargó el trabajo seleccionado, el `system_prompt.md`, la `rubrica.md` y el `formato_salida.md`, realizó la solicitud mediante la API y devolvió una evaluación estructurada por criterios.

Durante las pruebas también se verificó el manejo seguro de la credencial de acceso mediante `OPENAI_API_KEY`, evitando incorporar la clave directamente en el código fuente.

Los resultados obtenidos constituyen evidencia empírica preliminar del funcionamiento del agente y permiten orientar las siguientes iteraciones de calibración.