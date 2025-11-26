import pyautogui
import time

pyautogui.FAILSAFE = True   # segurança

# Tempo para preparar ambiente (abrir navegador e deixar visível)
time.sleep(3)

# PASSO 1 – Ativar o navegador
pyautogui.click(200, 200)   # clique em qualquer parte da janela do navegador

# PASSO 2 – Abrir Google
pyautogui.hotkey("ctrl", "l")   # seleciona barra de endereço
time.sleep(0.5)
pyautogui.write("https://www.google.com")
pyautogui.press("enter")

time.sleep(3)  # aguarda carregar

# PASSO 3 – Pesquisar clima
pyautogui.write("Clima hoje na minha cidade")
pyautogui.press("enter")

time.sleep(4)  # aguarda previsão carregar

# PASSO 4 – Screenshot da previsão
screenshot = pyautogui.screenshot()
screenshot.save("previsao.png")

print("Automação concluída e imagem salva como previsao.png")
