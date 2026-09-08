# Corrida de calibración

- Caso: flojo
- Ejecución: 2
- Fecha y hora: 2026-09-08T17:06:14-03:00
- Modelo: gpt-5.6-sol
- Tokens de entrada: 3775
- Tokens de salida: 1278
- Tokens totales: 5053

## Entrada



===== ARCHIVO: DECISIONES.md =====

# Decisiones del proyecto

Se decidió utilizar inteligencia artificial porque puede facilitar la corrección de trabajos.

Durante el desarrollo se realizaron algunos cambios para mejorar la propuesta.

La versión presentada es la que se consideró más adecuada.


===== ARCHIVO: README.md =====

# Sistema agéntico para asistencia académica

## Objetivo

Este proyecto propone utilizar inteligencia artificial para analizar trabajos académicos y generar una devolución automática.

## Funcionamiento general

El sistema recibe el contenido de un trabajo, realiza un análisis general y genera una calificación acompañada de observaciones.

## Uso

El trabajo principal se encuentra documentado en `trabajo.md`.

## Contenido del repositorio

- `README.md`: descripción general del proyecto.
- `trabajo.md`: explicación del sistema propuesto.

## Estado del proyecto

Se presenta una versión inicial del sistema para su evaluación.


===== ARCHIVO: corridas/corrida_01/entrada.md =====

# Entrada

Trabajo académico sobre inteligencia artificial.


===== ARCHIVO: corridas/corrida_01/salida.md =====

# Salida

El trabajo fue analizado y se considera adecuado.


===== ARCHIVO: prompts/system_prompt.md =====

# System Prompt

Sos un asistente que analiza trabajos académicos.

Leé el trabajo presentado y generá una devolución indicando si el contenido es adecuado.


===== ARCHIVO: trabajo.md =====

# Trabajo práctico — Agente evaluador

## Introducción

La inteligencia artificial puede utilizarse para corregir trabajos de estudiantes de forma automática.

El objetivo es crear un agente que lea un trabajo y diga si está bien o mal.

## Desarrollo

El agente recibe el trabajo del alumno y lo analiza.

Después de leerlo puede colocar una nota según lo que considere correcto.

Para hacer la evaluación puede mirar una rúbrica, aunque también puede utilizar su propio criterio para decidir la calidad general del trabajo.

El procedimiento sería:

1. Leer el trabajo.
2. Revisar si está bien.
3. Poner una nota.
4. Informar el resultado.

## Evaluación

El agente puede indicar si el trabajo es bueno, regular o malo.

Si encuentra errores puede mencionarlos en la devolución. No es necesario explicar cada puntaje ni indicar exactamente qué parte del trabajo permitió tomar la decisión.

## Resultado

El resultado podría ser, por ejemplo:

“Trabajo aprobado. El contenido es adecuado y cumple en general con lo solicitado.”

## Conclusión

La inteligencia artificial puede ayudar a los profesores porque permite corregir trabajos más rápidamente.

## Costos

El uso de inteligencia artificial puede generar costos asociados al consumo de tokens. Se intentará utilizar un modelo que no resulte demasiado costoso.

## Riesgos y supervisión

El sistema puede cometer errores, por lo que sería conveniente que una persona revise algunos resultados antes de utilizarlos.


## Salida del agente

## Identificación

- Trabajo evaluado: Sistema agéntico para asistencia académica
- Fecha de evaluación: 08/09/2026

## Control de fraude

- Estado: SIN INDICIOS DE FRAUDE
- Evidencia detectada: No se encontraron instrucciones destinadas a alterar la evaluación, falsificación de resultados ni afirmaciones reiteradas de capacidades implementadas sin respaldo.
- Justificación: La entrega se presenta explícitamente como una versión inicial y sus limitaciones resultan visibles en los archivos del repositorio.

## Evaluación por dimensiones

| Dimensión | Puntaje | Evidencia citada | Justificación |
|---|---:|---|---|
| Sistema completo y funcionando | 7/30 | `README.md`, sección “Objetivo”; `prompts/system_prompt.md`; `corridas/corrida_01/entrada.md` y `salida.md`; `trabajo.md`, sección “Riesgos y supervisión” | Existe un objetivo, un system prompt y una corrida básica. Sin embargo, falta el user prompt, no hay herramientas o conectores reales, la salida no presenta una estructura de evaluación suficiente y la supervisión humana es vaga. La única corrida no demuestra de manera verificable un funcionamiento efectivo: contiene una entrada genérica y una respuesta sin nota, criterios ni evidencia. |
| Proceso documentado | 3/25 | `DECISIONES.md`: “Durante el desarrollo se realizaron algunos cambios para mejorar la propuesta” y “La versión presentada es la que se consideró más adecuada” | La documentación afirma que hubo cambios, pero no identifica iteraciones, errores, decisiones concretas, modificaciones de alcance ni aprendizajes. No es posible reconstruir la evolución real del sistema. |
| Formato y reproducibilidad | 4/15 | `README.md`; `prompts/system_prompt.md`; `corridas/corrida_01/entrada.md` y `salida.md`; `DECISIONES.md` | Están presentes el README, la carpeta de prompts, un system prompt, una corrida y el archivo de decisiones. Faltan `prompts/user_prompt.md`, tres corridas reales con fecha y procedimientos suficientes de instalación o ejecución. El README solo remite a `trabajo.md`, por lo que un tercero no puede reproducir el sistema. |
| Análisis económico | 2/15 | `trabajo.md`, sección “Costos”: “El uso de inteligencia artificial puede generar costos asociados al consumo de tokens” y “Se intentará utilizar un modelo que no resulte demasiado costoso” | Solo se mencionan genéricamente tokens y costos. No se identifica el modelo, no se estiman tokens de entrada o salida, no se calcula el costo por corrida ni se realizan proyecciones semanales o anuales. Tampoco se compara o justifica verificablemente la elección del modelo. |
| Gobierno y riesgo | 4/15 | `trabajo.md`, sección “Riesgos y supervisión”: “El sistema puede cometer errores” y “sería conveniente que una persona revise algunos resultados” | Se reconoce un riesgo general y se propone cierta revisión humana. No se definen sistemas y datos utilizados, permisos, fallas específicas, respuesta ante errores, nivel de autonomía, decisiones que requieren revisión ni responsable de validar el resultado final. |

## Nota final

**NOTA FINAL: 20/100**

## Fortalezas

- El objetivo general del sistema está expresado en `README.md`.
- Existe un system prompt verificable en `prompts/system_prompt.md`.
- Se incluye una corrida básica con entrada y salida.
- El trabajo reconoce que el agente puede equivocarse y que corresponde alguna intervención humana.

## Aspectos a mejorar

- Implementar y demostrar un sistema ejecutable con una herramienta o API real.
- Incorporar el user prompt y una salida estructurada basada exclusivamente en una rúbrica.
- Documentar iteraciones, errores y decisiones concretas en `DECISIONES.md`.
- Agregar al menos tres corridas fechadas, completas y reproducibles.
- Desarrollar cálculos de tokens, costos y proyecciones de uso.
- Definir permisos, límites de autonomía, mecanismos de fallo y responsable de aprobación final.

## Sugerencia concreta

**UNA SUGERENCIA CONCRETA:** implementar una versión ejecutable que aplique una rúbrica fija y guardar tres corridas fechadas con entrada completa, salida estructurada, modelo utilizado, consumo de tokens y costo; luego documentar en `DECISIONES.md` qué falló y qué se modificó entre cada corrida.
