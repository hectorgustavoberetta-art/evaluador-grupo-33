# Decisiones e iteraciones del proyecto

## Objetivo

Construir un agente evaluador académico que analice un trabajo completo, aplique una rúbrica ejecutable, cite evidencia verificable, detecte posibles intentos de manipulación y entregue una devolución estructurada.

## Decisiones principales

### 1. Rúbrica ejecutable y salida estable

Se decidió separar la rúbrica (`rubrica.md`), el prompt del agente (`agente/system_prompt.md`) y el formato de salida (`formato_salida.md`). Esto permite evaluar siempre las mismas dimensiones y evita que el modelo invente criterios o puntajes.

### 2. Evaluación basada en evidencia

El agente fue instruido para no otorgar puntaje por afirmaciones que no estén respaldadas por archivos o fragmentos verificables del trabajo. Esta decisión responde directamente a la exigencia de trazabilidad de la consigna.

### 3. Control de fraude gradual

La calibración del caso tramposo mostró que una ausencia aislada de evidencia no alcanza para declarar fraude, pero que una acumulación significativa de afirmaciones no verificables puede justificar una alerta de `POSIBLE FRAUDE`. El prompt se ajustó para distinguir esa alerta de `FRAUDE DETECTADO`.

### 4. Interfaz web

Se agregó una interfaz Streamlit para que el agente pueda utilizarse sin operar directamente desde la terminal. También se corrigió la visualización de resultados duplicados.

### 5. Evaluación de repositorios completos

Se detectó que cargar archivos individuales no permitía evaluar correctamente un trabajo organizado como repositorio. Se incorporó la carga de un ZIP, extracción en un directorio temporal y evaluación de todo el contenido como una única entrega.

La extracción rechaza rutas que intenten salir del directorio temporal y enlaces simbólicos, y limita el tamaño del ZIP a 50 MB.

### 6. Registro de corridas

Se incorporó el guardado de cada corrida de calibración en `corridas/`, incluyendo fecha, entrada, salida, modelo y tokens. Los resultados reales deben generarse ejecutando el modo de calibración y conservarse sin editar manualmente.

### 7. Estructura canónica de prompts

La rúbrica exige una carpeta `prompts/` con `system_prompt.md` y `user_prompt.md`. Se creó allí una copia controlada del system prompt y se actualizó el código para leer esa ubicación como fuente canónica. El archivo anterior en `agente/system_prompt.md` se conserva por compatibilidad.

## Problemas detectados y estado

- La aplicación web inicialmente aceptaba únicamente archivos sueltos; se resolvió mediante carga de ZIP.
- La documentación inicialmente no explicaba cómo evaluar un repositorio real; se actualizó el README.
- La carpeta `corridas/` ahora tiene el mecanismo y las instrucciones, pero requiere una ejecución real con `OPENAI_API_KEY` para generar sus archivos.
- La calibración se conserva con los casos `deficiente`, `intermedio` y `excelente`, según la decisión del equipo.

## Evidencia técnica

- `af2d5b3`: carga y extracción segura de repositorios ZIP.
- `99017b2`: documentación del flujo de evaluación mediante ZIP.
- `ed98f36`: guardado de entrada, salida, fecha y tokens de cada corrida.
- `03f2fcc`: documentación del registro de corridas.
- `056178e`: documentación de la carpeta `corridas/`.
- `f705192`: creación de la carpeta documentada para conservar las corridas.

## Próximos pasos

1. Ejecutar la calibración real con la clave configurada.
2. Revisar que los archivos generados en `corridas/` contengan entrada, salida y fecha.
3. Subir esas corridas al repositorio como evidencia.
4. Verificar la estructura completa exigida por la rúbrica antes de la entrega final.
