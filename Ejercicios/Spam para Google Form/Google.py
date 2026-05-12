"""
Script mejorado para rellenar un Google Form a partir de respuestas ordenadas.
Instrucciones:
- Pega la URL de tu formulario en `FORM_URL`.
- Rellena `datas` con listas ordenadas de respuestas (en el mismo orden
  que aparecen las preguntas en el formulario). Para opciones (radio/checkbox)
  usa el texto exacto de la opción.
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os


FORM_URL = "https://docs.google.com/forms/d/e/1FAIpQLSeCcy6eUjJ1Gq3XWOVR5Qd4_Zv9Y7ddOT3EAc9mziob8MrO8Q/viewform?usp=publish-editor"

# Ejemplo de datos: cada sublista es una respuesta completa (una fila a enviar)
# Debes adaptar las respuestas al orden de las preguntas en tu formulario.
datas = [
    [
        "25",  # 1. Edad (texto o la opción exacta)
        "Educación universitaria en curso",  # 2. Grado de instrucción
        "Estudiante",  # 3. Ocupación
        "Soltero (a)",  # 4. Estado civil
        "Masculino",  # 5. Género
        "Zona urbana",  # 6. Lugar de residencia
        "Satisfecho",  # 7. Satisfacción espacio
        "Adaptable con algunas limitaciones",  # 8. Adaptabilidad
        "Muy importante",  # 9. Reorganizar fácil
        "Adecuada pero mejorable",  # 10. Eficiencia distribución
        "Muy importante",  # 11. Optimizar uso
        "Cómodo con algunas incomodidades",  # 12. Comodidad
        "Influye de manera significativa",  # 13. Influencia en productividad
        "Muy importante",  # 14. Muebles modulares
        "Muy útil",  # 15. Espacio que se adapte
        "Muy importante",  # 16. Integración de tecnología
        "Muy importante",  # 17. Espacio multifuncional
        "Mucho",  # 18. Transformar rápido
        "Muy necesario",  # 19. Innovar espacios
        "Muy dispuesto",  # 20. Disposición a usar
        "Medio",  # 21. Nivel de inversión
        "Muy beneficioso",  # 22. Beneficios de combinar funciones
    ],
]


def fill_form(driver, answers):
    wait = WebDriverWait(driver, 10)

    # Esperar que se carguen posibles campos de texto
    time.sleep(1)

    # Índice para rellenar inputs/textarea en orden (cuando existan)
    text_index = 0

    # Recolectar campos de texto y áreas (puede variar según versión de Forms)
    text_fields = driver.find_elements(By.CSS_SELECTOR, 'input[type="text"], input[type="email"], input[type="tel"], textarea')

    for answer in answers:
        # Primero intentar completar un campo de texto si queda alguno
        if text_index < len(text_fields):
            try:
                elem = text_fields[text_index]
                elem.click()
                elem.clear()
                elem.send_keys(answer)
                text_index += 1
                continue
            except Exception:
                # si falla continuar y probar selección por texto
                text_index += 1

        # Intentar seleccionar una opción (radio/checkbox) buscando por texto exacto
        try:
            # Buscar un span que contenga exactamente el texto de la respuesta
            option = driver.find_element(By.XPATH, f"//span[normalize-space()=\"{answer}\"]")
            # Subir al elemento clicable más cercano
            clickable = option
            for _ in range(4):
                parent = clickable.find_element(By.XPATH, '..')
                if parent.get_attribute('role') in ('radio', 'checkbox', 'option') or parent.tag_name == 'label' or parent.get_attribute('role') == 'button':
                    parent.click()
                    break
                clickable = parent
            else:
                try:
                    option.click()
                except Exception:
                    pass
        except Exception:
            # Si no se encuentra la opción por texto, intentar clickear el primer radio disponible
            try:
                radios = driver.find_elements(By.CSS_SELECTOR, 'div[role="radiogroup"] div[role="radio"]')
                if radios:
                    radios[0].click()
            except Exception:
                pass


def submit_and_prepare_another(driver):
    # Intentar encontrar botón Enviar/Submit
    try:
        submit = driver.find_element(By.XPATH, "//span[text()='Enviar'] | //span[text()='Submit'] | //div[@role='button' and .//span[text()='Enviar']] | //div[@role='button' and .//span[text()='Submit']]")
        submit.click()
    except Exception:
        try:
            # antiguo fallback
            submit = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div/span/span')
            submit.click()
        except Exception:
            pass

    time.sleep(1)
    # Click en "Enviar otra respuesta" si existe
    try:
        another = driver.find_element(By.XPATH, "//a[contains(., 'Enviar otra respuesta') or contains(., 'Submit another response')]")
        another.click()
    except Exception:
        # intentar cerrar navegador al final si no hay más
        pass


def main():
    # Configurar opciones de Brave
    options = Options()
    options.add_argument("--start-maximized")
    options.add_argument("--disable-blink-features=AutomationControlled")
    
    # Rutas comunes de Brave en Windows
    brave_paths = [
        "C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe",
        "C:/Program Files (x86)/BraveSoftware/Brave-Browser/Application/brave.exe",
        os.path.expandvars("%ProgramFiles%/BraveSoftware/Brave-Browser/Application/brave.exe"),
        os.path.expandvars("%ProgramFiles(x86)%/BraveSoftware/Brave-Browser/Application/brave.exe"),
    ]
    
    brave_binary = None
    for path in brave_paths:
        if os.path.exists(path):
            brave_binary = path
            break
    
    if brave_binary:
        options.binary_location = brave_binary
    
    # Usar undetected-chromedriver que auto-actualiza el driver
    try:
        import undetected_chromedriver as uc
        driver = uc.Chrome(options=options, version_main=None)
    except ImportError:
        print("Instalando undetected-chromedriver...")
        import subprocess
        import sys
        subprocess.check_call([sys.executable, "-m", "pip", "install", "undetected-chromedriver"])
        import undetected_chromedriver as uc
        driver = uc.Chrome(options=options, version_main=None)
    
    driver.get(FORM_URL)

    for answers in datas:
        fill_form(driver, answers)
        submit_and_prepare_another(driver)

    driver.quit()


if __name__ == '__main__':
    main()