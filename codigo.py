# pip install pyautogui
import pyautogui
import time
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
# Passo a passo do seu programa
# Passo 1:Entrar no sistema da empresa
# Abrir Navegador
pyautogui.PAUSE = 0.5
pyautogui.press("win")
pyautogui.write("Microsoft Edge")
pyautogui.press("enter")


# Passo 2: Fazer login no sistema da empresa
pyautogui.write(link)
pyautogui.press("enter")
# Fazer uma pausa maior para o site carregar
time.sleep(3) # pyautogui hashtag
pyautogui.click(x=660, y=456) # Clicar em um campo específico
pyautogui.write("pythonimpressionador@gmail.com")
pyautogui.press("tab") # Passar para o próximo campo
pyautogui.write("python123")
pyautogui.press("tab") # Passar para o próximo campo
pyautogui.press("enter")
# Fazer uma pausa maior para o site carregar
time.sleep(3)

# Passo 3: Abrir a base de dados (importar o arquivo)
# pip install pandas openpyxl
import pandas
tabela = pandas.read_csv("produtos.csv")
print(tabela)

for linha in tabela.index:
# Passo 4: Cadastrar 1 produto
    pyautogui.click(x=709, y=307)
    codigo = str(tabela.loc[linha, "codigo"])
    # PRODUTO
    pyautogui.write(codigo)
    pyautogui.press("tab")
    marca = str(tabela.loc[linha, "marca"])
    # MARCA
    pyautogui.write(marca)
    pyautogui.press("tab")
    tipo = str(tabela.loc[linha, "tipo"])
    # TIPO
    pyautogui.write(tipo)
    pyautogui.press("tab")
    #CATEGORIA
    categoria = str(tabela.loc[linha, "categoria"])
    pyautogui.write(categoria)
    pyautogui.press("tab")
    preco = str(tabela.loc[linha, "preco_unitario"])
    # PRECO
    pyautogui.write(preco)
    pyautogui.press("tab")
    custo = str(tabela.loc[linha, "custo"])
    # CUSTO
    pyautogui.write(custo)
    pyautogui.press("tab")
    obs = str(tabela.loc[linha, "obs"])
    if obs != "nan":
        pyautogui.write(obs)
    # OBS
    pyautogui.press("tab")  

    pyautogui.press("enter")
    # Voltar para o inicio da tela
    pyautogui.scroll(5000)
# Passo 5: Repetir o passo 4 até acabar a lista de produtos