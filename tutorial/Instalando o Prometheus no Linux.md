# Instalação do Prometheus no Linux

1- Pegar o link de download da versão deseja no site so Prometheus (https://prometheus.io/download/).  

2- Baixar o arquivo no linux:

```
wget https://github.com/prometheus/prometheus/releases/download/v2.37.5/prometheus-2.37.5.linux-amd64.tar.gz
```
  

3 - Descompactar:
```
tar -xzvf prometheus-2.37.5.linux-amd64.tar.gz
```


4 - Entrar no diretorio descompactado e mover os binarios para os devidos diretorios:
```
cd prometheus-2.37.5.linux-amd64
sudo mv prometheus /usr/local/bin/prometheus
sudo mv promtool /usr/local/bin/promtool
```


5 - Criar o diretorio de configuração e mover os arquivos de configuração de biblioteca para la:
```
sudo mkdir /etc/prometheus
sudo mv prometheus.yml /etc/prometheus/
sudo mv consoles /etc/prometheus
sudo mv console_libraries /etc/prometheus
```


6 - Editar o arquivo de configuração do prometheus conforme [/conf/prometheus.yml](/conf/prometheus.yml)


7 - Criar o diretorio para armazenamento dos dados do Prometheus:
```
sudo mkdir /var/lib/prometheus
```


8 - Criar usuario e grupo para ser usado pelo Prometheus:
```
sudo addgroup --system prometheus
sudo adduser --shell /sbin/nologin --system --group prometheus
```


9 - Para fazer com que o Prometheus rode como serviço, precisamos criar o arquivo `/etc/systemd/system/promtetheus.service`:
```
nano /etc/systemd/system/promtetheus.service
```

E deixar o conteudo conforme [/conf/prometheus.service](/conf/prometheus.service)
