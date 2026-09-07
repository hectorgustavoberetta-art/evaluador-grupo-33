# Análisis económico del agente

## Objetivo

Medir el costo de uso del agente a partir de los tokens reales registrados en cada corrida. Las tarifas deben verificarse en la página oficial de precios de la API antes de presentar la entrega final:

https://openai.com/api/pricing/

## Datos medidos

Cada archivo de `corridas/` registra:

- modelo;
- tokens de entrada;
- tokens de salida;
- tokens totales;
- fecha de ejecución.

Mientras no existan corridas reales, no se deben completar valores manualmente.

## Fórmula

Si `Pi` es la tarifa de entrada en USD por millón de tokens y `Po` la tarifa de salida:

`Costo por corrida = (tokens_entrada / 1.000.000 × Pi) + (tokens_salida / 1.000.000 × Po)`

`Costo semanal = costo promedio por corrida × corridas por semana`

`Costo anual = costo semanal × 52`

## Procedimiento reproducible

1. Ejecutar al menos tres evaluaciones.
2. Descargar y conservar las corridas completas.
3. Calcular el promedio de tokens de entrada y salida.
4. Consultar las tarifas vigentes para el modelo utilizado.
5. Aplicar las fórmulas anteriores.
6. Registrar la frecuencia esperada de uso semanal.
7. Comparar el resultado con un modelo de menor costo y verificar si mantiene una calidad aceptable.

## Elección del modelo

El modelo actual se eligió por su capacidad para analizar repositorios completos y producir justificaciones trazables. La elección debe revisarse con una comparación real de calidad y costo; si un modelo más pequeño resuelve la tarea sin perder evidencia ni consistencia, debe preferirse ese modelo.

## Tabla para completar con evidencia

| Métrica | Valor |
|---|---:|
| Modelo utilizado | Pendiente de corridas |
| Promedio de tokens de entrada | Pendiente de corridas |
| Promedio de tokens de salida | Pendiente de corridas |
| Tarifa de entrada USD/millón | Pendiente de verificación |
| Tarifa de salida USD/millón | Pendiente de verificación |
| Costo promedio por corrida | Pendiente de cálculo |
| Corridas esperadas por semana | Definir por el equipo |
| Proyección semanal | Pendiente de cálculo |
| Proyección anual | Pendiente de cálculo |

No se deben presentar estimaciones como mediciones reales. Toda cifra final debe quedar respaldada por corridas y tarifas identificables.
