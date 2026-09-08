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

Para este análisis se utilizaron las nueve corridas reales de calibración realizadas el 08/09/2026: tres correspondientes al caso `excelente`, tres al caso `flojo` y tres al caso `tramposo`.

## Fórmula

Si `Pi` es la tarifa de entrada en USD por millón de tokens y `Po` la tarifa de salida:

`Costo por corrida = (tokens_entrada / 1.000.000 × Pi) + (tokens_salida / 1.000.000 × Po)`

`Costo semanal = costo promedio por corrida × corridas por semana`

`Costo anual = costo semanal × 52`

## Procedimiento reproducible

1. Ejecutar al menos tres evaluaciones.
2. Conservar las corridas completas en la carpeta `corridas/`.
3. Calcular el promedio de tokens de entrada y salida.
4. Consultar las tarifas vigentes para el modelo utilizado.
5. Aplicar las fórmulas anteriores.
6. Definir un escenario de uso semanal para realizar la proyección.
7. Comparar el resultado con un modelo de menor costo y verificar si mantiene una calidad aceptable.

## Elección del modelo

El modelo utilizado en las corridas analizadas fue GPT-5.6 Sol. Se eligió por su capacidad para analizar repositorios completos y producir evaluaciones estructuradas con justificaciones trazables.

La elección del modelo debe revisarse periódicamente considerando calidad y costo. Si un modelo más pequeño permite realizar la misma tarea sin una pérdida significativa de consistencia, capacidad de análisis o trazabilidad de la evidencia, debe preferirse la alternativa de menor costo.

## Mediciones reales

Las nueve corridas de calibración quedaron conservadas en la carpeta `corridas/` y registran el modelo utilizado y el consumo real de tokens.

| Métrica | Valor |
|---|---:|
| Modelo utilizado | GPT-5.6 Sol |
| Corridas reales analizadas | 9 |
| Promedio de tokens de entrada | 8.153 |
| Promedio de tokens de salida | 1.543 |
| Promedio de tokens totales | 9.696 |
| Tarifa de entrada USD/millón | USD 4,00 |
| Tarifa de salida USD/millón | USD 20,00 |
| Costo promedio por corrida | USD 0,0635 |
| Escenario de uso supuesto | 10 evaluaciones por semana |
| Proyección semanal | USD 0,635 |
| Proyección anual | USD 33,00 |

## Fuente de tarifas

Tarifas consultadas el 08/09/2026 en la documentación oficial de OpenAI para GPT-5.6 Sol:

- Entrada: USD 4,00 por millón de tokens.
- Salida: USD 20,00 por millón de tokens.

Los valores corresponden a la tarifa vigente al momento de realizar este análisis y deben verificarse nuevamente si el sistema se utiliza en el futuro.

## Cálculo

El costo promedio se calculó sobre las nueve corridas reales de calibración conservadas en la carpeta `corridas/`.

Promedio de entrada: 8.153 tokens.

Promedio de salida: 1.543 tokens.

Costo aproximado por evaluación:

`(8.153 / 1.000.000 × 4) + (1.543 / 1.000.000 × 20) = USD 0,0635 por corrida`

Para realizar una proyección económica se adopta un escenario supuesto de 10 evaluaciones semanales. Este valor no representa una medición de uso real, sino un escenario de referencia para estimar el costo operativo.

Costo semanal estimado:

`USD 0,0635 × 10 = USD 0,635 por semana`

Proyección anual:

`USD 0,635 × 52 = aproximadamente USD 33,00 por año`

## Interpretación

El costo variable de utilización del agente resulta bajo para el escenario analizado. Con un costo promedio aproximado de USD 0,0635 por evaluación, incluso un escenario de 10 evaluaciones semanales produciría un costo anual aproximado de USD 33,00.

El principal factor económico es el consumo de tokens de cada repositorio evaluado. Trabajos más extensos pueden incrementar el número de tokens de entrada y, por lo tanto, el costo de cada corrida.

## Criterio de selección económica

La selección del modelo no debe basarse únicamente en su capacidad técnica. Debe buscarse el modelo de menor costo que mantenga un nivel aceptable de calidad, consistencia y trazabilidad.

Como mejora futura, corresponde realizar una comparación controlada utilizando los mismos casos de calibración con un modelo de menor costo y comparar:

- puntajes obtenidos;
- consistencia entre ejecuciones;
- detección del caso tramposo;
- calidad de las evidencias citadas;
- costo por corrida.

Si el modelo de menor costo mantiene resultados equivalentes, debería preferirse para el uso habitual del agente.

## Conclusión

El análisis se basa en mediciones reales obtenidas durante nueve corridas de calibración y diferencia expresamente los datos medidos de las proyecciones de uso.

Las cifras de costo semanal y anual son estimaciones construidas sobre un escenario supuesto de 10 evaluaciones por semana. Las tarifas de la API deberán verificarse nuevamente antes de utilizar estos valores para una decisión económica futura.
