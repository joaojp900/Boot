import time
from tkinter import *

from selenium import webdriver
from selenium.webdriver.common.by import By



def pesquisar():
    navegador = webdriver.Chrome()
    navegador.get("https://images.google.com.br/imghp?source=mog&gl=br&gws_rd=ssl")
    navegador.find_element(by=By.XPATH, value='/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(j.get())
    navegador.find_element(by=By.XPATH, value='/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/button/div/span').click()
    time.sleep(20)

janela = Tk()
janela.title("Front")

texto_orientacao = Label(janela, text="Digite algo pra Pesquisar")
texto_orientacao.grid(column=0, row=0)

j = Entry(janela)
j.grid(column=0, row=1)


ed= Button(janela,text="buscar Pesquisa",command= pesquisar)
ed.grid(column=0, row=2)


janela.mainloop()
