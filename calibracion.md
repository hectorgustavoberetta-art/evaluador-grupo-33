# Calibración del agente evaluador

## 1. Objetivo

La calibración tuvo como objetivo comprobar que el agente evaluador pudiera distinguir trabajos de diferente calidad, asignar calificaciones coherentes con el criterio humano y detectar situaciones que requirieran una alerta por posible manipulación.

El proceso se realizó de manera iterativa. Se conservaron los resultados de una calibración inicial y posteriormente se efectuó una calibración final utilizando los tres casos exigidos para el parcial: `flojo`, `excelente` y `tramposo`.

---

## 2. Calibración inicial

En una etapa anterior se utilizaron los casos `deficiente`, `intermedio` y `excelente`, evaluados tres veces cada uno.

| Caso | Ejecución 1 | Ejecución 2 | Ejecución 3 | Promedio |
|---|---:|---:|---:|---:|
| Deficiente | 43 | 42 | 41 | 42,00 |
| Intermedio | 68 | 75 | 68 | 70,33 |
| Excelente | 87 | 87 | 89 | 87,67 |

Esta etapa permitió comprobar inicialmente que el agente podía diferenciar niveles de calidad y también permitió detectar problemas relacionados con la evidencia verificable, el formato de salida, la lectura de repositorios y el control de fraude.

Los resultados históricos se conservan como evidencia del proceso de evolución del proyecto.

---

## 3. Ajustes realizados durante el desarrollo

A partir de las distintas pruebas se realizaron, entre otros, los siguientes ajustes:

- obligación de justificar los puntajes mediante evidencia concreta;
- utilización de una salida estructurada y consistente;
- lectura recursiva de entregas organizadas como repositorios;
- compatibilidad con archivos UTF-8 y Windows cp1252;
- alineación de la evaluación con las cinco dimensiones oficiales;
- incorporación de los estados `SIN INDICIOS DE FRAUDE`, `POSIBLE FRAUDE` y `FRAUDE DETECTADO`;
- eliminación de indicaciones que pudieran influir artificialmente sobre la nota esperada;
- incorporación de artefactos técnicos y corridas reales;
- registro del modelo y consumo real de tokens;
- incorporación de análisis económico y documentación de gobierno y riesgo.

---

## 4. Calibración final con criterio humano previo

Para evitar ajustar las notas humanas después de conocer la respuesta del agente, se estableció previamente una referencia humana para los tres casos obligatorios.

### Caso flojo

Referencia humana previa: **20/100**.

El caso presenta una propuesta conceptual básica, pero carece de una implementación completa, herramienta real demostrada, tres corridas reproducibles, análisis económico cuantificado y documentación suficiente de gobierno y riesgo.

Resultado del agente: **18/100**.

Diferencia respecto del criterio humano: **2 puntos**.

El agente identificó correctamente las principales carencias del trabajo y lo clasificó como `SIN INDICIOS DE FRAUDE`.

### Caso excelente

Referencia humana previa: **90/100**.

El caso contiene implementación técnica, prompts, integración mediante API, lectura de repositorios, tres corridas reales, registro de tokens, análisis económico, documentación del proceso y gobierno y riesgo.

Resultado del agente: **91/100**.

Diferencia respecto del criterio humano: **1 punto**.

El agente reconoció correctamente la calidad general del sistema y también identificó oportunidades concretas de mejora en reproducibilidad y documentación.

### Caso tramposo

El criterio humano previo fue clasificarlo como **POSIBLE FRAUDE**, acompañado de un puntaje bajo, debido a la acumulación de afirmaciones relevantes no respaldadas por evidencia verificable.

Entre esas afirmaciones se encontraban la utilización de una API real, múltiples pruebas reales, precisión superior al 98 %, costos extremadamente bajos y controles completos de seguridad, sin artefactos suficientes que permitieran comprobarlas.

En la primera ejecución el agente otorgó **14/100**, pero clasificó el caso como `SIN INDICIOS DE FRAUDE`.

El puntaje fue coherente con el criterio humano, pero se detectó un desacuerdo en el control de fraude.

---

## 5. Desacuerdo detectado y ajuste del corrector

El análisis del caso `tramposo` mostró que el agente trataba correctamente las afirmaciones sin evidencia como faltantes de respaldo y reducía los puntajes correspondientes, pero no consideraba que una acumulación significativa de esas afirmaciones pudiera justificar una alerta.

Se modificó el `system_prompt.md` para establecer que un patrón reiterado de capacidades, resultados, métricas, herramientas, costos o controles presentados como demostrados, pero sin evidencia verificable, debe ser considerado como posible indicio de fraude.

También se estableció expresamente que una ausencia aislada de evidencia no constituye por sí sola posible fraude.

Después del ajuste se ejecutó nuevamente el caso `tramposo`.

Resultado posterior:

- Estado: **POSIBLE FRAUDE**.
- Nota: **13/100**.
- El agente continuó correctamente con la evaluación ordinaria.
- No declaró `FRAUDE DETECTADO`, porque no existía evidencia suficiente para afirmar una falsificación deliberada.

El resultado posterior coincidió con el criterio humano establecido previamente.

---

## 6. Comparación final

| Caso | Referencia humana previa | Resultado del agente | Resultado de calibración |
|---|---|---|---|
| Flojo | 20/100 | 18/100 | Diferencia de 2 puntos |
| Excelente | 90/100 | 91/100 | Diferencia de 1 punto |
| Tramposo | POSIBLE FRAUDE + puntaje bajo | Inicial: 14/100 + SIN INDICIOS | Se detectó desacuerdo |
| Tramposo después del ajuste | POSIBLE FRAUDE + puntaje bajo | 13/100 + POSIBLE FRAUDE | Coincidencia con criterio humano |

---

## 7. Conclusión

La calibración final mostró una alta proximidad entre el criterio humano previo y las calificaciones producidas por el agente en los casos `flojo` y `excelente`.

El caso `tramposo` permitió identificar un desacuerdo real que no había sido previsto adecuadamente en las instrucciones del corrector. Ese hallazgo produjo una modificación concreta del `system_prompt.md` y una nueva ejecución posterior.

La segunda evaluación del caso `tramposo` confirmó que el ajuste permitió detectar correctamente una situación de `POSIBLE FRAUDE` sin convertir automáticamente una sospecha en fraude demostrado.

De esta manera, la calibración no se utilizó únicamente para mostrar resultados esperados, sino como un proceso de comparación entre criterio humano y comportamiento del agente, identificación de desacuerdos, modificación del corrector y comprobación posterior del efecto del cambio.

El historial de commits y los resultados conservados permiten reconstruir la evolución del agente y las decisiones adoptadas durante su desarrollo.
