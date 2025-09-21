import pyautogui
import time 
import pandas as pd

pyautogui.PAUSE = 0.5

# ABRINDO O CHROME
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
pyautogui.click(x=999, y=795)
pyautogui.hotkey("ctrl", "n")

# ENTRANDO NO SISTEMA
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)
pyautogui.press("enter")

# FAZENDO LOGIN NO SISTEMA
pyautogui.press("tab")
pyautogui.write("emailqualquesr@gmail.com")
pyautogui.press("tab")
pyautogui.write("senhaqualquers")
pyautogui.press("tab")
pyautogui.press("enter")


tabela = pd.read_csv("produtos.csv")

print(tabela)



for linha in tabela.index:

    # CADASTRANDO O CODIGO DO PRODUTO
    pyautogui.press("tab")
    pyautogui.click(x=1060, y=262)
    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(str(codigo))
    pyautogui.press("tab")

    # CADASTRANDO A MARCA 
    marca = tabela.loc[linha, "marca"]
    pyautogui.write(str(marca))
    pyautogui.press("tab")

    # CADASTRANDO O TIPO
    tipo = tabela.loc[linha, "tipo"]
    pyautogui.write(str(tipo))
    pyautogui.press("tab")

    # CADASTRANDO A CATEGORIA
    categoria = tabela.loc[linha, "categoria"]
    pyautogui.write(str(categoria))
    pyautogui.press("tab")

    # CADATRANDO O PREÇO UNITARIO
    preco_unitario = tabela.loc[linha, "preco_unitario"]
    pyautogui.write(str(preco_unitario))
    pyautogui.press("tab")

    # CADASTRANDO O CUSTO
    custo = tabela.loc[linha, "custo"]
    pyautogui.write(str(custo))
    pyautogui.press("tab")

    # CADASTRANDO A OBS
    obs = str(tabela.loc[linha, "obs"])

    if obs != "nan":     
        pyautogui.write(obs)
    pyautogui.press("tab")

    # CADASTRANDO O PRODUTO
    pyautogui.press("enter")
