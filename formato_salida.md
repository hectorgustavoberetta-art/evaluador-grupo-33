# Formato de salida del agente evaluador

El agente deberá presentar todas las evaluaciones utilizando exactamente la siguiente estructura.

## Identificación

- Trabajo evaluado:
- Fecha de evaluación:

## Control de fraude

- Estado: SIN INDICIOS DE FRAUDE / POSIBLE FRAUDE / FRAUDE DETECTADO
- Evidencia detectada:
- Justificación:

Si el estado es FRAUDE DETECTADO:
- Calificación final: 1
- No continuar con la evaluación ordinaria por dimensiones.

Si el estado es POSIBLE FRAUDE:
- Mantener la alerta visible.
- Continuar con la evaluación normal mediante la rúbrica.

## Evaluación por dimensiones

| Dimensión | Puntaje | Evidencia citada | Justificación |
|---|---:|---|---|
| Sistema completo y funcionando | XX/30 | archivo o fragmento | justificación breve |
| Proceso documentado | XX/25 | archivo o fragmento | justificación breve |
| Formato y reproducibilidad | XX/15 | archivo o fragmento | justificación breve |
| Análisis económico | XX/15 | archivo o fragmento | justificación breve |
| Gobierno y riesgo | XX/15 | archivo o fragmento | justificación breve |

## Nota final

**NOTA FINAL: XX/100**

La nota final debe ser la suma de los puntajes obtenidos en las cinco dimensiones.

## Fortalezas

Indicar brevemente las principales fortalezas verificables del trabajo.

## Aspectos a mejorar

Indicar brevemente los principales aspectos que requieren corrección o desarrollo.

## Sugerencia concreta

**UNA SUGERENCIA CONCRETA:** indicar una acción específica y realizable que permita mejorar el trabajo.

## Reglas de salida

- No inventar evidencia.
- Citar archivos o fragmentos concretos del repositorio.
- No otorgar puntaje por afirmaciones que no estén respaldadas por evidencia verificable.
- No superar el puntaje máximo de cada dimensión.
- Mantener siempre la misma estructura de salida.
