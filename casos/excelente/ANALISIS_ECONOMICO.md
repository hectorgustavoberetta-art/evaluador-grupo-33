# Análisis económico

## Modelo utilizado

Las ejecuciones reales se realizaron solicitando `gpt-5.6` mediante la API de OpenAI. La respuesta de la API identificó al modelo efectivamente utilizado como `gpt-5.6-sol`.

La elección del modelo sigue el criterio de utilizar el modelo de menor costo que permita aplicar adecuadamente una rúbrica compleja, analizar evidencia distribuida en un repositorio y producir una evaluación estructurada. La conveniencia de migrar a un modelo de menor costo deberá comprobarse mediante calibración antes de adoptarlo.

## Componentes del costo

El costo de cada corrida depende principalmente de:

- tokens de entrada;
- tokens de salida;
- precio vigente del modelo;
- cantidad de evaluaciones realizadas.

Para estas mediciones se utilizaron como referencia las tarifas vigentes verificadas para el modelo utilizado:

- entrada: USD 4 por millón de tokens;
- salida: USD 20 por millón de tokens.

Los precios pueden cambiar y deben verificarse nuevamente antes de una utilización futura.

## Fórmula de cálculo

Costo de entrada = (tokens de entrada / 1.000.000) × USD 4.

Costo de salida = (tokens de salida / 1.000.000) × USD 20.

Costo total = costo de entrada + costo de salida.

## Mediciones reales

Se realizaron tres ejecuciones reales y se conservaron sus salidas y metadatos en `corridas/`.

| Corrida | Tokens entrada | Tokens salida | Tokens totales | Costo estimado |
|---|---:|---:|---:|---:|
| 01 | 12.258 | 2.049 | 14.307 | USD 0,0900 |
| 02 | 13.594 | 2.004 | 15.598 | USD 0,0945 |
| 03 | 14.879 | 1.774 | 16.653 | USD 0,0950 |
| Promedio | 13.577 | 1.942 | 15.519 | USD 0,0932 |

El costo promedio observado es, por lo tanto, de aproximadamente **USD 0,093 por evaluación**.

## Proyección de uso

Como escenario ilustrativo, si el sistema realizara 10 evaluaciones por semana:

Costo semanal estimado:

USD 0,0932 × 10 = **USD 0,932 por semana**.

Costo anual estimado:

USD 0,932 × 52 = **USD 48,46 por año**.

Esta proyección es un escenario de referencia y no representa una frecuencia de uso observada.

## Observación sobre el crecimiento del contexto

Se observó un aumento de tokens de entrada entre las tres corridas: 12.258, 13.594 y 14.879 tokens.

Esto ocurre porque el evaluador realiza una lectura recursiva del repositorio y las nuevas corridas guardadas pasan a formar parte del material leído en ejecuciones posteriores.

Este comportamiento muestra que el costo no necesariamente permanece constante cuando el repositorio aumenta de tamaño. Una optimización futura consiste en excluir de la entrada aquellos resultados históricos que no sean necesarios para evaluar el trabajo actual.

## Criterio de selección del modelo

El criterio económico adoptado es utilizar el modelo de menor costo que mantenga una calidad suficiente y consistente en la aplicación de la rúbrica.

No se afirma que `gpt-5.6-sol` sea definitivamente la alternativa más económica posible. Para justificar una sustitución por un modelo más pequeño sería necesario ejecutar una calibración comparativa y verificar que la reducción de costo no deteriore de manera significativa la calidad de las evaluaciones.

## Trazabilidad

Los valores de tokens utilizados en este análisis provienen de ejecuciones efectivas de la API y están registrados individualmente en:

- `corridas/corrida_01/METADATOS.md`
- `corridas/corrida_02/METADATOS.md`
- `corridas/corrida_03/METADATOS.md`

De este modo, el análisis económico diferencia entre mediciones reales y proyecciones estimadas.
