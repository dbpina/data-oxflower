# data-oxflower



## Imagens Docker
Disponibilizamos uma imagem do ambiente caso alguém queira utilizar.
O Dockerfile presente na pasta cria a imagem de um conteiner com os dados deste repositório. No entanto, utilizando o comando :

```
docker pull lilianekunstmann/tensorflow_i
```

É possível baixar a imagem pronta do DockerHub, essa imagem pode ser executada e acessada interativamente através dos seguintes comandos:

```
docker run --name <nome_container> -i tensorflow_i
docker exec -it <nome_container> bash
```
