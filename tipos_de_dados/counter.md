# Counter

Counter é um tipo de dado que só é incrementado. Geralmente de 1 em 1. Diferente do `gauge`, o `counter` não diminuiu o valor.

É comum que as metricas do tipo `counter` tenham a flag `_total` no final do nome. Por exemplo: `requests_total`

<br>

Abaixo um exemplo de query que vai retornar os valores de um counter:
```
requests_total{instance="localhost:8899",job="Primeiro Exporter"}
```
