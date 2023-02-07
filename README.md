<h1 align="center">
PROJETO PORTFÓLIO/CURRÍCULO WEB
</h1>

## Sobre

<p align="justify">  
Uma das recomendações mais recorrentes para as pessoas que querem ingressar no mercado de TI, é a criação de um portfólio com seus principais dados de 
perfil, contato e projetos. Tendo isso em mente, quando iniciei o curso de <em> Django </em> decidi que ao final dele utilizaria dos conhecimentos adquiridos para 
fazer o meu, o que resultou neste projeto que será aqui descrito.
</p>

<p align="justify"> 
O projeto é baseado em <em> Django </em> e utiliza o banco de dados <em> PostgreSQL </em> para armazenamento, o site foi publicado através da plataforma 
<a href="https://dashboard.heroku.com/login"> HEROKU </a> que possui um plano grátis (logicamente com algumas limitações de uso). 
 
</p>

<p align="center">
 <img src="https://github.com/ErickFernan/curriculo_online_django/blob/main/media/simplescreenrecorder-2023-01-25_15.07.50.gif?raw=true"/>
</p>


[CLIQUE AQUI PARA CONFERIR O SITE](#)
 Obs.: A Heroku não possui mais o plano gratuito, então por enquanto o site não está disponível.

## Front-end

<p align="justify"> 
Para o projeto foi utilizado um <a href="https://www.free-css.com/free-css-templates/page278/freefolio"> template </a> gratuito disponivel na internet, a partir desse template algumas mudanças foram efetuadas para
deixa-lo “compatível” com o <em> Django </em>, algumas das principais mudanças foram a separação do modelo em partes distintas (como: <em> header, about, index, … </em>) 
para reaproveitamento e organização de cada modelo, a parte do <em> Html </em> foi reescrita para que as partes repetitivas sejam criadas a partir das informações 
disponíveis no banco de dados, assim o site torna-se dinâmico e atualizações no mesmo podem ser feitas diretamente na parte administrativa, sem a 
necessidade de levar para produção sempre que houver alguma alteração no projeto, além disso reaproveitando a separação de cada tópico foram criadas as 
paginas de erros 404 e 500.
</p>

## Views

<p align="justify"> 
Para as views do projeto foi utilizado <em> Class Based Views </em>(CBV), diferentemente de projetos antigos em que utilizei <em> Function Based Views </em>(FBV), a CBV para 
este projeto possui tudo o que era necessário por padrão (FormView), o que facilitou tanto a parte organizacional quanto diminuiu a carga de trabalho necessário 
para seu funcionamento.
</p>

## Models


Para os <em> models </em> foi criado um grupo base utilizado em todos os modelos contendo as informações:

1. Criado: Data de criação, campo do tipo <em> Datefield </em>.
2. Modificado: Data de modificação, campo do tipo <em> Datefield </em>.
3. Ativo: Situação do dado (ativo ou não), campo do tipo <em> BooleanField </em>.

<p align="justify"> 
Para a parte de imagens foi utilizado a função <em> stdimage </em>, sendo seus nomes rescritos utilizando a biblioteca <em> uuid </em> no intuito de evitar conflito entre os nomes na hora de fazer o upload e, consequentemente, a perca de informação (o django possui por padrão a função de reescrita, entretanto ela mantêm parte do nome original, sendo assim preferi usar uma biblioteca hexadecimal para existir apenas caracteres sem a formação de palavras).
</p>

## Tradução

<p align="justify"> 
Para que o site possua a função de tradução foi lançado mão de duas ferramentas, uma para a parte Html (<em>gettext</em>) disponível pelo próprio django e outra para os textos no banco de dados (<em>django-modeltranslation</em>) que é necessário efetuar a instalação por fora. Para a parte Html é gerado um arquivo de lista onde você escreve a tradução para cada palavra, algumas ferramentas como o poedit podem ser utilizadas para simplificar o trabalho. Já para os textos do banco de dados, foi preciso escrever para quais linguas a tradução seria feita e após configurado é possível digitar as traduções no momento que se cadastra algo no banco de dados. Com as traduções configuradas, o texto apresentado na página será referente ao idioma utilizado pelo navegador.
OBS.: ainda não possuo um inglês fluente, dessa forma se encontrar alguma tradução estranha a culpa é do Google tradutor!
</p>

## Testes

<p align="justify"> 
Este projeto está com todos os testes escritos e funcionando, para criar os testes e ver quais estavam faltando foi utilizada a biblioteca <em> coverage </em> e é possível ver o PDF de resumo clicando <a href="https://github.com/ErickFernan/curriculo_online_django/blob/main/tests.pdf"> AQUI </a> ou executando os comandos abaixo via terminal através do projeto no <em> python </em>, ou via <em> Docker </em>.
</p>

1. <em>coverage run manage.py test</em> -> para rodar os testes.
2. <em> coverage report</em> -> para ver um resumo no próprio terminal.
3. <em>coverage html</em> -> para criar uma pagina html contendo detalhes sobre os testes.

## Demonstração

Caso queira ver mais sobre o projeto você pode:
1. Assistir a esse vídeo onde mostro mais detalhes sobre o projeto assim com sua parte administrativa.
2. Fazer o <em> download </em> deste arquivo .zip e instalar utilizando o docker para já testar em sua própria máquina. Acesse esse [LINK](https://gist.github.com/ErickFernan/e8d9e72500b7f75b77db9e9fb931e5fa) para conferir o passo a passo de <em> download </em> e execução no <em> docker </em>. 
    * Obs1.: Você pode também assitir esse [Vídeo](https://youtu.be/HGx5Y0h-Lkg) para ver o passo a passo.
    * Obs2.: Por não estar publicado vou deixar uma opção do site estático [AQUI](#), assim além de testar é possível vê-lo preenchido.
3. Baixar pelo <em> Github </em> e se divertir modificando-o. Obs.: lembre-se de instalar o requisitos que se encontram no arquivo 
<em> requirements.txt </em>.

## Contato

Para sugestões ou dúvidas entre em contado por:

1. E-mail: dverickfernan@gmail.com
2. Whatsapp: <a href="https://wa.me/5532999824460"> 32 999824460 </a>
3. Linkedin: <a href="https://www.linkedin.com/in/dverickfernan/"> in/dverickfernan </a>

