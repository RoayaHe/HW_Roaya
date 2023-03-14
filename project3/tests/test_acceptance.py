from selenium.webdriver.common.by import By
import pytest
import time
from BaseClass import BaseClass
import logging as logger
@pytest.mark.usefixtures("setup")
@pytest.mark.acceptance
class TestAccept(BaseClass):
    def test_search_bar(self, setup):
        logger = self.getLogger()
        setup.get("http://127.0.0.1:5000/")
        setup.find_element(By.XPATH, "//input[@name='search_string']").send_keys("The")
        setup.find_element(By.XPATH, "//input[@value='Search Movie']").click()
        time.sleep(3)
        # setup.get_screenshot_as_file('HomeWorks/project3/screenshots/acceptance/SearchBar.jpg')
        img_elements = setup.find_elements(By.XPATH, "//img[@class='image']")
        assert len(img_elements) == 4
        logger.info("Acceptance test case 1 - Passed!")

    def test_update_trailer(self, setup):
        logger = self.getLogger()
        setup.get("http://127.0.0.1:5000/")
        setup.find_element(By.XPATH, "//body/div/a[11]/img[1]").click()
        time.sleep(2)
        setup.find_element(By.XPATH, "//button[normalize-space()='Update Movie']").click()
        setup.find_element(By.XPATH, "//input[@name='video_link']").send_keys("https://www.youtube.com/embed/v=OXrcDonY-B8&t=1s")
        setup.find_element(By.XPATH, "//button[normalize-space()='Update Movie']").click()
        time.sleep(2)
        # setup.get_screenshot_as_file('HomeWorks/project3/screenshots/acceptance/MovieTrailer.jpg')
        assert setup.find_element(By.XPATH, "//div/iframe").is_displayed()
        logger.info("Acceptance test case 2 - Passed!")

    def test_logo_icon(self, setup):
        logger = self.getLogger()
        setup.get("http://127.0.0.1:5000/")
        setup.find_element(By.XPATH, "//img[@src='/display/scarface.jpg']").click()
        setup.find_element(By.XPATH, "//img[@src='../static/logo.jpg']").click()
        time.sleep(2)
        # setup.get_screenshot_as_file('HomeWorks/project3/screenshots/acceptance/TheLogoIconTest.jpg')
        assert setup.find_element(By.XPATH, "//h1[text()='MovieUniverse']").text == "MovieUniverse"
        logger.info("Acceptance test case 3 - Passed!")

    def test_movie_doesnt_exist(self, setup):
        logger = self.getLogger()
        setup.get("http://127.0.0.1:5000/")
        setup.find_element(By.XPATH, "//input[@name='search_string']").send_keys("Interstellar")
        setup.find_element(By.XPATH, "//input[@value='Search Movie']").click()
        time.sleep(2)
        # setup.get_screenshot_as_file('HomeWorks/project3/screenshots/acceptance/MovieDoesntExist.jpg')
        assert setup.find_element(By.XPATH, "//div").text == ""
        logger.info("Acceptance test case 4 - Passed!")

    def test_deleted_from_both_pages(self, setup):
        logger = self.getLogger()
        setup.get("http://127.0.0.1:5000/")
        #checking_how_many_movies_are_on_homepage_and_watchlist
        homepage_img_elements_before = setup.find_elements(By.XPATH, "//div//img")
        time.sleep(2)
        setup.find_element(By.XPATH, "//button[normalize-space()='My Watchlist']").click()
        time.sleep(2)
        watchlist_img_elements_before = setup.find_elements(By.XPATH, "//div//img")
        setup.find_element(By.XPATH, "//img[@src='../static/logo.jpg']").click()
        #adding_new_movie
        setup.find_element(By.XPATH, "//button[text()='Add Movie']").click()
        setup.find_element(By.XPATH, "//input[@name='filename']").send_keys("C:/Users/roaya/OneDrive/Desktop/nostringsattached.jpg")
        setup.find_element(By.XPATH, "//input[@name='movie_title']").send_keys("TEST")
        setup.find_element(By.XPATH, "//textarea[@name='description']").send_keys("TEST")
        setup.find_element(By.XPATH, "//input[@name='director']").send_keys("TEST")
        setup.find_element(By.XPATH, "//input[@name='release_year']").send_keys("2023")
        setup.find_element(By.XPATH, "//textarea[@name='main_actors']").send_keys("TEST")
        setup.find_element(By.XPATH, "//input[@name='proper_age']").send_keys("TEST")
        setup.find_element(By.XPATH, "//input[@name='budget']").send_keys("TEST")
        setup.find_element(By.XPATH, "//input[@name='genre']").send_keys("TEST")
        setup.find_element(By.XPATH, "//input[@name='duration']").send_keys("TEST")
        setup.find_element(By.XPATH, "//input[@name='video']").send_keys("TEST")
        setup.find_element(By.XPATH, "//button[text()='Add Movie']").click()
        time.sleep(3)
        #verifying_movie_added
        homepage_img_elements_after = setup.find_elements(By.XPATH, "//div//img")
        assert len(homepage_img_elements_before) < len(homepage_img_elements_after)
        setup.execute_script("window.scrollBy(0, document.body.scrollHeight);")
        # setup.get_screenshot_as_file('HomeWorks/project3/screenshots/acceptance/MovieInHomepage.jpg')
        #adding_to_watchlist
        setup.find_element(By.XPATH, "//img[@src='../static/logo.jpg']").click()
        time.sleep(2)
        setup.find_element(By.XPATH, "//body/div/a[12]/img[1]").click()
        time.sleep(2)
        setup.execute_script("window.scrollBy(0, document.body.scrollHeight);")
        setup.find_element(By.XPATH, "//button[normalize-space()='+MyList']").click()
        setup.find_element(By.XPATH, "//img[@src='../static/logo.jpg']").click()
        #vefirying_its_added_to_watchlist
        setup.find_element(By.XPATH, "//button[normalize-space()='My Watchlist']").click()
        time.sleep(2)
        watchlist_img_elements_after = setup.find_elements(By.XPATH, "//div//img")
        setup.get_screenshot_as_file('HomeWorks/project3/screenshots/acceptance/MovieInWatchlist.jpg')
        setup.find_element(By.XPATH, "//img[@src='../static/logo.jpg']").click()
        #deleting_the_movie
        setup.find_element(By.XPATH, "//div/a[12]/img[1]").click()
        setup.execute_script("window.scrollBy(0, document.body.scrollHeight);")
        time.sleep(2)
        setup.find_element(By.XPATH, "//button[normalize-space()='Delete Movie']").click()
        setup.find_element(By.XPATH, "//img[@src='../static/logo.jpg']").click()
        homepage_img_elements_after_delete = setup.find_elements(By.XPATH, "//div//img")
        assert len(homepage_img_elements_after_delete) < len(homepage_img_elements_after)
        logger.info("Acceptance test case 5 - Passed!")