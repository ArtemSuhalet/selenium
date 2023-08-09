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
#whisper
#url = "https://calendar.google.com/"
# url = 'https://drive.google.com/file/d/1mOHre6TCgEin3qEqmSjzKf5OzwsSPIA3/view?usp=drivesdk'
# try:
#     driver.get(url)
#     #button = driver.find_element_by_xpath("/html/body/main/section[1]/div[1]/header/div/div[2]/a")
#     # button = driver.find_element("xpath", "/html/body/main/section[1]/div[1]/header/div/div[2]/a")
#     # button.click()
#     # input_tab = WebDriverWait(driver, 10).until(
#     #     EC.presence_of_element_located((By.ID("identifierId")))
#     # )
#     #input_tab = driver.find_element(By.CSS_SELECTOR, '#identifierId')
#     #input_tab = driver.find_element(By.ID('identifierId'))
#     #print(input_tab)
#     #input_tab = driver.find_element(By.CLASS_NAME, 'whsOnd')
#     #input_tab = driver.find_element("xpath", "//*[@id=identifierId]")
#     #input_tab.send_keys('artem.s@gart.tech')
#
#     #input_tab.send_keys(Keys.ENTER)
#     #button2 = driver.find_element("xpath", "//button[@class='VfPpkd-vQzf8d']")
#    # button2.click()
#
# # try:
# #     driver.get(url)
# #     #element = driver.find_element_by_xpath("//button[@class='example']")#???????
# #     #element2 = driver.find_element_by_link_text('Gart tech - regular LLM check in').get_attribute('href')
# except Exception as ex:
#      print(ex)
#
# finally:
#     #driver.close()
#     driver.quit()

#
# https://meet.google.com/jxj-kxra-yff?authuser=0&hs=122
# //*[@id="xDetDlgVideo"]/div[2]/div/div[1]/span/a

