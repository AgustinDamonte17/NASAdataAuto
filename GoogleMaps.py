from selenium import webdriver
from selenium.webdriver.common.by import By  # Importar By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service  # Para manejar el Service
from selenium.webdriver.chrome.options import Options  # Para agregar opciones al navegador
from webdriver_manager.chrome import ChromeDriverManager  # WebDriver Manager para gestionar el ChromeDriver
import time

def obtener_coordenadas(ubicacion):
    # Configurar las opciones del navegador
    opciones = Options()
    opciones.add_argument("--start-maximized")  # Abrir en pantalla completa
    opciones.add_argument("--disable-infobars")  # Deshabilitar mensajes de info de Selenium
    opciones.add_argument("--disable-extensions")  # Deshabilitar extensiones

    # Usar WebDriver Manager para instalar el ChromeDriver automáticamente
    servicio = Service(ChromeDriverManager().install())
    
    # Iniciar el navegador usando el ChromeDriver Manager y las opciones configuradas
    navegador = webdriver.Chrome(service=servicio, options=opciones)

    try:
        # Abrir Google Maps
        navegador.get("https://www.google.com/maps")

        # Esperar a que Google Maps cargue completamente
        time.sleep(3)

        # Encontrar la barra de búsqueda
        barra_busqueda = navegador.find_element(By.ID, "searchboxinput")

        # Insertar la ubicación en la barra de búsqueda y presionar Enter
        barra_busqueda.send_keys(ubicacion)
        barra_busqueda.send_keys(Keys.ENTER)

        # Esperar un momento para que se muestren los resultados
        time.sleep(5)

        # Obtener la URL actual, que contiene las coordenadas en ella
        url_actual = navegador.current_url

        # Extraer latitud y longitud de la URL
        if '/@' in url_actual:
            coords = url_actual.split('/@')[1].split(',')[0:2]
            latitud = coords[0]
            longitud = coords[1]
        else:
            latitud = None
            longitud = None

        # Mostrar latitud y longitud
        print(f"Latitud: {latitud}, Longitud: {longitud}")

        # Retornar latitud y longitud
        return latitud, longitud

    finally:
        # Cerrar el navegador
        navegador.quit()
