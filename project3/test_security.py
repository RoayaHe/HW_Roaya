from selenium.webdriver.common.by import By
import pytest

@pytest.mark.security
class TestSecurity:
    def test_ending_of_file(self, setup):
        setup.get("http://127.0.0.1:5000/")
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
            setup.find_element(By.XPATH, "//img[@src='/display/nostringsattached_ffAuLoYeyh.jpg']").click()
            print(setup.find_element(By.XPATH, "//img[@src='/display/nostringsattached_ffAuLoYeyh.jpg']").text)
            assert setup.find_element(By.XPATH, "//h1[text()='No Strings Attached']").text == "No Strings Attached"