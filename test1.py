#BROWSER DRIVER IMPORTS
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

#DELAY LIBRARY IMPORT
import time

#import pandas as pd

#CONSTANTS
class DadosUsuario:
    USUARIO = "giovanni"
    SENHA = "abcde"
DELAY1 = 3 #seconds
d = DadosUsuario()


#criar o navegador
servico = Service()
opcoes = Options()
opcoes.add_argument("--start-maximized")
navegador = webdriver.Chrome(service=servico, options=opcoes)

def login():
    navegador.get('https://fatece.edu.br/adm/login')
    time.sleep(DELAY1)
    navegador.find_element(By.NAME,'user').send_keys(d.USUARIO)
    time.sleep(DELAY1)
    try:
        navegador.find_element(By.NAME,'senha').send_keys(d.SENHA,Keys.ENTER)
    except:
        return print("deu ruim no login!")
    finally:
        time.sleep(DELAY1)


#passo a passo:

login() # -> essa foi!

#certificados()

#clicaCampo()

#insereDados()
    #excel->data frame com pandas

#emitirCertificado()

#baixarCertificado()
