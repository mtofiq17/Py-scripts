import Login
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

'''Connecting with driver'''
driver = webdriver.Chrome(executable_path=r"C:\Driver\chromedriver.exe")

'''Go to website'''
driver.get("https://recruit.engyj.com/login")
get_url = driver.current_url
print(get_url)

'''Login '''

driver.find_element_by_name("email").send_keys("sohail.sabaseo@gmail.com")
driver.find_element_by_name("password").send_keys("123456")
driver.find_element_by_id("save-form").click()
Login.cl_login.fn_login()

try:
    elem = driver.find_element_by_class_name("invalid-feedback")
    if elem.is_displayed():
        pass
    else:
        print("Error")
except NoSuchElementException:
    print('Login successful')