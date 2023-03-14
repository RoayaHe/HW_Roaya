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

#testcase1 - add new movie
driver.find_element(By.XPATH, "//button[text()='Add Movie']").click()
driver.find_element(By.XPATH, "//input[@name='filename']").send_keys("C:/Users/roaya/OneDrive/Desktop/nostringsattached.jpg")
driver.find_element(By.XPATH, "//input[@name='movie_title']").send_keys("No Strings Attached")
driver.find_element(By.XPATH, "//textarea[@name='description']").send_keys("Starring Natalie Portman and Ashton Kutcher, the film is about two friends who decide to make a pact to have a 'no strings attached' relationship, without falling in love with each other.")
driver.find_element(By.XPATH, "//input[@name='director']").send_keys("Ivan Reitman")
driver.find_element(By.XPATH, "//input[@name='release_year']").send_keys("2011")
driver.find_element(By.XPATH, "//textarea[@name='main_actors']").send_keys("Natalie Portman, Ashton Kutcher, Greta Gerwig, Kevin kline")
driver.find_element(By.XPATH, "//input[@name='proper_age']").send_keys("+17")
driver.find_element(By.XPATH, "//input[@name='budget']").send_keys("$25 Million")
driver.find_element(By.XPATH, "//input[@name='genre']").send_keys("Romance, Comedy")
driver.find_element(By.XPATH, "//input[@name='duration']").send_keys("1h 50m")
driver.find_element(By.XPATH, "//input[@name='video']").send_keys("https://www.youtube.com/embed/v=XGmsRMvQ2AM")
driver.find_element(By.XPATH, "//button[text()='Add Movie']").click()

time.sleep(5)

#testcase2 - Write a review
driver.find_element(By.XPATH, "//img[@src='../static/logo.jpg']").click()
driver.find_element(By.XPATH, "//img[@src='/display/thegodfather.jpg']").click()
time.sleep(3)
driver.find_element(By.CSS_SELECTOR, "label[for='star5']").click()
driver.find_element(By.XPATH, "//input[@name='name']").send_keys("Don Vito Corleone")
driver.find_element(By.XPATH, "//textarea[@name='review_text']").send_keys("'I have learned more from the streets than in any classrooms'")
driver.find_element(By.XPATH, "//button[normalize-space()='Add Review']").click()

time.sleep(5)

#testcase3 - Add to watchlist
driver.find_element(By.XPATH, "//img[@src='../static/logo.jpg']").click()
driver.find_element(By.XPATH, "//img[@src='/display/scentofawoman.jpg']").click()
driver.find_element(By.XPATH, "//button[text()='+MyList']").click()

time.sleep(5)

#testcase5 - Modify Movie information
driver.find_element(By.XPATH, "//img[@src='../static/logo.jpg']").click()
driver.find_element(By.XPATH, "//img[@src='/display/mammamia.jpg']").click()
driver.find_element(By.XPATH, "//button[text()='Update Movie']").click()
driver.find_element(By.XPATH, "//input[@name='movie_title']").send_keys("Mamma Mia!")
driver.find_element(By.XPATH, "//button[text()='Update Movie']").click()
driver.find_element(By.XPATH, "//img[@src='../static/logo.jpg']").click()
driver.find_element(By.XPATH, "//img[@src='/display/mammamia.jpg']").click()

time.sleep(5)

#testcase8 - Add movie twice to watchlist
driver.find_element(By.XPATH, "//img[@src='../static/logo.jpg']").click()
driver.find_element(By.XPATH, "//button[text()='My Watchlist']").click()
driver.find_element(By.XPATH, "//img[@src='../static/logo.jpg']").click()
driver.find_element(By.XPATH, "//img[@src='/display/straightouttacompton.jpg']").click()
driver.find_element(By.XPATH, "//button[text()='+MyList']").click()
driver.find_element(By.XPATH, "//img[@src='../static/logo.jpg']").click()
driver.find_element(By.XPATH, "//button[text()='My Watchlist']").click()
driver.find_element(By.XPATH, "//img[@src='../static/logo.jpg']").click()
driver.find_element(By.XPATH, "//img[@src='/display/straightouttacompton.jpg']").click()
driver.find_element(By.XPATH, "//button[text()='+MyList']").click()
driver.find_element(By.XPATH, "//img[@src='../static/logo.jpg']").click()
driver.find_element(By.XPATH, "//button[text()='My Watchlist']").click()

time.sleep(5)

#testcase9 - Using the search bar
driver.find_element(By.XPATH, "//img[@src='../static/logo.jpg']").click()
driver.find_element(By.XPATH, "//input[@name='search_string']").send_keys("The")
driver.find_element(By.XPATH, "//input[@value='Search Movie']").click()

time.sleep(5)

#testcase4 - Delete movie
driver.find_element(By.XPATH, "//img[@src='../static/logo.jpg']").click()
driver.find_element(By.XPATH, "//img[@src='/display/nostringsattached.jpg']").click()
driver.find_element(By.XPATH, "//button[text()='Delete Movie']").click()