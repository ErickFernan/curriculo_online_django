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
O projeto foi desenvolvido com <em>Django</em> e utiliza o banco de dados <em>PostgreSQL</em> para o armazenamento de dados. A arquitetura de produção foi configurada com <em>Nginx</em> atuando como proxy reverso para o servidor de aplicação <em>Gunicorn</em>. O Nginx também é responsável por servir os arquivos estáticos, enquanto o <em>MinIO</em>, um serviço de armazenamento de objetos compatível com a API S3, gerencia os arquivos de mídia (como imagens e documentos), garantindo uma arquitetura robusta e escalável.
 
</p>

<p align="center">
 <img src="https://github.com/ErickFernan/curriculo_online_django/blob/master/readme imagens/arquitetura.svg"/>
</p>

<p align="center"> Visite o site em: https://erickfernan.dev.br/ </p>


## Front-end

<p align="justify"> 
Para a interface, utilizei um <a href="https://www.free-css.com/free-css-templates/page278/freefolio">template</a> gratuito que foi adaptado para se integrar ao ecossistema <em>Django</em>. As principais modificações incluíram a componentização do layout em partes reutilizáveis (como <em>header, about, index</em>), otimizando a organização e a manutenção. O código <em>HTML</em> foi reescrito para renderizar dinamicamente o conteúdo a partir do banco de dados, permitindo que atualizações sejam feitas diretamente pelo painel administrativo, sem a necessidade de um novo deploy a cada alteração. Além disso, a estrutura modular foi aproveitada para criar páginas de erro personalizadas (404 e 500).
</p>

## Views

<p align="justify"> 
As views do projeto foram implementadas utilizando <em>Class-Based Views</em> (CBV), uma abordagem que, para este caso de uso, se mostrou mais organizada e eficiente do que as <em>Function-Based Views</em> (FBV). As CBVs nativas do Django, como a <code>FormView</code>, ofereceram todas as funcionalidades necessárias, simplificando o desenvolvimento e reduzindo a quantidade de código escrito.
</p>

## Models


Para os <em> models </em> foi criado um grupo base utilizado em todos os modelos contendo as informações:

1. Criado: Data de criação, campo do tipo <em> Datefield </em>.
2. Modificado: Data de modificação, campo do tipo <em> Datefield </em>.
3. Ativo: Situação do dado (ativo ou não), campo do tipo <em> BooleanField </em>.

<p align="justify"> 
O upload de imagens é gerenciado pela biblioteca <em>stdimage</em>. Para evitar conflitos e sobreescrita de arquivos, os nomes das imagens são padronizados utilizando a biblioteca <em>uuid</em>, que gera identificadores hexadecimais únicos.
</p>

## Internacionalização (i18n)

<p align="justify"> 
O site foi desenvolvido para suportar múltiplos idiomas através de duas ferramentas principais: <em>gettext</em>, a solução nativa do Django para tradução de strings no template, e <em>django-modeltranslation</em> para a tradução de conteúdo armazenado no banco de dados. A configuração permite que o idioma exibido seja definido automaticamente com base nas preferências do navegador do usuário.
</p>

## Testes

<p align="justify"> 
A qualidade do código é garantida por uma suíte de testes completa. A biblioteca <em>coverage</em> foi utilizada para medir a cobertura de testes e identificar áreas não testadas. Você pode visualizar o relatório de cobertura clicando <a href="https://github.com/ErickFernan/curriculo_online_django/blob/master/tests.pdf"> AQUI </a> ou executando os seguintes comandos no terminal:
</p>

1. <em>coverage run manage.py test</em> -> Executa a suíte de testes.
2. <em> coverage report</em> -> Exibe um resumo da cobertura no terminal.
3. <em>coverage html</em> ->  Gera um relatório HTML detalhado.

## Demonstração

Caso queira ver mais sobre o projeto você pode:
1. [Assistir a esse vídeo](https://youtu.be/xNfOM4lk_LE) onde mostro mais detalhes sobre o projeto assim com sua parte administrativa.
2. Fazer o <em> download </em> deste arquivo .zip e instalar utilizando o docker para já testar em sua própria máquina. Acesse esse [LINK](https://gist.github.com/ErickFernan/e8d9e72500b7f75b77db9e9fb931e5fa) para conferir o passo a passo de <em> download </em> e execução no <em> docker </em>. 
    * Obs1.: Você pode também assitir esse [Vídeo](https://youtu.be/HGx5Y0h-Lkg) para ver o passo a passo.
3. Baixar pelo <em> Github </em> e se divertir modificando-o. Obs.: lembre-se de instalar os requisitos que se encontram no arquivo 
<em> requirements.txt </em>.

## Contato

Para sugestões ou dúvidas entre em contado por:

1. E-mail: dverickfernan@gmail.com
2. Whatsapp: <a href="https://wa.me/5532999824460"> 32 999824460 </a>
3. Linkedin: <a href="https://www.linkedin.com/in/dverickfernan/"> in/dverickfernan </a>

## 🚀 Status do Projeto

Este projeto está em constante evolução, com foco em modernizar sua arquitetura, segurança e funcionalidades.

### Melhorias Recentes
- [x] **Variáveis de Ambiente**: A configuração do projeto foi migrada para um arquivo `.env`, separando as credenciais do código-fonte.
- [x] **Docker Compose**: O arquivo `docker-compose.yml` foi corretamente integrado ao versionamento do projeto.
- [x] **Ocultar URL do Admin**: Alterar o caminho do painel administrativo para uma URL não previsível, visando reduzir a exposição a ataques automatizados.
- [x] **Storage de Arquivos**: Implementar o MinIO como serviço de storage self-hosted (compatível com API S3) para o upload e armazenamento de imagens e documentos.

### Próximos Passos (Roadmap)
- [ ] **Gerenciamento de Mídia**: Implementar a lógica para excluir/atualizar os arquivos no MinIO quando um objeto for modificado ou removido no painel administrativo do Django.
- [ ] **Revisão de UI/UX**: Analisar e refatorar os campos da aplicação e o design geral para melhorar a experiência do usuário.
- [ ] **Revisão de UI/UX**: Definir um peso de prioridade para os dados que compõem "Educação" e "Experiência" para melhor ordenação.
- [ ] **Serviço de E-mail**: Configurar um container de e-mail local para desenvolvimento (ex: MailHog ou Mailtrap) como solução temporária antes de integrar um serviço de produção.
- [ ] **Gerenciamento de Conteúdo**: Refatorar o template `videomodalstart.html` para permitir que o vídeo seja gerenciado pelo painel administrativo, em vez de estar fixo no código HTML.
- [ ] **Atualizar Vídeo de Apresentação**: Gravar um novo vídeo demonstrativo que reflita a arquitetura e as funcionalidades atuais do projeto.
- [ ] **Cobertura de Testes**: Revisar e complementar a suíte de testes para garantir que as novas funcionalidades estejam cobertas.

#### Segurança
- [ ] **Autenticação de Dois Fatores (2FA)**: Implementar o pacote `django-otp` para adicionar uma camada extra de segurança no login dos administradores.
- [ ] **Limitar Tentativas de Login**: Integrar o `django-axes` para bloquear endereços de IP após múltiplas tentativas de login falhas.
- [ ] **Admin Honeypot**: Configurar o `django-admin-honeypot` para criar uma página de login falsa em `/admin/` e registrar tentativas de acesso indevido.
