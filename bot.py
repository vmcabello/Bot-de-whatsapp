import pyautogui
import time
import hashlib
import pytesseract
from PIL import Image
import re

# Definindo as variáveis globais
mensagens_respondidas = set()

# Função para capturar a tela e retornar o texto via OCR
def capturar_e_transcrever_texto():
    x, y, largura, altura = 618, 844, 800, 68
    screenshot = pyautogui.screenshot(region=(x, y, largura, altura))
    texto = pytesseract.image_to_string(screenshot, lang='por')
    return texto

# Função para gerar um hash único para o texto
def hash_texto(texto):
    return hashlib.sha256(texto.encode('utf-8')).hexdigest()

# Função para verificar se o texto atende aos critérios para resposta
def deve_responder(texto):
    if 'passo' not in texto.lower():
        return False
    if re.search(r'nova hortolândia|nh|amanda', texto, re.IGNORECASE) and not re.search(r'líder|lider|emergencia|covas|psa|vermelha|emergência|rosolem|rosolém', texto, re.IGNORECASE):
        hash_msg = hash_texto(texto)
        if hash_msg not in mensagens_respondidas:
            mensagens_respondidas.add(hash_msg)
            return True
    return False

# Função para responder a mensagem
def responder_mensagem():
    campo_texto_x, campo_texto_y = 1043, 967
    pyautogui.click(campo_texto_x, campo_texto_y)
    pyautogui.write('Pego')
    pyautogui.press('enter')

# Função para verificar e clicar na seta, se necessário
def verificar_e_clicar_seta():
    caminho_icone_seta = r"C:\\Users\\cabel\\Desktop\\teste\\bot\\imagens\\seta.png"
    try:
        # Tenta localizar a seta na tela dentro da região especificada
        localizacao_seta = pyautogui.locateCenterOnScreen(caminho_icone_seta, region=(1818, 848, 73, 66), confidence=0.8)
        if localizacao_seta:
            pyautogui.click(localizacao_seta)
    except pyautogui.ImageNotFoundException:
        # Se a seta não for encontrada, simplesmente continua a execução do script sem fazer nada
        pass


# Loop principal do bot
while True:
    verificar_e_clicar_seta()  # Verifica e clica na seta antes de capturar e responder
    texto = capturar_e_transcrever_texto()
    if texto and deve_responder(texto):
        responder_mensagem()
    time.sleep(1)
