# Instalando o node exporter

1 - Ir no repositorio node_exporter do github do Prometheus. Em relases `(https://github.com/prometheus/node_exporter/releases)`, encontrar e baixar a versão compativel com o cliente:

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

<br>

5 - Criar um grupo e um usuario para executar o binario:
```
 addgroup --system node_exporter
 adduser --shel /sbin/nologin --system --group node_exporter
```

<br>

6 - Criar um serviço:
```
nano /etc/systemd/system/node_exporter.service
```
Colocando o conteudo de [/conf/node_exporter.service](https://github.com/LuanArndt/DescomplicandoPrometheus/blob/main/conf/node_exporter.service)

<br>

7 - Dar reload no daemon:
```
systemctl daemon-reload
```

<br>

8 - Habilitar e iniciar o serviço:
```
systemctl enable node_exporter --now
```

<br>

9 - Editar o `/etc/prometheus/prometheus.yml` e criar um novo job apontando para o servidor com node_exporter pela porta 9100.

<br>

# Habilitando novos coletores

1 - Criar o diretorio e arquivo de configuração do node_exporter:
```
mkdir /etc/node_exporter
nano /etc/node_exporter/node_exporter_options
```

<br>

2 - Criar a variavel com o coletor a ser habilitado, inserindo o conteúdo abaixo no arquivo:
```
OPTIONS="--collector.systemd"
```

<br>

3 - Dar o owner da pasta criada, para o usuario e grupo do node exporter:
```
sudo chown -R node_exporter:node_exporter /etc/node_exporter/
```

<br>

4 - Editar o arquivo do serviço `(/etc/systemd/system/node_exporter.service)`, colocando o `EnvironmentFile` apontando para o arquivo de configuração criado:
```
[Service]
...
EnvironmentFile=/etc/node_exporter/node_exporter_options
```

<br>

5 - Ainda no arquivo do serviço, adicionar o `$OPTIONS` (Variavel que criamos dentro do arquivo de configuração) ao final do `ExecStart`.
```
ExecStart=/usr/local/bin/node_exporter $OPTIONS
```

<br>

Ao final, o arquivo de serviço ficará assim:
```
[Unit]
Description=Node Exporter
Wants=network-online.target
After=network-online.target

[Service]
User=node_exporter
Group=node_exporter
Type=simple
EnvironmentFile=/etc/node_exporter/node_exporter_options
ExecStart=/usr/local/bin/node_exporter $OPTIONS

[Install]
WantedBy=multi-user.target
```

<br>

6 - Reiniciar o deamon e o node exporter:
```
sudo systemctl daemon-reload
sudo systemctl restart node_exporter
```
