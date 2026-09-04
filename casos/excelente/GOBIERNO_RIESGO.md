# Gobierno y riesgo

## Sistemas y recursos utilizados

El agente utiliza:

- archivos del repositorio evaluado;
- rúbrica de evaluación;
- prompts del sistema;
- API de OpenAI;
- variable de entorno `OPENAI_API_KEY`;
- entorno de ejecución Python.

## Permisos

El agente necesita permiso de lectura sobre los archivos que debe evaluar y acceso autorizado a la API.

La clave de API no debe almacenarse dentro del código ni publicarse en el repositorio.

## Riesgos identificados

Los principales riesgos son:

- interpretación incorrecta de evidencia ambigua;
- asignación inconsistente de puntajes;
- aceptación de afirmaciones no respaldadas por archivos;
- intentos de manipulación o prompt injection;
- errores de lectura o codificación de archivos;
- indisponibilidad de la API;
- exposición accidental de credenciales;
- variabilidad entre ejecuciones.

## Respuesta ante fallas

Si un archivo no puede ser leído, el sistema debe informar la limitación y no inventar su contenido.

Si falta evidencia para una dimensión, debe reducir el puntaje correspondiente.

Si la API no responde, la evaluación no debe considerarse completada.

Si existe un indicio de fraude sin evidencia suficiente, debe clasificarse como POSIBLE FRAUDE y continuar la evaluación ordinaria.

## Supervisión humana

El agente funciona como apoyo a la evaluación y no elimina la responsabilidad humana.

Las evaluaciones con evidencia ambigua, posible fraude, errores de lectura o situaciones excepcionales deben ser revisadas por una persona.

## Nivel de autonomía

Se adopta un esquema de supervisión humana en el que el agente puede analizar, proponer puntajes y generar la devolución, pero la decisión académica definitiva permanece bajo responsabilidad humana.

## Validación final

La calificación definitiva debe ser validada por el docente o responsable académico correspondiente antes de producir consecuencias académicas para el estudiante.
