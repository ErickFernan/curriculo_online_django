<h1 align="center">
PROJETO PORTFÓLIO/CURRÍCULO WEB
</h1>

## Sobre

<p align="justify">  
Uma das recomendações mais recorrentes para as pessoas que querem ingressar no mercado de TI, é a criação de um portfólio com seus principais dados de 
perfil, contato e projetos. Tendo isso em mente, quando iniciei o curso de Django decidi que ao final dele utilizaria dos conhecimentos adquiridos para 
fazer o meu, o que resultou neste projeto que será aqui descrito.
</p>

<p align="justify"> 
O projeto é baseado em Django e utiliza o banco de dados PostgreSQL para armazenamento, o site foi publicado através da plataforma 
[Heroku](https://dashboard.heroku.com/login) que possui um plano grátis sem a necessidade de cadastro de um cartão de 
crédito (logicamente com algumas limitações de uso). 
</p>


[clique aqui para acessa-lo](www.google.com)

## Front-end

<p align="justify"> 
Para o projeto foi utilizado um template(colocar o link) gratuito disponivel na internet, a partir desse template algumas mudanças foram efetuadas para
deixa-lo “compatível” com o Django, algumas das principais mudanças foram a separação do modelo em partes distintas (como: header, about, index, …) 
para reaproveitamento e organização de cada modelo, a parte do Html foi reescrita para que as partes repetitivas sejam criadas a partir das informações 
disponíveis no banco de dados, assim o site torna-se dinâmico e atualizações no mesmo podem ser feitas diretamente na parte administrativa, sem a 
necessidade de levar para produção sempre que houver alguma alteração no projeto, além disso reaproveitando a separação de cada tópico foram criadas as 
paginas de erros 404 e 500.
</p>

## Views

<p align="justify"> 
Para as views do projeto foi utilizado Class Based Views(CBV), diferentemente de projetos antigos em que utilizei Function Based Views(FBV), a CBV para 
este projeto possui tudo o que era necessário por padrão (FormView), o que facilitou tanto a parte organizacional quanto a carga de trabalho necessário 
para seu funcionamento.
</p>

## Models


Para os models foi criado um grupo base utilizado em todos os modelos contendo as informações:

1. Criado: Data de criação, campo do tipo Datefield.
2. Modificado: Data de modificação, campo do tipo Datefield.
3. Ativo: Situação do dado (ativo ou não), campo do tipo BooleanField.

<p align="justify"> 
Para a parte de imagens foi utilizado a função stdimage, sendo seus nomes rescritos utilizando a biblioteca uuid no intuito de evitar conflito entre os nomes na hora de fazer o upload e, consequentemente, a perca de informação (o django possui por padrão a função de reescrita, entretanto ela mantêm parte do nome original, sendo assim preferi usar uma biblioteca hexadecimal para existir apenas caracteres sem a formação de palavras).
</p>

## Tradução

<p align="justify"> 
Para que o site possua a função de tradução foi lançado mão de duas ferramentas, uma para a parte Html (<em>gettext</em>) disponível pelo próprio django e outra para os textos no banco de dados (<em>django-modeltranslation</em>) que é necessário efetuar a instalação por fora. Para a parte Html é gerado um arquivo de lista onde você escreve a tradução para cada palavra, algumas ferramentas como o poedit podem ser utilizadas para simplificar o trabalho. Já para os textos do banco de dados, foi preciso escrever para quais linguas a tradução seria feita e após configurado é possível digitar as traduções no momento que se cadastra algo no banco de dados. Com as traduções configuradas, o texto apresentado na página será referente ao idioma utilizado pelo navegador.
OBS.: ainda não possuo um inglês fluente, dessa forma se encontrar alguma tradução estranha a culpa é do Google tradutor!
</p>

## Testes

<p align="justify"> 
Este projeto está com todos os testes escritos e funcionando, para criar os testes e ver quais estavam faltando foi utilizada a biblioteca coverage e é possível ver o PDF de resumo clicando <a href="https://github.com/ErickFernan/curriculo_online_django/blob/main/tests.pdf" target="_blank"> AQUI </a> ou executando os comandos abaixo via terminal através do projeto no python, ou via Docker.
</p>

1. <em>coverage run manage.py test</em> -> para rodar os testes 
2. <em> coverage report</em> -> para ver um resumo no próprio terminal, 
3. <em>coverage html</em> -> para criar uma pagina html contendo detalhes sobre os testes 

## Demonstração

Caso queira ver mais sobre o projeto você pode:
1. Assistir a esse vídeo onde mostro mais detalhes sobre o projeto assim com sua parte administrativa.
2. Fazer o download deste arquivo docker para instalar e já testar em sua própria maquina. Acesse esse link para conferir o passo a passo de download e execução no docker.
3. Baixar pelo Github e se divertir modificando-o.

