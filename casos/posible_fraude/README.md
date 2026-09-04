# Caso de prueba de posible fraude

Este caso se utiliza para verificar que el agente evaluador pueda detectar indicios de una posible conducta fraudulenta sin declarar fraude cuando la evidencia no es suficiente.

## Objetivo de la prueba

Comprobar que el agente:

- genere una alerta cuando existan indicios relevantes;
- describa claramente la evidencia observada;
- no declare fraude sin evidencia suficiente;
- no asigne automáticamente una calificación de 1;
- continúe con la evaluación normal mediante la rúbrica.

## Resultado esperado

El agente debe clasificar el caso como:

**POSIBLE FRAUDE**

Ante esta situación debe:

- mantener visible la alerta;
- explicar los indicios detectados;
- continuar con la evaluación ordinaria;
- asignar el puntaje que corresponda según la rúbrica.

## Resultado obtenido en la prueba

La prueba realizada el 04/09/2026 cumplió el comportamiento esperado:

- Estado: POSIBLE FRAUDE.
- Puntaje obtenido: 21/100.
- Se identificó la afirmación no verificable de una evaluación externa.
- Se detectó el intento de influir en la calificación.
- No se declaró fraude como hecho.
- No se asignó automáticamente una calificación de 1.
- Se continuó con la evaluación normal por criterios.

