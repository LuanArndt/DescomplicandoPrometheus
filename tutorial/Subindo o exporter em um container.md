# Subindo o exporter em um container

1 - Rodar o script de instalação do docker: 
```
curl -fsSL https://get.docker.com | bash
```

<br>

2 - Clonar esse repositorio e entrar na pasta exporter:
```
git clone https://github.com/LuanArndt/DescomplicandoPrometheus.git
cd DescomplicandoPrometheus/exporter
```

<br>

3 - Buildar o container:
```
docker build -t primeiro-exporter:1.0 .
```

<br>

4 - Subir o container a partir da imagem buildada e mapear a porta configurada no [exporter/exporter.py](https://github.com/LuanArndt/DescomplicandoPrometheus/blob/3b7f0404978fdd624cb603cd03fc658dc46fa6b3/exporter/exporter.py#L44):
```
docker run -d --name primeiro-exporter -p 8899:8899 primeiro-exporter:1.0
```

<br>

5 - Testar o acesso em `http://localhost:8899/metrics` ou apontando para o IP da maquina, caso seja externo.
