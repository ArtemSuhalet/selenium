import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
#from selenium.webdriver.firefox.service import Service
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import requests
from twocaptcha import TwoCaptcha

def captcha_solution(path) -> str:
    API_KEY = 'b17e9e7e489fe791be1d7f6adce300e6'
    CAPTCHA_IMAGE_URL = path

    # Запрос на отправку капчи на 2Captcha
    response = requests.post(
        f"http://2captcha.com/in.php?key={API_KEY}&method=base64&body={CAPTCHA_IMAGE_URL}&json=1"
    )

    request_result = response.json()

    if request_result['status'] == 1:
        request_id = request_result['request']
        print(f"Request ID: {request_id}")

        # Ожидание решения капчи
        solution = None
        max_attempts = 10
        for _ in range(max_attempts):
            solution_response = requests.get(
                f"http://2captcha.com/res.php?key={API_KEY}&action=get&id={request_id}&json=1")
            solution_result = solution_response.json()
            if solution_result['status'] == 1:
                solution = solution_result['request']
                break

        if solution:
            print(f"Captcha solution: {solution}")
            return solution
        else:
            print("Captcha solution not found")
    else:
        print("Error occurred:", request_result['request'])

# def captcha_solution(path) -> str:
#     solver = TwoCaptcha('b17e9e7e489fe791be1d7f6adce300e6')
#
#     try:
#         result = solver.normal(path)
#
#     except Exception as e:
#         print(e)
#
#     else:
#         code = result['code']
#         #return str(result)
#         return code
#     #return solver.get_result(result)


# service = Service(executable_path='/Users/mymacbook/PycharmProjects/pythonProject/selenium/firefoxdriver')
# options = webdriver.FirefoxOptions()
# driver = webdriver.Firefox(service=service, options=options)
service = Service(executable_path='/Users/mymacbook/PycharmProjects/pythonProject/selenium/chromedriver')
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)
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
time.sleep(5)

#Получение решения капчи & Ввод решения капчи
captcha_input_element = driver.find_element('xpath', '//*[@id="ca"]')
captcha_input_element.send_keys(captcha_solution(captcha_image_url))
#captcha_input_element.send_keys(str(123456))
captcha_input_element.send_keys(Keys.RETURN)
time.sleep(5)

password_elem = driver.find_element("xpath","//input[@type='password']")
password_elem.send_keys("")
password_elem.send_keys(Keys.RETURN)
time.sleep(5)  # Добавлено для паузы

# Переход к встрече Google Meet
driver.get(URL)
time.sleep(5)  # Дайте странице время для загрузки

# Присоединение к встрече
join_button = driver.find_element("xpath","//*[@id="'xDetDlgVideo'"]/div[2]/div/div[1]/span/a")
join_button.click()


#Закрыть браузер после окончания встречи
driver.quit()
