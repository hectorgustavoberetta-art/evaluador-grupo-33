# Trabajo práctico — Diseño de un agente evaluador con inteligencia artificial

## Introducción

El presente trabajo tiene como objetivo diseñar un agente de inteligencia artificial capaz de evaluar trabajos académicos de manera objetiva, consistente y trazable. Para ello se propone utilizar una rúbrica explícita que permita asignar puntajes a diferentes criterios y justificar cada decisión tomada durante la evaluación.

## Desarrollo

El agente evaluador recibe como entrada un trabajo presentado por un estudiante y una rúbrica de evaluación.

Antes de asignar una calificación, el agente debe analizar completamente el trabajo e identificar evidencias concretas relacionadas con cada criterio de la rúbrica.

El proceso de evaluación se organiza en las siguientes etapas:

1. Leer completamente el trabajo presentado.
2. Identificar los requisitos establecidos en la consigna.
3. Analizar cada criterio definido en la rúbrica.
4. Buscar evidencias concretas dentro del trabajo.
5. Asignar un puntaje para cada criterio.
6. Justificar cada puntaje utilizando las evidencias encontradas.
7. Calcular el puntaje total.
8. Generar una devolución final indicando fortalezas y aspectos a mejorar.

## Uso de una rúbrica

La utilización de una rúbrica permite reducir la subjetividad del proceso de evaluación.

Cada criterio posee un puntaje máximo y diferentes niveles de cumplimiento. El agente debe seleccionar el nivel que mejor represente las evidencias encontradas en el trabajo.

La calificación nunca debe basarse únicamente en una impresión general.

## Trazabilidad

Una característica fundamental del agente es la trazabilidad.

Cada puntaje asignado debe estar acompañado por una justificación que permita comprender por qué se otorgó esa calificación.

De esta manera, otra persona puede revisar la evaluación y verificar la relación entre la evidencia encontrada, el criterio aplicado y el puntaje asignado.

## Consistencia

El agente debe aplicar los mismos criterios a todos los trabajos evaluados.

No debe modificar los criterios de evaluación según el estudiante ni introducir requisitos que no estén establecidos previamente en la consigna o en la rúbrica.

## Formato de salida

El resultado de la evaluación debe incluir:

- identificación del trabajo evaluado;
- puntaje obtenido en cada criterio;
- evidencia encontrada;
- justificación del puntaje;
- puntaje total;
- fortalezas;
- aspectos a mejorar;
- recomendaciones.

## Conclusión

Un agente evaluador basado en una rúbrica explícita puede contribuir a realizar evaluaciones más consistentes, transparentes y reproducibles.

La combinación de criterios previamente definidos, búsqueda de evidencias y justificación de los puntajes permite construir un proceso de evaluación en el que las decisiones del agente puedan ser revisadas y comprendidas.
