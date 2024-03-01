from selenium import webdriver
#import webdriver_manager.chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Inicjalizacja WebDrivera Chrome bez options
webdriver_path ='C:/WebDriver/chromedriver-win64/chromedriver.exe'
driver = webdriver.Chrome
# Otwarcie strony
driver.get('https://portal.ab-werkt.nl/medewerker_api/account/login')

# Czekaj na pole do wprowadzenia nazwy użytkownika
username_field = driver.find_element_by_css_selector('input[formcontrolname="userName"]')
username_field.send_keys('DominP24@interia.pl')  # Twoja nazwa użytkownika

# Czekaj na pole do wprowadzenia hasła
password_field = driver.find_element_by_css_selector('input[formcontrolname="password"]')
password_field.send_keys('dW6x8KvFbZ')  # Twoje hasło
# Kliknij przycisk Log in
login_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[contains(., "Log in")]')))
login_button.click()

# Poczekaj na jakieś elementy, które wskazują na zalogowanie lub niepowodzenie logowania
# Np. możesz czekać na element, który jest wyświetlany po zalogowaniu, np. witamy komunikat
# Szukanie elementu katalogu przez wybór właściwego selektora

welcome_message = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'wiadomosc_powitalna')))
assert 'Witaj!' in welcome_message.text, "Nieudane logowanie!"

# Wylogowanie (może się różnić w zależności od strony)
# logout_button = driver.find_element_by_id('przycisk_wylogowania')
# logout_button.click()

# Zamknięcie przeglądarki
driver.quit()
