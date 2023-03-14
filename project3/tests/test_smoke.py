import time
from selenium.webdriver.common.by import By
import pytest
from BaseClass import BaseClass
import logging as logger
@pytest.mark.usefixtures("setup")
@pytest.mark.smoke
class TestSmoke(BaseClass):
    def test_homepage_title(self, setup):
        logger = self.getLogger()
        setup.get("http://127.0.0.1:5000/")
        time.sleep(3)
        # setup.get_screenshot_as_file('screenshots/functional/HomepageTitle.jpg')
        assert setup.find_element(By.XPATH, "//h1[text()='MovieUniverse']").text == "MovieUniverse"
        logger.info("Smoke test case 1 - Passed!")

    def test_watchlist_title(self, setup):
        logger = self.getLogger()
        setup.get("http://127.0.0.1:5000/")
        setup.find_element(By.XPATH, "//button[text()='My Watchlist']").click()
        time.sleep(3)
        # setup.get_screenshot_as_file('screenshots/functional/WatchlistTitle.jpg')
        assert setup.find_element(By.XPATH, "//h1[text()='My Watchlist']").text == "My Watchlist"
        logger.info("Smoke test case 2 - Passed!")

    def test_add_movie_title(self, setup):
        logger = self.getLogger()
        setup.get("http://127.0.0.1:5000/")
        setup.find_element(By.XPATH, "//button[text()='Add Movie']").click()
        time.sleep(3)
        # setup.get_screenshot_as_file('screenshots/functional/AddMovieTitle.jpg')
        assert setup.find_element(By.XPATH, "//label[text()='Add Movie']").text == "Add Movie"
        logger.info("Smoke test case 3 - Passed!")


    def test_update_movie_title(self, setup):
        logger = self.getLogger()
        setup.get("http://127.0.0.1:5000/")
        setup.find_element(By.XPATH, "//div/a[1]/img[1]").click()
        time.sleep(3)
        setup.execute_script("window.scrollBy(0, document.body.scrollHeight);")
        setup.find_element(By.XPATH, "//button[normalize-space()='Update Movie']").click()
        time.sleep(3)
        # setup.get_screenshot_as_file('screenshots/functional/UpdateMovieTitle.jpg')
        assert setup.find_element(By.XPATH, "//label[normalize-space()='Update Movie']").text == "Update Movie"
        logger.info("Smoke test case 4 - Passed!")

    def test_buttons_are_clickable(self, setup):
        logger = self.getLogger()
        setup.get("http://127.0.0.1:5000/")
        setup.find_element(By.XPATH, "//button[normalize-space()='My Watchlist']").click()
        assert setup.find_element(By.XPATH, "//h1[normalize-space()='My Watchlist']").text == "My Watchlist"
        time.sleep(2)
        # setup.get_screenshot_as_file('screenshots/functional/WatchlistPage.jpg')
        setup.find_element(By.XPATH, "//img[@src='../static/logo.jpg']").click()
        time.sleep(2)
        setup.find_element(By.XPATH, "//button[normalize-space()='Add Movie']").click()
        time.sleep(2)
        # setup.get_screenshot_as_file('screenshots/functional/AddMoviePage.jpg')
        assert setup.find_element(By.XPATH, "//button[normalize-space()='Add Movie']") .text== "Add Movie"
        logger.info("Smoke test case 5 - Passed!")