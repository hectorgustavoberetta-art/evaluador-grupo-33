# Calibración del agente evaluador

## 1. Objetivo

La calibración tuvo como objetivo comprobar que el agente evaluador pudiera distinguir trabajos de diferente calidad y asignar calificaciones coherentes con el criterio humano del grupo.

Se utilizaron tres casos de prueba: deficiente, intermedio y excelente. Cada caso fue evaluado tres veces para observar la estabilidad de los resultados.

## 2. Resultados obtenidos

| Caso | Ejecución 1 | Ejecución 2 | Ejecución 3 | Promedio |
|---|---:|---:|---:|---:|
| Deficiente | 43 | 42 | 41 | 42,00 |
| Intermedio | 68 | 75 | 68 | 70,33 |
| Excelente | 87 | 87 | 89 | 87,67 |

Los resultados conservaron en todas las pruebas el orden esperado:

**Deficiente < Intermedio < Excelente**

## 3. Criterio humano del grupo

Antes de analizar los resultados del agente, el criterio del grupo fue que:

- El caso deficiente debía obtener una calificación baja por presentar una metodología superficial, escasa fundamentación y falta de trazabilidad.
- El caso intermedio debía obtener una calificación media por desarrollar adecuadamente los conceptos principales, aunque sin evidencia técnica suficiente.
- El caso excelente debía obtener una calificación alta por presentar mayor profundidad, una arquitectura clara, trazabilidad, seguridad, reproducibilidad y una metodología más completa.

El orden producido por el agente coincidió con este criterio humano.

## 4. Desacuerdos y hallazgos

La calibración permitió identificar diferencias y aspectos a mejorar.

En el caso deficiente, los resultados fueron estables: 43, 42 y 41 puntos. El agente identificó correctamente la falta de aplicación estricta de la rúbrica, la ausencia de evidencia y el uso de criterios personales no regulados.

En el caso intermedio se observó una variación mayor: 68, 75 y 68 puntos. El agente reconoció correctamente que el trabajo presentaba una propuesta conceptualmente adecuada, pero carecía de código, resultados de ejecución y evidencia suficiente para demostrar una solución completamente funcional.

En el caso excelente se obtuvieron 87, 87 y 89 puntos. Aunque el grupo esperaba una calificación alta, el agente no otorgó el nivel máximo porque el caso describía archivos técnicos, pruebas y calibraciones que no estaban incorporados físicamente en la entrega utilizada en esa etapa.

Este último resultado fue especialmente útil porque permitió detectar que una descripción de una implementación no debe ser considerada equivalente a evidencia verificable de su existencia.

## 5. Ajustes realizados

A partir de las pruebas se realizaron ajustes progresivos en el agente y en los casos de calibración:

- Se reforzó la obligación de justificar los puntajes mediante evidencia concreta.
- Se estructuró la salida para mantener el mismo formato entre evaluaciones.
- Se incorporó un control específico de fraude y manipulación de las instrucciones.
- Se diferenciaron los estados SIN INDICIOS DE FRAUDE, POSIBLE FRAUDE y FRAUDE DETECTADO.
- Se mejoró la lectura de entregas para admitir archivos y estructuras de carpetas completas.
- Se incorporó compatibilidad de lectura UTF-8 y Windows cp1252.
- Se eliminó del README del caso excelente una indicación sobre la calificación esperada, porque podía interpretarse como un intento de influir sobre el evaluador.
- Se incorporaron al caso excelente artefactos técnicos reales para que las afirmaciones de implementación puedan ser verificadas.

## 6. Comprobación sobre una entrega organizada como repositorio

Como prueba adicional, el agente fue ejecutado sobre una carpeta que contenía varios archivos pertenecientes a una misma entrega.

El sistema recorrió la estructura, reunió los archivos admitidos, realizó el control de fraude, aplicó la rúbrica y generó automáticamente un archivo de evaluación.

La prueba permitió comprobar que el agente no se limita a evaluar un único archivo aislado, sino que puede analizar una entrega organizada como repositorio.

## 7. Conclusión

La calibración demostró que el agente distingue de manera consistente trabajos de diferente calidad y mantiene el orden esperado entre los tres niveles de prueba.

Las diferencias encontradas durante las ejecuciones fueron utilizadas para mejorar tanto las instrucciones del corrector como la calidad de los casos de prueba.

El proceso también permitió detectar problemas que una calibración basada únicamente en resultados esperados podría haber ocultado, especialmente la diferencia entre afirmar que un artefacto existe y proporcionar evidencia verificable de ese artefacto.

Los resultados completos de las ejecuciones se conservan en la carpeta `resultados/`.
