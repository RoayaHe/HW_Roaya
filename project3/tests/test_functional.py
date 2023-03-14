from selenium.webdriver.common.by import By
import pytest
import time
from BaseClass import BaseClass
import logging as logger
@pytest.mark.usefixtures("setup")
@pytest.mark.functional
class TestFunction(BaseClass):
    def test_add_movie(self, setup):
        logger = self.getLogger()
        setup.get("http://127.0.0.1:5000/")
        setup.find_element(By.XPATH, "//button[text()='Add Movie']").click()
        setup.find_element(By.XPATH, "//input[@name='filename']").send_keys("C:/Users/roaya/OneDrive/Desktop/nostringsattached.jpg")
        setup.find_element(By.XPATH, "//input[@name='movie_title']").send_keys("No Strings Attached")
        setup.find_element(By.XPATH, "//textarea[@name='description']").send_keys("Starring Natalie Portman and Ashton Kutcher, the film is about two friends who decide to make a pact to have a 'no strings attached' relationship, without falling in love with each other.")
        setup.find_element(By.XPATH, "//input[@name='director']").send_keys("Ivan Reitman")
        setup.find_element(By.XPATH, "//input[@name='release_year']").send_keys("2011")
        setup.find_element(By.XPATH, "//textarea[@name='main_actors']").send_keys("Natalie Portman, Ashton Kutcher, Greta Gerwig, Kevin kline")
        setup.find_element(By.XPATH, "//input[@name='proper_age']").send_keys("+17")
        setup.find_element(By.XPATH, "//input[@name='budget']").send_keys("$25 Million")
        setup.find_element(By.XPATH, "//input[@name='genre']").send_keys("Romance, Comedy")
        setup.find_element(By.XPATH, "//input[@name='duration']").send_keys("1h 50m")
        setup.find_element(By.XPATH, "//input[@name='video']").send_keys("https://www.youtube.com/embed/v=XGmsRMvQ2AM")
        setup.find_element(By.XPATH, "//button[text()='Add Movie']").click()
        setup.execute_script("window.scrollBy(0, document.body.scrollHeight);")
        time.sleep(3)
        # setup.get_screenshot_as_file('screenshots/functional/NewMovie.jpg')
        setup.find_element(By.XPATH, "//div/a[12]/img[1]").click()
        assert setup.find_element(By.XPATH, "//h1[text()='No Strings Attached']").text == "No Strings Attached"
        logger.info("Functional test case 1 - Passed!")

    def test_modify_movie(self, setup):
        logger = self.getLogger()
        setup.get("http://127.0.0.1:5000/")
        setup.find_element(By.XPATH, "//div/a[12]/img[1]").click()
        time.sleep(2)
        # setup.get_screenshot_as_file('screenshots/functional/Unupdated_Title.jpg')
        setup.find_element(By.XPATH, "//button[text()='Update Movie']").click()
        setup.find_element(By.XPATH, "//input[@name='movie_title']").send_keys("New Movie!")
        setup.find_element(By.XPATH, "//button[text()='Update Movie']").click()
        time.sleep(2)
        # setup.get_screenshot_as_file('screenshots/functional/UpdatedTitle.jpg')
        assert setup.find_element(By.XPATH, "//h1[normalize-space()='New Movie!']").text == "New Movie!"
        logger.info("Functional test case 2 - Passed!")

    def test_review(self, setup):
        logger = self.getLogger()
        setup.get("http://127.0.0.1:5000/")
        setup.find_element(By.XPATH, "//img[@src='../static/logo.jpg']").click()
        setup.find_element(By.XPATH, "//div/a[12]/img[1]").click()
        setup.execute_script("window.scrollBy(0, document.body.scrollHeight);")
        time.sleep(2)
        setup.find_element(By.XPATH, "//label[normalize-space()='5 stars']").click()
        setup.find_element(By.XPATH, "//input[@name='name']").send_keys("Don Vito Corleone")
        setup.find_element(By.XPATH, "//textarea[@name='review_text']").send_keys("I have learned more from the streets than in any classrooms")
        setup.find_element(By.XPATH, "//button[normalize-space()='Add Review']").click()
        setup.execute_script("window.scrollBy(0, document.body.scrollHeight);")
        time.sleep(3)
        # setup.get_screenshot_as_file('screenshots/functional/NewReview.jpg')
        assert setup.find_element(By.XPATH, "//p[last()]").is_displayed()
        logger.info("Functional test case 3 - Passed!")

    def test_watchlist(self, setup):
        logger = self.getLogger()
        setup.get("http://127.0.0.1:5000/")
        setup.find_element(By.XPATH, "//img[@src='/display/straightouttacompton.jpg']").click()
        setup.find_element(By.XPATH, "//button[text()='+MyList']").click()
        setup.find_element(By.XPATH, "//img[@src='../static/logo.jpg']").click()
        setup.find_element(By.XPATH, "//button[text()='My Watchlist']").click()
        setup.find_element(By.XPATH, "//img[@src='/display/straightouttacompton.jpg']").is_displayed()
        time.sleep(2)
        # setup.get_screenshot_as_file('screenshots/functional/NewMovieAddedToWatchlist.jpg')
        setup.find_element(By.XPATH, "//img[@src='/display/straightouttacompton.jpg']").click()
        assert setup.find_element(By.XPATH, "//h1[normalize-space()='Straight Outta Compton']").text == "Straight Outta Compton"
        logger.info("Functional test case 4 - Passed!")

    def test_delete_movie(self, setup):
        logger = self.getLogger()
        setup.get("http://127.0.0.1:5000/")
        Homepage_img_elements_before = setup.find_elements(By.XPATH, "//div//img")
        setup.execute_script("window.scrollBy(0, document.body.scrollHeight);")
        setup.find_element(By.XPATH, "//div/a[12]/img[1]").click()
        time.sleep(2)
        setup.find_element(By.XPATH, "//button[normalize-space()='Delete Movie']").click()
        setup.find_element(By.XPATH, "//img[@src='../static/logo.jpg']").click()
        time.sleep(2)
        Homepage_img_elements_after = setup.find_elements(By.XPATH, "//div//img")
        assert len(Homepage_img_elements_after) <= len(Homepage_img_elements_before)
        logger.info("Functional test case 5 - Passed!")
