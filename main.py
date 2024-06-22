import pyautogui
import pyperclip
import time
import os

# Declaramos las variables necesarias para hacer login. Aquí pon las tuyas.
# Se podría tomar la password desde el vault de Windows o de un vault online también.

username = 'nicezefer@gmail.com'
password = '' #Aquí, entre las comillas simples, inserta tu password.

# Configuramos de antemano la carpeta donde se almacenan las imágenes de referencia
os.chdir(os.path.join(os.path.dirname(__file__), "screenshotsElementos"))

# Funciones necesarias para el proceso
def esperar_Elemento(rutaScrElemento, timeout=5, confidence=0.8):
    start_time = time.time()
    while time.time() - start_time < timeout:
        location = pyautogui.locateCenterOnScreen(rutaScrElemento, minSearchTime=1, confidence=confidence)
        if location:
            return location
        time.sleep(0.5)
    return None
def navigate_URL(searchBarScr, URL):
    location = esperar_Elemento(searchBarScr)
    if location:
        pyautogui.click(location)
        pyautogui.write(URL)
        pyautogui.press('enter')
    else:
        print(f"No se encontró el elemento correspondiente a: {searchBarScr}")

def manipular_Cookies(cookiesDecision):
    if esperar_Elemento('WindowCookies.png', confidence=0.8):
        button = 'AceptarCookiesBtn.png' if cookiesDecision else 'RechazarCookiesBtn.png'
        location = esperar_Elemento(button, confidence=0.8)
        if location:
            pyautogui.click(location)
        else:
            print(f"Botón {button} no encontrado")
    else:
        print("Ventana de cookies no encontrada")

def hacer_Login(username, password):
    locationUsername = esperar_Elemento(r'C:\Users\nicol\OneDrive\Escritorio\InfoJobs\screenshotsElementos\FieldEmail.png', confidence=0.9)
    if locationUsername:
        pyperclip.copy(username)
        pyautogui.click(locationUsername)
        pyautogui.hotkey('ctrl', 'v')
        pyautogui.press('tab')
        pyautogui.write(password, interval=0.05)
        pyautogui.press('enter')
    else:
        print("Campo de usuario no encontrado")

def click_Elemento(rutaScrElemento):
    location = esperar_Elemento(rutaScrElemento, confidence=0.9)
    if location:
        pyautogui.click(location)
    else:
        print(f"Elemento {rutaScrElemento} no encontrado")

##########################################

os.system('start chrome --incognito --start-maximized')
time.sleep(2)

navigate_URL('SearchBarChrome.png', 'https://www.infojobs.net/candidate/candidate-login/candidate-login.xhtml?dgv=1718954201266')
#Coloco más que nada este sleep para darle tiempo a la ventana de cookies en aparecer
time.sleep(3)

if esperar_Elemento('WindowCookies.png'):
    manipular_Cookies(False)
    hacer_Login(username, password)
    time.sleep(1)
    if esperar_Elemento('MisOfertasBtn.png'):
        click_Elemento('MisOfertasBtn.png')
    else:
        print("No se pudo encontrar el botón 'Mis Ofertas'")
else:
    print("La página de login no cargó correctamente")