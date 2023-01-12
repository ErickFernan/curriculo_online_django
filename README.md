Uma das recomendações mais recorrentes para as pessoas que querem ingressar no mercado de TI, é a criação de um portfólio com seus principais dados de 
perfil, contato e projetos. Tendo isso em mente, quando iniciei o curso de Django decidi que ao final dele utilizaria dos conhecimentos adquiridos para 
fazer o meu, o que resultou nesse projeto que será aqui descrito.

O projeto é baseado em Django e utiliza o banco de dados PostgreSQL para armazenamento, o site foi publicado através da plataforma 
[Heroku](https://dashboard.heroku.com/login) que possui um plano grátis sem a necessidade de cadastro de um cartão de 
crédito (logicamente com algumas limitações de uso). 

# Front-end

Para o projeto foi utilizado um template(colocar o link) gratuito disponivel na internet, a partir desse template algumas mudanças foram efetuadas para
deixa-lo “compatível” com o Django, algumas das principais mudanças foram a separação do modelo em partes distintas (como: header, about, index, …) 
para reaproveitamento e organização de cada modelo, a parte do Html foi reescrita para que as partes repetitivas sejam criadas a partir das informações 
disponíveis no banco de dados, assim o site torna-se dinâmico e atualizações no mesmo podem ser feitas diretamente na parte administrativa, sem a 
necessidade de levar para produção sempre que houver alguma alteração no projeto, além disso reaproveitando a separação de cada tópico foram criadas as 
paginas de erros 404 e 500.

# Views

Para as views do projeto foi utilizado Class Based Views(CBV), diferentemente de projetos antigos em que utilizei Function Based Views(FBV), a CBV para 
este projeto possui tudo o que era necessário por padrão (FormView), o que facilitou tanto a parte organizacional quanto a carga de trabalho necessário 
para seu funcionamento.
