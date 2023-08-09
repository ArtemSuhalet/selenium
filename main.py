import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from twocaptcha import TwoCaptcha

def captcha_solution(path) -> str:
    solver = TwoCaptcha('api_key')

    try:
        result = solver.normal(path)

    except Exception as e:
        sys.exit(e)

    else:
        return sys.exit(str(result))
    #return solver.get_result(result)


service = Service(executable_path='/Users/mymacbook/PycharmProjects/pythonProject/selenium/firefoxdriver')
options = webdriver.FirefoxOptions()
driver = webdriver.Firefox(service=service, options=options)
# service = Service(executable_path='/Users/mymacbook/PycharmProjects/pythonProject/selenium/chromedriver')
# options = webdriver.ChromeOptions()
# driver = webdriver.Chrome(service=service, options=options)
URL = 'ссылка на встречу'
driver.get("https://accounts.google.com/signin")

# Вход в аккаунт Google
email_elem = driver.find_element("xpath", "//input[@type='email']")
email_elem.send_keys("artem.s@gart.tech")
email_elem.send_keys(Keys.RETURN)
time.sleep(2)  # Добавлено для паузы

#Получение изображения капчи
captcha_image_element = driver.find_element('css selector','#captchaimg')
captcha_image_url = captcha_image_element.get_attribute('src')
print(captcha_image_url)

#Получение решения капчи & Ввод решения капчи
captcha_input_element = driver.find_element('xpath', '//*[@id="ca"]')
captcha_input_element.send_keys(captcha_solution(captcha_image_url))
captcha_input_element.send_keys(Keys.RETURN)


password_elem = driver.find_element("xpath","//input[@type='password']")
password_elem.send_keys("")
password_elem.send_keys(Keys.RETURN)
time.sleep(2)  # Добавлено для паузы

# Переход к встрече Google Meet
driver.get(URL)
time.sleep(5)  # Дайте странице время для загрузки

# Присоединение к встрече
join_button = driver.find_element("xpath","//*[@id="'xDetDlgVideo'"]/div[2]/div/div[1]/span/a")
join_button.click()


#Закрыть браузер после окончания встречи
driver.quit()
