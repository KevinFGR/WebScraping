# WebScraping
<label>Acessando a internet, coletando seus dados e apresentando-os</label>

<div align=center>
<img src="https://user-images.githubusercontent.com/109561598/197368807-89056542-fbeb-430d-a4c7-dd05c9330790.jpg" width=800 alt=imagem logo do projeto" />
</div>

## Tópicos: 
:small_blue_diamond: [Sobre o projeto](#sobre-o-projeto)

:small_blue_diamond: [Arquivos](#arquivos)

:small_blue_diamond: [Sobre o arquivo app](#sobre-o-arquivo-app)

:small_blue_diamond: [Sobre o arquivo planilhas](#sobre-o-arquivo-planilhas)

:small_blue_diamond: [Lógica utilizada para encontrar os dados no site](#lógica-utilizada-para-encontrar-os-dados-no-site)

:small_blue_diamond: [Requisitos para rodar o programa](#requisitos-para-rodar-o-programa)

:small_blue_diamond: [Como rodar o código](#como-rodar-o-código)

## Sobre o projeto:
<p>A iniciativa da criação desse projeto se deu por uma vaga de emprego que concorri, a qual teve como teste para os candidatos a criação de um script cuja função é realizar um WebScraping. Sendo assim, a tarefa foi:</p>
<ul>
<li>Abrir o site da Amazon;</li>
<li>Pesquisar por Iphone;</li>
<li>Coletar os dados de todos os resultados encontrados;</li>
<li>Criar uma planilha com esses dados.</li>
</ul>

## Arquivos:
<ul>
  <li>app.py: arquivo principal, é ele quem deve ser executado;</li>
  <li>planilhas.py:arquivo que possui os métodos voltados à criação da planilha.</li>
</ul>

## Sobre o arquivo <a href='https://github.com/KevinFGR/WebScraping/blob/main/app.py'>app</a>:
<ul align="justify">
  <li>
    Linhas 1 à 4 : importando bibliotecas e módulo;</li>
  <li>
    Linha 6: declarando o navegador que será usado;</li>
  <li>
    Linhas 8 à 13: com auxílio da biblioteca selenium, abrindo a página inicial da
    Amazon para o Brasil (https://www.amazon.com.br), procurando a barra de
    pesquisa, digitando “iPhone” na barra e clicando no botão pesquisar;</li>
  <li>
    Linhas 17 e 18: passando para o BeautifulSoup o conteúdo HTML da página
    em que o programa se encontra no momento;</li>
  <li>
    Linha 20: atribuindo à variável “tagsPai” uma lista onde cada item refere ao
    bloco de código referente a cada produto retornado pelo site;</li>
  <li>
    Linha 23: inicia o laço de repetição que para cada item dentro da lista
  “tagsPai” será efetuado os seguintes comandos;</li>
  <li>
    Linhas 24 e 25: atribuindo à variável “precoInt” o valor referente ao preço;</li>
  <li>
    Linhas 26 à 30: caso o valor recebido na variável “precoInt” não seja do tipo
    nulo será atribuído à variável “preco” os valores inteiro e fracionário do preço
    do produto concatenados. Caso o valor recebido na variável “precoInt” seja
    do tipo nulo o programa entende que o site não disponibiliza esta informação
    e atribui à variável “preco” o valor “Indeterminado”;</li>
  <li>
    Linhas 32 à 34: acha onde está o valor referente ao nome do produto, o
  capta e converte em uma string;</li>
  <li>
    Linha 36: adiciona à lista “produtos” um dicionário contendo o valor referente
    ao nome e o preço do produto;</li>
  <li>
    Linha 38: chama o método que cria a planilha com o nome de
    “iPhone_Amazon”.</li>
</ul>

## Sobre o arquivo <a href="https://github.com/KevinFGR/WebScraping/blob/main/planilha.py">planilhas<a>:
<ul align="justify">
  <li>
    Linhas 1 e 2: importa da biblioteca openpyxl os comando necessários;</li><br />
  <li>
    criaPlan (nomeArq, produtos): recebe como parâmetro um valor referente ao
    nome a ser dado à planilha e ao título e uma lista de dicionários que
    contenham os nomes dos produtos e seus respectivos valores. O método irá
    criar a planilha, suas linhas iniciais e chamará os demais métodos para
    adicionar os registros e estilizar a planilha;</li><br />
  <li>
    addProdutos (produtos, plan, linhaInicial): Recebe como parâmetro a lista
    de produtos, a referência da planilha em que serão adicionados os produtos e
    a linha de onde o método poderá inicial a adicionar os registros.
    Basicamente, a função do método é adicionar os valores referentes ao preço
    e o nome dos produtos na tabela;</li><br />
  <li>
    estiliza (planilha, celulas, estilo): recebe como parâmetro a referência da
    planilha que será modificada, uma lista com cada célula da planilha que será
    modificada e o tipo de estilo. O método estiliza as células da planilha (cor da
    fonte, espessura da fonte, cor de fundo da célula, e bordas), caso o valor
    referênte ao estilo seja 1 as células serão estilizadas como células de título,
    caso seja 2 as células serão estilizadas como células de valores.</li>
</ul>

## Lógica utilizada para encontrar os dados no site:
<ol align="justify">
  <li>Primeiramente separei os registros de cada produto retornado pelo site,
  assim, notei que cada registro está em uma div com um atributo
  “data-component-type” com o valor “s-search-result” que foi o critério usado
  para separá-los:</li>
  <br />

  <div align=center>
    <img src="https://user-images.githubusercontent.com/109561598/197365943-9c3bece0-1de8-42c9-8182-f462724cc84d.png" width=800 alt="Imagem referente ao item 1" />
  </div>

  <li>Uma vez que tenho cada registro separado e todos dentro de uma lista,
  apenas preciso de um loop que percorre cada item da lista para recuperar os
  dados;</li>
  
  <li>Para obter o nome do produto notei que esta informação está na única tag
  span dentro da primeira tag h2 dentro do registro:</li><br />

  <div align=center>
  <img src="https://user-images.githubusercontent.com/109561598/197365990-85e7c1a8-f061-4a47-8097-bd5b8a9f0ca9.png" width=800 alt="Imagem referente ao item 3" />
  </div>

  <li>Para obter o preço do registros percebi que este valor estava dentro de uma
  tag spam com o valor “a-offscreen”:</li><br />

  <div align=center>
  <img src="https://user-images.githubusercontent.com/109561598/197366007-ae98c132-335a-47f4-9504-48418fd7897e.png" width=800 alt="Imagem referente ao item 4" />
  </div>

  <ul>
    <li>Outro caminho pode ser tomado ao perceber que o valor estava
    quebrado em dois (provavelmente por conta de estética da página), a
    parte em reais inteiros estava dentro de uma span com o valor de
    “a-price-whole” para a classe e a parte em centavos estava numa span
    com o valor de “a-price-fraction” para a classe.Portanto, seria
    necessário recuperar esses dois dados e os concatenar.</li><br />
   <div align=center>
   <img src="https://user-images.githubusercontent.com/109561598/197366028-bef75a5d-4ee3-4968-b497-fd25c67547d1.png" width=800 alt="Imagem referente à segunda opção  do item 4" />
  </div>
</ul>
</ol>

## Condições para a execução do programa:
<p align="justify">Além das condições já ditas sobre os itens a serem instalados no computador
que irá executar o programa há mais uma condição para o bom funcionamento.
Em algumas situações o site da Amazon pode redirecionar o programa para
uma página inicial paralela (talvez por sobrecarga de acesso), neste caso o
programa não conseguirá captar o endereço da barra de pesquisa uma vez que
seus atributos e chave “xpah” mudaram. Abaixo uma imagem do layout da página
inicial padrão da Amazon que o programa espera encontrar:</p>

<div align=center>
<img src="https://user-images.githubusercontent.com/109561598/197366041-3805a5a2-5a9d-486d-9cf1-6fc068d9f918.png" width=800 alt="Imagem da página inicial que o programa espera" />
</div>

<p align="justify">Outra situação que pode ocasionar mal funcionamento é caso já exista uma
planilha com o nome “iPhone_Amazon”. Neste caso o programa não irá criar outra
planilha e nem substituir a planilha existente.</p>

## Requisitos para rodar o programa:
<ul>
  <li>Python (de preferência, versão 3.8 ou superior);</li>
  <li>Selenium (versão mais recente até outubro de 2022);</li>
  <li>BeautifulSoup4</li>
  <li>Openpyxl (versão mais recente até setembro de 2022);</li>
  <li>Google Chrome;</li> 
  <li>ChromeDriver referente à versão do Chrome.</li>
</ul>
<div style="display:flex">
  <img src="https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/python/python.png" height="60px" width="60px" alt="Imagem logo do python"/>
  <img src="https://seeklogo.com/images/S/selenium-logo-DB9103D7CF-seeklogo.com.png" width="60" alt="Imagem logo do Selenium" />
  <img src="https://lh3.googleusercontent.com/o9HtAcCnpfW_o5b1lkhvrJ0lzZBJ6Lm8TwxYue4Z3K5OdekeptiGVAUEPcBC_1ra7cFqAV0QOFByNl3ub_1BJbNe3A=w640-h400-e365-rj-sc0x00ffffff" alt="Imagem logo do BeautifulSoup"  width="80"/>
  <img src="https://user-images.githubusercontent.com/109561598/193160002-cd3e64d1-0076-4403-ae89-f870db7d5a43.png" height="50px" alt="Imagem logo do openpyxl"/>
  <img src="https://seeklogo.com/images/G/google-chrome-logo-95B6A0B483-seeklogo.com.png"  height="50px" alt="Imagem logo do ChromeDriver" />
  
</div>

## Como rodar o código:
<ol>
<li align="justify">
    Selecione a pasta que deseja baixar o projeto, abra a interface de linha de comando do Git e cole o seguinte código para clonar o projeto:

```
git clone https://github.com/KevinFGR/WebScraping.git 
```
</li>
<li align="justify">
    Abra a interface de linha de comando do seu computador na pasta webscraping e insira o seguinte comando para executar o programa:

```
py app.py
```
</li>
<li>Aguarde a execução do programa;</li>
<li>Após o programa informar que a planilha foi criada você pode encontrá-la na pasta do projeto com o nome "iPhone_Amazon".</li>
</ol>


:small_blue_diamond: [Voltar ao topo](#webscraping)
