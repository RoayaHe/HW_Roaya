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
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("http://127.0.0.1:5000/")

#testcase6 - Same image for 2 movies, delete one movie
driver.find_element(By.XPATH, "//img[@src='../static/logo.jpg']").click()
driver.find_element(By.XPATH, "//img[@src='/display/nostringsattached.jpg']").click()
driver.find_element(By.XPATH, "//button[text()='Update Movie']").click()
driver.find_element(By.XPATH, "//input[@name='filename']").send_keys("C:/Users/roaya/OneDrive/Desktop/nostringsattached.jpg")
driver.find_element(By.XPATH, "//button[text()='Update Movie']").click()
driver.find_element(By.XPATH, "//img[@src='../static/logo.jpg']").click()
driver.find_element(By.XPATH, "//img[@src='/display/mammamia.jpg']").click()
driver.find_element(By.XPATH, "//button[text()='Update Movie']").click()
driver.find_element(By.XPATH, "//input[@name='filename']").send_keys("C:/Users/roaya/OneDrive/Desktop/nostringsattached.jpg")
driver.find_element(By.XPATH, "//button[text()='Update Movie']").click()
driver.find_element(By.XPATH, "//img[@src='../static/logo.jpg']").click()
driver.find_element(By.XPATH, "//img[@src='/display/nostringsattached.jpg']").click()
driver.find_element(By.XPATH, "//button[text()='Delete Movie']").click()

time.sleep(5)

#testcase7 - delete movie from watchlist
driver.find_element(By.XPATH, "//img[@src='../static/logo.jpg']").click()
driver.find_element(By.XPATH, "//img[@src='/display/goodwillhunting.jpg']").click()
driver.find_element(By.XPATH, "//button[text()='+MyList']").click()
driver.find_element(By.XPATH, "//img[@src='../static/logo.jpg']").click()
driver.find_element(By.XPATH, "//button[text()='My Watchlist']").click()
driver.find_element(By.XPATH, "//img[@src='/display/goodwillhunting.jpg']").click()
driver.find_element(By.XPATH, "//button[text()='Delete from watchlist']").click()

time.sleep(5)

#testcase10 - update movie trailer
driver.find_element(By.XPATH, "//img[@src='../static/logo.jpg']").click()
driver.find_element(By.XPATH, "//img[@src='/display/nostringsattached.jpg']").click()
driver.find_element(By.XPATH, "//button[text()='Update Movie']").click()
driver.find_element(By.XPATH, "//input[@name='video_link']").send_keys("https://www.youtube.com/watch?v=XGmsRMvQ2AM")
driver.find_element(By.XPATH, "//button[text()='Update Movie']").click()