# Rúbrica ejecutable del Trabajo Final — v2

## Objetivo

Esta rúbrica convierte en criterios operativos la rúbrica oficial del Trabajo Final de la materia Programación de y con Agentes de IA · MBA UCEMA · 2026 2T.

El agente debe evaluar únicamente con evidencia verificable presente en el repositorio.

Puntaje máximo total: 100 puntos.

---

## Dimensión 1 — Sistema completo y funcionando
Puntaje máximo: 30 puntos

### Evidencia exigida
Debe existir evidencia verificable de:
- objetivo claro del sistema;
- system prompt y user prompt;
- al menos una herramienta, API, conector, archivo, planilla o calendario utilizado de manera real;
- salida estructurada;
- definición de supervisión humana;
- funcionamiento efectivo del sistema.

### Escala

- 27–30: El sistema está completo, funciona y todos los componentes exigidos son verificables en el repositorio.
- 21–26: El sistema funciona y cumple la mayor parte de los requisitos, con omisiones menores o evidencia incompleta en algún componente.
- 12–20: El sistema presenta implementación parcial, funcionamiento limitado o faltan varios componentes relevantes.
- 0–11: No existe evidencia suficiente de un sistema agéntico completo y funcionando.

### Ejemplo de nivel alto
El repositorio contiene prompts completos, herramienta real implementada, salida estructurada, instrucciones de uso y evidencia de ejecución.

### Ejemplo de nivel bajo
El README describe un agente, pero no existen prompts, código ejecutable, herramienta real ni evidencia de funcionamiento.

---

## Dimensión 2 — Proceso documentado
Puntaje máximo: 25 puntos

### Evidencia exigida
Debe existir documentación verificable del proceso de construcción:
- iteraciones;
- problemas encontrados;
- errores;
- decisiones tomadas;
- cambios de alcance;
- aprendizajes;
- evolución del sistema.

El archivo principal esperado para esta evidencia es `DECISIONES.md` o documentación equivalente claramente identificable.

### Escala

- 23–25: El proceso está documentado en profundidad, con iteraciones reales, fallas, decisiones y evolución claramente trazables.
- 18–22: Existe una buena documentación del proceso, aunque algunos cambios, errores o decisiones no están completamente desarrollados.
- 10–17: La documentación del proceso es parcial, superficial o principalmente descriptiva.
- 0–9: No existe evidencia suficiente del proceso real de construcción.

### Ejemplo de nivel alto
`DECISIONES.md` muestra versiones sucesivas del sistema, qué falló en cada etapa, qué se modificó y por qué.

### Ejemplo de nivel bajo
El repositorio presenta solamente el producto final y afirma que “funciona correctamente” sin mostrar cómo fue construido.

---

## Dimensión 3 — Formato y reproducibilidad
Puntaje máximo: 15 puntos

### Evidencia exigida
Debe verificarse:
- `README.md`;
- carpeta `prompts/`;
- `system_prompt.md`;
- `user_prompt.md`;
- carpeta `corridas/`;
- al menos tres ejecuciones reales con entrada, salida y fecha;
- `DECISIONES.md`;
- instrucciones suficientes para que un tercero pueda reconstruir lo realizado.

### Escala

- 14–15: La estructura obligatoria está completa y un tercero puede reproducir y reconstruir las ejecuciones sin ambigüedades.
- 11–13: La estructura es mayormente correcta, con omisiones menores que no impiden comprender el funcionamiento.
- 6–10: Existen varios elementos, pero faltan archivos, corridas o instrucciones relevantes.
- 0–5: La estructura obligatoria no se respeta o el trabajo no resulta reproducible.

### Ejemplo de nivel alto
Las tres corridas incluyen entrada, salida y fecha, y el README explica con precisión cómo ejecutar o reconstruir el sistema.

### Ejemplo de nivel bajo
Se afirma que hubo pruebas, pero no existen corridas guardadas ni instrucciones para reproducirlas.

---

## Dimensión 4 — Análisis económico
Puntaje máximo: 15 puntos

### Evidencia exigida
Debe existir:
- estimación o medición de tokens de entrada y salida;
- costo aproximado por corrida;
- proyección de costos de uso real, por ejemplo semanal y anual;
- identificación del modelo utilizado;
- justificación de la elección del modelo;
- consideración del principio de utilizar el modelo más pequeño que resuelva adecuadamente la tarea.

### Escala

- 14–15: El análisis económico es completo, verificable y conecta costos, frecuencia de uso y elección de modelo.
- 11–13: El análisis es adecuado, aunque alguna estimación, proyección o justificación podría ser más precisa.
- 6–10: Existe un análisis parcial de costos o tokens, pero faltan componentes relevantes.
- 0–5: No existe análisis económico suficiente o solo se mencionan costos de manera genérica.

### Ejemplo de nivel alto
Se informa consumo de tokens por corrida, costo unitario, proyección semanal y anual y se justifica el modelo elegido frente a alternativas.

### Ejemplo de nivel bajo
Solo se afirma que “usar la API tiene un costo” sin cálculos ni estimaciones.

---

## Dimensión 5 — Gobierno y riesgo
Puntaje máximo: 15 puntos

### Evidencia exigida
Debe documentarse:
- qué sistemas, datos o recursos utiliza el agente;
- qué permisos necesita;
- riesgos previsibles;
- qué puede salir mal;
- qué ocurre cuando falla;
- qué decisiones requieren revisión humana;
- nivel de autonomía o supervisión;
- quién valida o firma el resultado final.

### Escala

- 14–15: Los riesgos, permisos, fallas y controles humanos están claramente identificados y existe una estrategia concreta de supervisión.
- 11–13: El gobierno y los riesgos están adecuadamente considerados, con algunas omisiones menores.
- 6–10: Se mencionan riesgos y supervisión, pero de manera parcial o poco operativa.
- 0–5: No existe una definición suficiente de gobierno, permisos, riesgos o supervisión humana.

### Ejemplo de nivel alto
El trabajo identifica accesos, riesgos, límites de autonomía, puntos de revisión humana y responsable final de aprobación.

### Ejemplo de nivel bajo
El trabajo afirma que el agente es “autónomo” sin explicar permisos, controles, fallas posibles ni responsable humano.

---

## Reglas generales de evaluación

1. Evaluar las cinco dimensiones de manera independiente.
2. No superar el puntaje máximo de cada dimensión.
3. Utilizar exclusivamente evidencia verificable presente en el repositorio.
4. Citar el archivo o fragmento que respalda cada puntaje.
5. Las afirmaciones no respaldadas por artefactos verificables no deben sumar puntaje.
6. Si falta evidencia, indicarlo expresamente y reducir el puntaje correspondiente.
7. No inventar evidencia ni completar información ausente mediante supuestos.
8. El puntaje total es la suma de las cinco dimensiones.
9. Un proceso honesto con fallas documentadas puede obtener mejor evaluación que una presentación aparentemente perfecta sin evidencia.
10. Si el README afirma capacidades que los archivos no demuestran, señalar la inconsistencia.
11. La evaluación debe mantener el mismo formato en cada ejecución.
12. La devolución debe incluir una sugerencia concreta de mejora basada en la evidencia encontrada.

## Puntaje total

Puntaje máximo: 100 puntos.
