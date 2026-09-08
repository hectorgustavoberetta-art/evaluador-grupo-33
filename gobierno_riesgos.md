# Gobierno, riesgos y supervisión humana

## Alcance del agente

El sistema analiza repositorios académicos y genera una evaluación orientativa basada exclusivamente en la rúbrica, el system prompt y la evidencia textual encontrada. No reemplaza la decisión final del docente ni del equipo responsable de la corrección.

## Datos y permisos

El agente recibe los archivos que el usuario carga, o un archivo ZIP que contiene un repositorio. Para evaluarlo, lee únicamente archivos de texto con extensiones `.md`, `.txt`, `.py` y `.json`.

La aplicación también puede recibir la URL de un repositorio público de GitHub. En ese caso utiliza acceso de red únicamente para consultar información pública del repositorio y descargar su contenido mediante los servicios públicos de GitHub. Esta función no requiere permisos de escritura sobre el repositorio evaluado ni autoriza al agente a modificar, publicar o eliminar contenido en GitHub.

No necesita permisos para modificar el repositorio evaluado, publicar contenido, ejecutar sus programas ni acceder a cuentas externas. La clave de OpenAI se obtiene desde la variable de entorno `OPENAI_API_KEY` y no debe escribirse en el código ni subirse al repositorio.

## Flujo y límites de seguridad

- El ZIP está limitado a 50 MB.
- La extracción se realiza en un directorio temporal.
- Se rechazan rutas que intenten salir del directorio temporal.
- Se rechazan enlaces simbólicos.
- El código del repositorio evaluado no se ejecuta.
- Los archivos que no sean de texto compatible no se incorporan al análisis.
- Los archivos temporales deben eliminarse al finalizar la evaluación.

## Riesgos previsibles

### Información sensible
El contenido textual cargado se envía al modelo configurado para realizar la evaluación. No deben cargarse claves, contraseñas, datos personales innecesarios ni archivos confidenciales.

### Evidencia incompleta
El agente puede asignar un puntaje menor cuando la evidencia no está presente, aunque el trabajo haya sido realizado. La devolución debe señalar esa limitación y no presentar la ausencia de evidencia como prueba automática de fraude.

### Fallas del servicio
Una falla de la API, una clave inválida o un archivo ZIP dañado puede impedir la evaluación. En esos casos debe informarse el error y repetirse la ejecución; no debe generarse una calificación inventada.

### Variabilidad del modelo
Dos ejecuciones pueden producir diferencias menores. Por eso se registran las corridas, los tokens y la fecha, y se utiliza la calibración para controlar la consistencia.

### Detección de fraude
`POSIBLE FRAUDE` es una alerta que requiere revisión humana. `FRAUDE DETECTADO` solo corresponde cuando existe evidencia concreta de manipulación deliberada.

## Supervisión humana

La persona responsable debe:

1. verificar que el repositorio evaluado sea el correcto;
2. revisar la evidencia citada para cada dimensión;
3. controlar el puntaje total y el estado de fraude;
4. analizar las recomendaciones del agente;
5. resolver cualquier desacuerdo antes de comunicar la nota final.

El agente no tiene autoridad para aprobar, desaprobar ni comunicar por sí mismo una calificación definitiva. La decisión final queda a cargo del docente o responsable humano.

## Nivel de autonomía

El agente tiene autonomía limitada para leer los archivos cargados, aplicar la rúbrica y redactar una devolución. No puede modificar el trabajo evaluado, ejecutar su código, cambiar la rúbrica ni reemplazar la revisión humana.

## Plan de respuesta ante incidentes

Si se detecta una clave expuesta, un archivo sensible cargado por error o un resultado inconsistente:

1. detener la evaluación;
2. retirar o revocar la credencial comprometida;
3. eliminar el archivo sensible del flujo correspondiente;
4. revisar las corridas registradas;
5. repetir la evaluación cuando el entorno sea seguro;
6. documentar el incidente y la decisión adoptada.
