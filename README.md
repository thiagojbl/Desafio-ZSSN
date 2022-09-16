# Desafio-ZSSN
ZSSN (Rede Social de Sobrevivência Zumbi)

## Teste de codificação de desenvolvedor


### ZSSN (Rede Social de Sobrevivência Zumbi). O mundo como o conheceu caiu em um cenário apocalíptico. Um vírus produzido em laboratório está transformando seres humanos e animais em zumbis, famintos por carne fresca.


### Você desenvolverá uma API REST,  que armazenará informações sobre os sobreviventes, bem como os recursos que eles possuem.
### Para fazer isso, a API deve atender aos seguintes casos de uso:
#### 1) Adicionar sobreviventes ao banco de dados;
#### 2) Atualizar local do sobrevivente;
#### 3) Sinalizar sobrevivente como infectado;
#### 4) Um sobrevivente é marcado como infectado quando pelo menos outros três sobreviventes relatam sua contaminação;
#### 5) Os sobreviventes não podem adicionar / remover itens do inventário;
#### 6) Itens comerciais:
##### Os sobreviventes podem trocar itens entre si.
### Relatórios:
#### i. Porcentagem de sobreviventes infectados;
#### ii. Porcentagem de sobreviventes não infectados;
#### iii. Quantidade média de cada tipo de recurso por sobrevivente (por exemplo, 5 águas por sobrevivente);
#### iv. Pontos perdidos por causa do sobrevivente infectado.

<hr>


## 🚀 Tecnologias
<p align="center">
    <a href="https://www.python.org/">Python</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
    <a href="https://www.djangoproject.com/">Django</a></a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
    <a href="https://www.django-rest-framework.org/api-guide/viewsets/">Django Rest Framework</a></a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
    <a href="https://www.docker.com/">Docker</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
    <a href="https://www.postgresql.org/">Postgresql</a></a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
    <a href="https://git-scm.com/">GIT</a></a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
    <a href="https://aws.amazon.com/">AWS</a></a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
    <a href="https://www.postman.com/">Postman</a>
</p>
<hr>

## ⚙️ Utilização

Para utilizar a aplicação basta acessar o link público: <a href="http://ec2-18-211-64-16.compute-1.amazonaws.com/"> Desafio-Thiago </a>.

<hr>

## Clone o repositório

    $ git clone https://github.com/thiagojbl/Desafio-ZSSN.git


### Execute no docker

   $  ```docker run -p 8000:8000 thiagojb12/desafio-thiago:5```

## Endpoints 

#### 1) Todos os pedidos por cliente (filtro pelo cliente):

  $ ```GET /api/pedido/?cliente=Jose```


#### Collections utilizadas neste projeto


[desafio.postman_collection.zip]
