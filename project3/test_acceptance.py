from selenium.webdriver.common.by import By
import pytest

@pytest.mark.acceptance
class TestAccept:
    def test_search_bar(self, setup):
        setup.get("http://127.0.0.1:5000/")
        setup.find_element(By.XPATH, "//input[@name='search_string']").send_keys("The")
        setup.find_element(By.XPATH, "//input[@value='Search Movie']").click()

    def test_update_trailer(self, setup):
        setup.get("http://127.0.0.1:5000/")
        setup.find_element(By.XPATH, "//img[@src='/display/nostringsattached_ffAuLoYeyh.jpg']").click()
        setup.find_element(By.XPATH, "//button[text()='Update Movie']").click()
        setup.find_element(By.XPATH, "//input[@name='video_link']").send_keys("https://www.youtube.com/embed/v=XGmsRMvQ2AM&t=1s")
        setup.find_element(By.XPATH, "//button[text()='Update Movie']").click()

    def test_logo_icon(self, setup):
        setup.get("http://127.0.0.1:5000/")
        setup.find_element(By.XPATH, "//img[@src='/display/scarface.jpg']").click()
        setup.find_element(By.XPATH, "//img[@src='../static/logo.jpg']").click()
        print(setup.find_element(By.XPATH, "//h1[text()='MovieUniverse']").text)
        assert setup.find_element(By.XPATH, "//h1[text()='MovieUniverse']").text == "MovieUniverse"

    def test_movies_pages(self, setup):
        setup.get("http://127.0.0.1:5000/")
        setup.find_element(By.XPATH, "//img[@src='/display/thegodfather.jpg']").click()
        print(setup.find_element(By.XPATH, "//h1[normalize-space()='The Godfather I']").text)
        assert setup.find_element(By.XPATH, "//h1[normalize-space()='The Godfather I']").text == "The Godfather I"
        setup.find_element(By.XPATH, "//img[@src='../static/logo.jpg']").click()
        setup.find_element(By.XPATH, "//img[@src='/display/theirishman.jpg']").click()
        print(setup.find_element(By.XPATH, "//h1[normalize-space()='The Irishman']").text)
        assert setup.find_element(By.XPATH, "//h1[normalize-space()='The Irishman']").text == "The Irishman"
        setup.find_element(By.XPATH, "//img[@src='../static/logo.jpg']").click()
        setup.find_element(By.XPATH, "//img[@src='/display/straightouttacompton.jpg']").click()
        print(setup.find_element(By.XPATH, "//h1[normalize-space()='Straight Outta Compton']").text)
        assert setup.find_element(By.XPATH, "//h1[normalize-space()='Straight Outta Compton']").text == "Straight Outta Compton"
        setup.find_element(By.XPATH, "//img[@src='../static/logo.jpg']").click()
        setup.find_element(By.XPATH, "//body/div/a[10]/img[1]").click()
        print(setup.find_element(By.XPATH, "//h1[normalize-space()='10 things I hate about you']").text)
        assert setup.find_element(By.XPATH, "//h1[normalize-space()='10 things I hate about you']").text == "10 things I hate about you"



