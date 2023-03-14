from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
service_obj = Service("chromedriver_win32/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj, options=chrome_options)
driver.implicitly_wait(3)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.find_element(By.XPATH, "//div[@class='form-group']//input[@name='name']").send_keys("Roaya Heib")
#CopyingEmailFromAnotherWebsite
driver.get("https://rahulshettyacademy.com/loginpagePractise/")
driver.find_element(By.LINK_TEXT, "Free Access to InterviewQues/ResumeAssistance/Material").click()
WindowsOpened = driver.window_handles
driver.switch_to.window(WindowsOpened[1])
Email = driver.find_element(By.XPATH, "//strong/a").text
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.find_element(By.XPATH, "//input[@name='email']").send_keys(Email)
driver.find_element(By.XPATH, "//input[@id='exampleInputPassword1']").send_keys("ARandomPassword")
driver.find_element(By.XPATH, "//input[@id='exampleCheck1']").click()
dropdown = Select(driver.find_element(By.ID, "exampleFormControlSelect1"))
dropdown.select_by_visible_text("Female")
driver.find_element(By.XPATH, "//input[@id='inlineRadio1']").click()
driver.find_element(By.XPATH, "//input[@name='bday']").send_keys("04022003")
driver.find_element(By.XPATH, "//input[@value='Submit']").click()
