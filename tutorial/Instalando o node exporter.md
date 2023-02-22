# Instalando o node exporter

1 - Ir no repositorio node_exporter do github do Prometheus. Em relases `+(https://github.com/prometheus/node_exporter/releases)`, encontrar e baixar a versão compativel com o cliente:

```
wget https://github.com/prometheus/node_exporter/releases/download/v1.5.0/node_exporter-1.5.0.linux-amd64.tar.gz
```

<br>

2 -  Descompactar:
```
 tar -xvf node_exporter-1.5.0.linux-amd64.tar.gz
```

<br>

3 - Entrar na pasta e mover o binario para o `/usr/local/bin`:
```
cd node_exporter-1.5.0.linux-amd64/
mv node_exporter /usr/local/bin/
```

<br>

4 - Testar o binario, vendo a versão:
```
node_exporter --version
```

o retorno deve ser semelhante a esse:
```
node_exporter, version 1.5.0 (branch: HEAD, revision: 1b48970ffcf5630534fb00bb0687d73c66d1c959)
  build user:       root@6e7732a7b81b
  build date:       20221129-18:59:09
  go version:       go1.19.3
  platform:         linux/amd64
```