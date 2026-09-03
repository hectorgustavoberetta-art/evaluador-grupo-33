# Trabajo práctico — Diseño de un agente evaluador con inteligencia artificial

## 1. Introducción

El objetivo de este trabajo es desarrollar un agente de inteligencia artificial capaz de evaluar trabajos académicos utilizando una rúbrica previamente definida.

El agente busca aplicar criterios comunes a diferentes entregas y generar una devolución que permita conocer el resultado general, las fortalezas del trabajo y sus principales aspectos a mejorar.

## 2. Objetivo

El agente debe ser capaz de:

1. leer un trabajo presentado por un estudiante;
2. consultar una rúbrica de evaluación;
3. analizar los criterios establecidos;
4. asignar un puntaje;
5. calcular una calificación final;
6. generar una devolución para el estudiante.

## 3. Funcionamiento general

El sistema utiliza tres elementos principales:

- un archivo con las instrucciones del agente;
- una rúbrica con los criterios de evaluación;
- el trabajo que debe ser evaluado.

El agente recibe estos elementos y compara el contenido del trabajo con los criterios establecidos en la rúbrica.

El procedimiento general consiste en:

1. leer el trabajo;
2. identificar los aspectos principales;
3. revisar los criterios de la rúbrica;
4. asignar puntajes;
5. calcular el resultado;
6. generar una devolución.

## 4. Uso de la rúbrica

La rúbrica permite establecer criterios comunes para todos los trabajos.

Cada criterio posee un puntaje máximo y diferentes niveles de cumplimiento. El agente debe utilizar esos niveles como referencia para determinar el puntaje correspondiente.

Esto permite reducir parte de la subjetividad de la evaluación, aunque pueden existir diferencias de interpretación cuando la evidencia presentada por el estudiante no sea suficientemente clara.

## 5. Justificación de la evaluación

El agente debe explicar los principales motivos de la calificación asignada.

Cuando sea posible, la devolución debe relacionar el puntaje con información encontrada en el trabajo.

Sin embargo, no se exige una identificación exhaustiva de evidencia para cada decisión tomada por el agente.

## 6. Integración mediante API

El agente se ejecuta mediante un programa desarrollado en Python y utiliza la API de OpenAI.

La clave de acceso no debe escribirse directamente dentro del código. Para evitar exponerla, se utiliza la variable de entorno:

`OPENAI_API_KEY`

El programa envía las instrucciones, la rúbrica y el trabajo al modelo y posteriormente recupera la respuesta generada.

## 7. Pruebas

Para observar el comportamiento del agente se prepararon diferentes trabajos de prueba.

Los casos representan distintos niveles de calidad y permiten comparar los puntajes generados.

Se espera que un trabajo con mayor desarrollo obtenga una calificación superior a otro que presente información incompleta.

Las pruebas permiten detectar problemas generales del evaluador, aunque no se estableció un procedimiento formal para medir la estabilidad de los resultados entre múltiples ejecuciones.

## 8. Formato de salida

La devolución debería contener:

- identificación del trabajo;
- puntaje total;
- comentarios sobre los criterios evaluados;
- fortalezas;
- aspectos a mejorar;
- recomendaciones.

El objetivo es que el estudiante pueda comprender los principales motivos de la evaluación.

## 9. Limitaciones

El sistema depende de un modelo de lenguaje, por lo que pueden existir variaciones entre distintas ejecuciones.

Además, la calidad de la evaluación depende de la claridad de la rúbrica y de la información disponible en el trabajo.

El agente puede facilitar la tarea de evaluación, pero los resultados deberían ser revisados cuando existan situaciones ambiguas.

## 10. Conclusión

La utilización de un agente de inteligencia artificial puede ayudar a sistematizar la evaluación de trabajos académicos.

El uso de una rúbrica permite establecer criterios comunes y generar devoluciones más ordenadas. La integración mediante API facilita la automatización del proceso y permite aplicar el mismo agente sobre diferentes trabajos.

El sistema desarrollado constituye una solución funcional, aunque todavía puede mejorarse en aspectos relacionados con la trazabilidad, la documentación técnica, la validación de resultados y la reproducibilidad.