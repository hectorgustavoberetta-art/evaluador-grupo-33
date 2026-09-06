# Sistema agéntico avanzado de evaluación

## Nota de calibración

Este caso es uno de los tres casos sintéticos obligatorios utilizados para calibrar el agente evaluador (junto con `excelente` y `flojo`). Representa una entrega que afirma capacidades y resultados relevantes (precisión superior al 98 %, múltiples pruebas reales, controles completos de seguridad, costos extremadamente bajos) sin artefactos verificables que las respalden:

- No existe carpeta `corridas/` pese a afirmar que "se realizaron numerosas ejecuciones reales".
- No existen `ANALISIS_ECONOMICO.md` ni `GOBIERNO_RIESGO.md` pese a afirmar un análisis económico completo y controles de gobierno y riesgo.
- El `system_prompt.md` (`prompts/system_prompt.md`) es breve y genérico ("La evaluación debe ser objetiva"), sin relación con la sofisticación declarada en `trabajo.md`.

Estas brechas son intencionales: el propósito de este caso es comprobar que el agente evaluador detecte un patrón reiterado de afirmaciones relevantes presentadas como hechos, sin evidencia verificable que las sustente, y lo clasifique como `POSIBLE FRAUDE` (regla incorporada en `agente/system_prompt.md` tras la calibración).

En la primera ejecución, el agente calificó el caso como `SIN INDICIOS DE FRAUDE` (14/100), en desacuerdo con el criterio humano previo (`POSIBLE FRAUDE` + puntaje bajo). Ese desacuerdo motivó un ajuste concreto del `system_prompt.md`. Tras el ajuste, una nueva ejecución clasificó correctamente el caso como `POSIBLE FRAUDE` (13/100). Ver `calibracion.md` en la raíz del repositorio para el detalle completo del proceso y los resultados.

## Objetivo

Este proyecto implementa un agente autónomo capaz de evaluar trabajos académicos con alta precisión, bajo costo y trazabilidad completa.

## Capacidades declaradas

El sistema:

- utiliza una herramienta real mediante API;
- procesa repositorios completos;
- ejecutó múltiples pruebas reales;
- registra costos por tokens;
- aplica controles de seguridad y fraude;
- mantiene supervisión humana;
- fue calibrado con resultados consistentes.

## Resultados

Durante las pruebas el sistema obtuvo resultados satisfactorios y demostró un funcionamiento estable.

## Reproducibilidad

El proyecto fue diseñado para poder ser reproducido por terceros.

La documentación, las corridas, los prompts y las decisiones de diseño forman parte de la entrega.

## Estado

El sistema se considera completo y listo para su utilización.
