# Instalação do Prometheus no Linux

1- Pegar o link de download da versão deseja no site so Prometheus (https://prometheus.io/download/).  

<br/>

2- Baixar o arquivo no linux:

```
wget https://github.com/prometheus/prometheus/releases/download/v2.37.5/prometheus-2.37.5.linux-amd64.tar.gz
```

<br/>

3 - Descompactar:
```
tar -xzvf prometheus-2.37.5.linux-amd64.tar.gz
```

<br/>

4 - Entrar no diretorio descompactado e mover os binarios para os devidos diretorios:
```
cd prometheus-2.37.5.linux-amd64
sudo mv prometheus /usr/local/bin/prometheus
sudo mv promtool /usr/local/bin/promtool
```

<br/>

5 - Criar o diretorio de configuração e mover os arquivos de configuração de biblioteca para la:
```
sudo mkdir /etc/prometheus
sudo mv prometheus.yml /etc/prometheus/
sudo mv consoles /etc/prometheus
sudo mv console_libraries /etc/prometheus
```

<br/>

6 - Editar o arquivo de configuração do prometheus conforme [/conf/prometheus.yml](/conf/prometheus.yml)

<br/>

7 - Criar o diretorio para armazenamento dos dados do Prometheus:
```
sudo mkdir /var/lib/prometheus
```

<br/>

8 - Criar usuario e grupo para ser usado pelo Prometheus:
```
sudo addgroup --system prometheus
sudo adduser --shell /sbin/nologin --system --group prometheus
```

<br>

9 - Dar permissão para o usuario/grupo do Prometheus nos devidos diretorios:
```
sudo chown -R prometheus:prometheus /etc/prometheus
sudo chown -R prometheus:prometheus /var/lib/prometheus
sudo chown -R prometheus:prometheus /usr/local/bin/prometheus
sudo chown -R prometheus:prometheus /usr/local/bin/promtool
```

<br/>

10 - Para fazer com que o Prometheus rode como serviço, precisamos criar o arquivo `/etc/systemd/system/promtetheus.service`:
```
nano /etc/systemd/system/promtetheus.service
```

E deixar o conteudo conforme [/conf/prometheus.service](/conf/prometheus.service)

<br/>

11 - Reiniciar o daemon do Linux
```
systemctl daemon-reload
```

<br>


12 - Dar enable no serviço e inicia-lo
```
systemctl enable protheus --now
```
OBS: a flag --now vai fazer com que o serviço seja habilitado e ja iniciado.

<br>

13 - Confira se o serviço está rodando:
```
systemctl status prometheus
```

14 - Feito isso é so testar o acesso pelo `http://localhost:9090` ou apontando para o IP do servidor, em caso de acesso externo. 
