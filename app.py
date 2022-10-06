from time import sleep
from selenium import webdriver
from bs4 import BeautifulSoup 
from planilha import criaPlan

nv = webdriver.Chrome() #declarando o navegador

nv.get("https://amazon.com.br") #navegando até a página inicial da amazon 
barPesquisa = nv.find_element('xpath','//*[@id="twotabsearchtextbox"]') #reconhecendo a barra de pesquisa
barPesquisa.click() #clicando na barra de pesquisa
barPesquisa.send_keys("iPhone") #inserindo o produto que quero pesquisar
confirmar=nv.find_element('xpath','//*[@id="nav-search-submit-button"]') #reconhecendo o botão para confirmar a pesquisa
confirmar.click()

sleep(5)

pagConteud = nv.page_source
bs = BeautifulSoup(pagConteud,"html.parser")

tagsPai = bs.find_all('div', attrs={'data-component-type':'s-search-result'})

produtos = []
for i in tagsPai:
    precoInt = i.find('span',attrs={'class':'a-price-whole'})
    precoFrac= i.find('span',attrs={'class':'a-price-fraction'})
    if str(type(precoInt)) != "<class 'NoneType'>":
        preco = str(precoInt.text) + str(precoFrac.text)       
    else:preco = 'Indeterminado'

    h2 = i.find('h2')
    nome = h2.find('span')
    nome = str(nome.text)
    
    produtos.append({'nome':nome,'valor':preco})


criaPlan('iPhone_Amazon', produtos)

