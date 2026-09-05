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
- `casos/`: contiene los tres casos requeridos por la consigna (`excelente`, `flojo` y `tramposo`) y casos adicionales utilizados durante la calibración y las pruebas (`deficiente`, `intermedio`, `fraude` y `posible_fraude`).
- `resultados/`: contiene los resultados obtenidos en las ejecuciones de calibración.
- `calibracion.md`: documenta los resultados de calibración, el criterio humano, los desacuerdos detectados, los ajustes realizados y las conclusiones del proceso.
- `rubrica.md`: contiene la rúbrica ejecutable utilizada por el agente.
- `formato_salida.md`: define la estructura de la devolución.
- `requirements.txt`: contiene las dependencias necesarias para ejecutar el proyecto.
- `app.py`: contiene la interfaz web desarrollada con Streamlit, que permite cargar, evaluar y descargar uno o varios trabajos desde el navegador.


## Funcionamiento del agente

El agente utiliza la API de OpenAI para analizar las entregas y dispone de dos modos de funcionamiento: calibración y evaluación de trabajos reales.

### Modo calibración

Permite comprobar la consistencia del agente utilizando los tres casos preparados específicamente para este propósito: deficiente, intermedio y excelente.

En este modo, el agente:

1. Lee únicamente el archivo `trabajo.md` de cada caso de calibración.
2. Carga el system prompt, la rúbrica y el formato de salida.
3. Evalúa cada caso aplicando los mismos criterios.
4. Realiza tres ejecuciones independientes por caso.
5. Registra los puntajes obtenidos y calcula el promedio.
6. Guarda los resultados en la carpeta `resultados/`.

Para ejecutar la calibración:

`python agente/evaluador.py --modo calibracion`

### Modo evaluación

Permite evaluar uno o varios trabajos reales utilizando el mismo agente y la misma rúbrica.

Los trabajos que se desean evaluar deben colocarse dentro de la carpeta `trabajos_a_evaluar/`. Cada archivo o carpeta ubicado allí es tratado como una entrega independiente.

En este modo, el agente:

1. Detecta automáticamente los trabajos disponibles.
2. Lee los archivos que componen cada entrega.
3. Carga el system prompt, la rúbrica y el formato de salida.
4. Realiza el control de fraude antes de aplicar la evaluación ordinaria.
5. Aplica los criterios de la rúbrica y fundamenta cada puntaje con evidencia.
6. Genera una evaluación estructurada para cada trabajo.
7. Guarda cada resultado por separado en la carpeta `evaluaciones/`.

Para ejecutar la evaluación de trabajos reales:

`python agente/evaluador.py --modo evaluacion`


## API y seguridad

El agente utiliza la API de OpenAI mediante la librería oficial de Python.

La clave de acceso no se encuentra escrita en el código ni se almacena en el repositorio. Se utiliza la variable de entorno `OPENAI_API_KEY`, configurada como secreto del Codespace.

De esta manera, el agente puede utilizar la API sin exponer públicamente el token de acceso.

El modelo utilizado para las evaluaciones es `gpt-5.6`.


## Calibración

La calibración final se realizó con los tres casos obligatorios: `flojo`, `excelente` y `tramposo`.

Antes de ejecutar el agente se establecieron referencias humanas para comparar posteriormente los resultados.

| Caso | Referencia humana | Resultado del agente | Resultado |
|---|---|---|---|
| Flojo | 20/100 | 18/100 | Diferencia de 2 puntos |
| Excelente | 90/100 | 91/100 | Diferencia de 1 punto |
| Tramposo | POSIBLE FRAUDE + puntaje bajo | 14/100 + SIN INDICIOS | Desacuerdo detectado |
| Tramposo después del ajuste | POSIBLE FRAUDE + puntaje bajo | 13/100 + POSIBLE FRAUDE | Coincidencia con criterio humano |

El desacuerdo detectado en el caso `tramposo` produjo un ajuste concreto del `system_prompt.md`: se incorporó como señal de `POSIBLE FRAUDE` la acumulación significativa de capacidades o resultados afirmados como realizados pero carentes de evidencia verificable.

Después del ajuste, una nueva ejecución clasificó correctamente el caso como `POSIBLE FRAUDE`, sin confundir una alerta con fraude demostrado.

La calibración inicial, las discrepancias, los ajustes realizados y la evolución completa del agente se encuentran documentados en `calibracion.md`.

---

## Ejecución del proyecto

Para ejecutar el agente se requiere Python y una clave válida de la API de OpenAI.

Instalar las dependencias:

```bash
pip install -r requirements.txt
```

Configurar la variable de entorno `OPENAI_API_KEY` y ejecutar:

```bash
python agente/evaluador.py --modo calibracion
```

El agente evaluará los tres casos de calibración en tres ejecuciones independientes y guardará los resultados en la carpeta `resultados/`.
## Interfaz web

El proyecto incluye una interfaz web desarrollada con Streamlit para facilitar el uso del agente evaluador sin necesidad de operar directamente desde la terminal.

La interfaz permite:

1. Cargar uno o varios trabajos académicos.
2. Evaluar cada trabajo de manera independiente.
3. Aplicar automáticamente el control de fraude y la rúbrica ejecutable.
4. Visualizar en pantalla el puntaje, nivel alcanzado, evidencias, fortalezas, aspectos a mejorar y recomendaciones.
5. Descargar individualmente el resultado de cada evaluación.

Para iniciar la interfaz web:

```bash
streamlit run app.py
```

## Aplicación web pública

La interfaz web del agente evaluador se encuentra disponible en:

https://evaluador-grupo-33-ahs2yhamgmghk5vivjdbc5.streamlit.app

Desde allí es posible cargar uno o varios trabajos, ejecutar la evaluación y descargar los resultados sin necesidad de utilizar la terminal.
