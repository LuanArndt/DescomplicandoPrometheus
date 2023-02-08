# Gauge
O gauge é o tipo de dado que pode ter valores flutuantes, ou seja, que aumentam e diminuem conforme necessario. Um exemplo disso pode ser o consumo de RAM.

Abaixo um exemplo de query que vai retornar uma metrica gauge:
```
memory_usage{instance="localhost:8899",job="Primeiro Exporter"}
```
