from selenium.webdriver.common.by import By
import pytest

@pytest.mark.smoke
class TestSmoke:
    def test_homepage_title(self, setup):
        setup.get("http://127.0.0.1:5000/")
        print(setup.find_element(By.XPATH, "//h1[text()='MovieUniverse']").text)
        assert setup.find_element(By.XPATH, "//h1[text()='MovieUniverse']").text == "MovieUniverse"

    def test_movie_title(self, setup):
        setup.get("http://127.0.0.1:5000/")
        setup.find_element(By.XPATH, "//img[@src='/display/thegodfather.jpg']").click()
        print(setup.find_element(By.XPATH, "//h1[text()='The Godfather I']").text)
        assert setup.find_element(By.XPATH, "//h1[text()='The Godfather I']").text == "The Godfather I"

    def test_watchlist_title(self, setup):
        setup.get("http://127.0.0.1:5000/")
        setup.find_element(By.XPATH, "//button[text()='My Watchlist']").click()
        print(setup.find_element(By.XPATH, "//h1[text()='My Watchlist']").text)
        assert setup.find_element(By.XPATH, "//h1[text()='My Watchlist']").text == "My Watchlist"

    def test_add_movie_title(self, setup):
        setup.get("http://127.0.0.1:5000/")
        setup.find_element(By.XPATH, "//button[text()='Add Movie']").click()
        print(setup.find_element(By.XPATH, "//label[text()='Add Movie']").text)
        assert setup.find_element(By.XPATH, "//label[text()='Add Movie']").text == "Add Movie"

    def test_update_movie_title(self, setup):
        setup.get("http://127.0.0.1:5000/")
        setup.find_element(By.XPATH, "//img[@src='/display/thegodfather.jpg']").click()
        setup.find_element(By.XPATH, "//button[text()='Update Movie']").click()
        print(setup.find_element(By.XPATH, "//label[text()='Update Movie']").text)
        assert setup.find_element(By.XPATH, "//label[text()='Update Movie']").text == "Update Movie"
