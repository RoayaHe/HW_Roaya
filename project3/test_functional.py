from selenium.webdriver.common.by import By
import pytest

# @pytest.mark.functional
# class TestFunction:
#     def test_add_movie(self, setup):
#         setup.get("http://127.0.0.1:5000/")
#         setup.find_element(By.XPATH, "//button[text()='Add Movie']").click()
#         setup.find_element(By.XPATH, "//input[@name='filename']").send_keys("C:/Users/roaya/OneDrive/Desktop/nostringsattached.jpg")
#         setup.find_element(By.XPATH, "//input[@name='movie_title']").send_keys("No Strings Attached")
#         setup.find_element(By.XPATH, "//textarea[@name='description']").send_keys("Starring Natalie Portman and Ashton Kutcher, the film is about two friends who decide to make a pact to have a 'no strings attached' relationship, without falling in love with each other.")
#         setup.find_element(By.XPATH, "//input[@name='director']").send_keys("Ivan Reitman")
#         setup.find_element(By.XPATH, "//input[@name='release_year']").send_keys("2011")
#         setup.find_element(By.XPATH, "//textarea[@name='main_actors']").send_keys("Natalie Portman, Ashton Kutcher, Greta Gerwig, Kevin kline")
#         setup.find_element(By.XPATH, "//input[@name='proper_age']").send_keys("+17")
#         setup.find_element(By.XPATH, "//input[@name='budget']").send_keys("$25 Million")
#         setup.find_element(By.XPATH, "//input[@name='genre']").send_keys("Romance, Comedy")
#         setup.find_element(By.XPATH, "//input[@name='duration']").send_keys("1h 50m")
#         setup.find_element(By.XPATH, "//input[@name='video']").send_keys("https://www.youtube.com/embed/v=XGmsRMvQ2AM")
#         setup.find_element(By.XPATH, "//button[text()='Add Movie']").click()
#         setup.find_element(By.XPATH, "//img[@src='/display/nostringsattached_ffAuLoYeyh.jpg']").click()
#         print(setup.find_element(By.XPATH, "//img[@src='/display/nostringsattached_ffAuLoYeyh.jpg']").text)
#         assert setup.find_element(By.XPATH, "//h1[text()='No Strings Attached']").text == "No Strings Attached"

#     def test_modify_movie(self, setup):
#         setup.get("http://127.0.0.1:5000/")
#         setup.find_element(By.XPATH, "//img[@src='/display/mammamia.jpg']").click()
#         setup.find_element(By.XPATH, "//button[text()='Update Movie']").click()
#         setup.find_element(By.XPATH, "//input[@name='movie_title']").send_keys("Mamma Mia!")
#         setup.find_element(By.XPATH, "//button[text()='Update Movie']").click()
#         print(setup.find_element(By.XPATH, "//img[@src='/display/mammamia.jpg']").text)
#         assert setup.find_element(By.XPATH, "//h1[text()='Mamma Mia!']").text == "Mamma Mia!"
#
#     def test_review(self, setup):
#         setup.get("http://127.0.0.1:5000/")
#         setup.find_element(By.XPATH, "//img[@src='../static/logo.jpg']").click()
#         setup.find_element(By.XPATH, "//img[@src='/display/thegodfather.jpg']").click()
#         setup.find_element(By.CSS_SELECTOR, "label[for='star5']").click()
#         setup.find_element(By.XPATH, "//input[@name='name']").send_keys("Don Vito Corleone")
#         setup.find_element(By.XPATH, "//textarea[@name='review_text']").send_keys("'I have learned more from the streets than in any classrooms'")
#         setup.find_element(By.XPATH, "//button[normalize-space()='Add Review']").click()
#         print(setup.find_element(By.XPATH, "//p[contains(text(),'I have learned more from the streets than in any classrooms')]").text)
#         assert setup.find_element(By.XPATH, "//p[contains(text(),'I have learned more from the streets than in any classrooms')]").text == 'I have learned more from the streets than in any classrooms'
#
#     def test_watchlist(self, setup):
#         setup.get("http://127.0.0.1:5000/")
#         setup.find_element(By.XPATH, "//img[@src='/display/straightouttacompton.jpg']").click()
#         setup.find_element(By.XPATH, "//button[text()='+MyList']").click()
#         setup.find_element(By.XPATH, "//img[@src='../static/logo.jpg']").click()
#         setup.find_element(By.XPATH, "//button[text()='My Watchlist']").click()
#         setup.find_element(By.XPATH, "//img[@src='/display/straightouttacompton.jpg']").click()
#         print(setup.find_element(By.XPATH, "//img[@src='/display/straightouttacompton.jpg']").text)
#         assert setup.find_element(By.XPATH, "//img[@src='/display/straightouttacompton.jpg']").text == "Straight Outta Compton"
#
#     def test_delete_movie(self, setup):
#         setup.get("http://127.0.0.1:5000/")
#         setup.find_element(By.XPATH, "//img[@src='../static/logo.jpg']").click()
#         setup.find_element(By.XPATH, "//img[@src='/display/nostringsattached_ffAuLoYeyh.jpg']").click()
#         setup.find_element(By.XPATH, "//button[text()='Delete Movie']").click()
