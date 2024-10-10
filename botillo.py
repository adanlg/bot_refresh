import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from playsound import playsound  # Import playsound para reproducir el sonido

# Set options for Chromium
options = webdriver.ChromeOptions()
options.binary_location = "/usr/bin/chromium-browser"  # Path to Chromium browser

# Dejar que inicies sesión manualmente
options.add_argument("user-data-dir=/home/luis/snap/chromium/current/.config/chromium")  # Ajustar si es necesario

# Configurar el driver de Chromium
service = Service("/usr/lib/chromium-browser/chromedriver")  # Ajusta este path si es necesario
driver = webdriver.Chrome(service=service, options=options)

# Abre Chromium y deja que navegues manualmente
driver.get("https://www.google.com")  # Inicia con cualquier página (puedes cambiarla)

# Esperar hasta que estés listo para empezar
input("Inicia sesión, ve a la página deseada, y escribe 'empieza' para iniciar el bot: ")

print("El bot está funcionando...")

# Empieza el ciclo de refresco
while True:
    try:
        # Refrescar la página cada 10 segundos
        time.sleep(10)
        driver.refresh()

        # Esperar hasta que la página se haya cargado completamente
        time.sleep(5)  # Esperar 5 segundos adicionales para asegurarse de que todo se haya cargado

        # Revisa si el texto "Tren Completo" está en el contenido de la página
        page_source = driver.page_source  # Obtener todo el código HTML de la página

        # Si no encuentra "Tren Completo", significa que hay billetes disponibles
        if "Tren Completo" not in page_source:
            print("¡Hay billetes disponibles! ¡Reserva ahora!")
            # Reproduce la alarma descargada
            playsound('alarm-26718.mp3')  # Reemplaza con el archivo de alarma que descargaste
            print("Hemos acabado")
            break
        else:
            print("El tren sigue completo.")

    except Exception as e:
        print(f"Error: {e}")

# No cerrar el navegador automáticamente
