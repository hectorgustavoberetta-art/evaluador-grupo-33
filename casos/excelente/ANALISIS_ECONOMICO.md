# Análisis económico

## Modelo utilizado

El sistema utiliza un modelo de OpenAI mediante API.

La elección del modelo debe seguir el principio de utilizar el modelo más pequeño que pueda resolver adecuadamente la tarea, siempre que mantenga la calidad necesaria para aplicar la rúbrica y analizar evidencia.

## Componentes del costo

El costo de cada corrida depende principalmente de:

- tokens de entrada;
- tokens de salida;
- precio vigente del modelo utilizado;
- cantidad de evaluaciones realizadas.

## Cálculo por corrida

El costo debe calcularse mediante:

Costo de entrada = (tokens de entrada / 1.000.000) × precio por millón de tokens de entrada.

Costo de salida = (tokens de salida / 1.000.000) × precio por millón de tokens de salida.

Costo total por corrida = costo de entrada + costo de salida.

## Registro de consumo

Para cada ejecución real se deben registrar:

- modelo utilizado;
- tokens de entrada;
- tokens de salida;
- costo estimado de la corrida.

Los precios deben verificarse al momento de realizar el cálculo porque pueden cambiar.

## Proyección de uso

Una vez determinado el costo promedio por corrida:

Costo semanal = costo promedio por corrida × cantidad de evaluaciones semanales.

Costo anual = costo semanal × 52.

## Criterio de selección del modelo

Si un modelo de menor costo obtiene resultados suficientemente consistentes durante la calibración, debe preferirse frente a un modelo más costoso.

Un modelo de mayor capacidad se justifica únicamente cuando la mejora observada en la calidad de evaluación compensa el incremento del costo.

## Nota sobre los valores

Este documento define el procedimiento económico y evita presentar como reales cifras de consumo que no hayan sido medidas durante una ejecución efectiva.
