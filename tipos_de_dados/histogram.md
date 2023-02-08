# Histogram

Histogram é um tipo de dado que é armezenado em `buckets`. Os `buckets` representam intervalos de tempo. Ou seja, posso ter um bucket com as requisições que duraram até 0.5s e outro bucket com as requisições que duraram até 1.5s.

Detalhe importante, o bucket de 1.5s vai conter também os dados que estão no bucket de 0.5s. Mas logicamente, nunca ao contrario. 

<br>

Por padrão, os buckets tem até 10 segundos, mas que podem ser personalizados.

<br>

Abaixo um exemplo de bucket de 0.5s:
```
requests_duration_seconds_bucket{le="0.5"}
```

Onde `le` é `less than or equal to` (Menor ou igual que)
