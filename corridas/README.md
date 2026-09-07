# Corridas de calibración

Esta carpeta conserva las ejecuciones reales del modo de calibración.

Cada archivo debe incluir:

- caso evaluado;
- número de ejecución;
- fecha y hora;
- entrada completa;
- salida del agente;
- modelo y tokens utilizados.

Los archivos se generan automáticamente al ejecutar:

```bash
python agente/evaluador.py --modo calibracion
```

No se deben inventar ni editar manualmente los resultados. Después de ejecutar la calibración, subir los archivos generados a esta carpeta para conservar la evidencia del proceso.