# Summary

O summary é bem parecido com o histogram. Aqui os `buckets` são chamados de `quantiles` e armazeam valores entre 0 e 1. O valor do bucket é o valor que está entre os quantiles.

A vantagem do `summary` é a precisão, e a desvantagem é que ele é menos flexivel, pois as janelas de tempo precisam ser definidas na criação das métricas.

<br>

Abaixo um exemplo de query que trás um retorno do tipo `summary`:
```
requests_duration_seconds_sum{instance="localhost:8899",job="Primeiro Exporter"}
```
