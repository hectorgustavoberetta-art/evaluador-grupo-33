# evaluador-grupo-33

## Integrantes

- HECTOR GUSTAVO BERETTA
- ELIANA ANDROSZCZUK
- DIEGO GONZALEZ
- AGUSTIN POSELSKI


## Descripción del proyecto

Este repositorio contiene un agente evaluador desarrollado para el parcial de la materia Programación de y con Agentes de IA del MBA UCEMA.

El agente tiene como objetivo evaluar trabajos académicos de manera objetiva, consistente y trazable, utilizando una rúbrica ejecutable como único criterio de evaluación.

El sistema lee los archivos de una entrega, analiza las evidencias disponibles, asigna puntajes por criterio, calcula el puntaje total y genera una devolución estructurada con fortalezas, aspectos a mejorar y recomendaciones.


## Estructura del repositorio

- `agente/`: contiene el código del evaluador y su system prompt.
- `casos/`: contiene los tres casos utilizados para calibración: deficiente, intermedio y excelente.
- `resultados/`: contiene los resultados obtenidos en las ejecuciones de calibración.
- `rubrica.md`: contiene la rúbrica ejecutable utilizada por el agente.
- `formato_salida.md`: define la estructura de la devolución.
- `requirements.txt`: contiene las dependencias necesarias para ejecutar el proyecto.


## Funcionamiento del agente

El agente utiliza la API de OpenAI para analizar las entregas.

El proceso de evaluación es el siguiente:

1. Lee los archivos que componen la entrega.
2. Carga el system prompt del agente.
3. Carga la rúbrica de evaluación.
4. Aplica cada criterio de la rúbrica al trabajo presentado.
5. Identifica evidencias que fundamentan cada puntaje.
6. Genera una evaluación estructurada según el formato de salida definido.
7. Realiza ejecuciones repetidas sobre los casos de calibración para analizar la consistencia de los resultados.


## API y seguridad

El agente utiliza la API de OpenAI mediante la librería oficial de Python.

La clave de acceso no se encuentra escrita en el código ni se almacena en el repositorio. Se utiliza la variable de entorno `OPENAI_API_KEY`, configurada como secreto del Codespace.

De esta manera, el agente puede utilizar la API sin exponer públicamente el token de acceso.

El modelo utilizado para las evaluaciones es `gpt-5.6`.


## Calibración

Para comprobar el comportamiento y la consistencia del agente se utilizaron tres casos de prueba con diferentes niveles de calidad.

Cada caso fue evaluado tres veces.

Resultados obtenidos:

| Caso | Ejecución 1 | Ejecución 2 | Ejecución 3 | Promedio |
|---|---:|---:|---:|---:|
| Deficiente | 43 | 42 | 41 | 42,00/100 |
| Intermedio | 68 | 75 | 68 | 70,33/100 |
| Excelente | 87 | 87 | 89 | 87,67/100 |

Los resultados muestran una separación clara entre los tres casos de calibración. Las ejecuciones repetidas permiten además observar la variabilidad propia de la evaluación y analizar la consistencia del agente.


## Ejecución del proyecto

Para ejecutar el agente se requiere Python y una clave válida de la API de OpenAI.

Instalar las dependencias:

```bash
pip install -r requirements.txt
```

Configurar la variable de entorno `OPENAI_API_KEY` y ejecutar:

```bash
python agente/evaluador.py
```

El agente evaluará los tres casos de calibración en tres ejecuciones independientes y guardará los resultados en la carpeta `resultados/`.