
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver


class PersonPage:

    def __init__(self, driver: WebDriver) -> None:
        self.__driver = driver

    def get_current_url(self) -> str:
        return self.__driver.current_url
    
    def result_p_name(self) -> str:
        WebDriverWait(self.__driver, 15).until(
            EC.visibility_of_element_located((
                By.XPATH, "//h1[text()='Мария Миронова']")))
        result = self.__driver.find_element(
            By.XPATH, "//h1[text()='Мария Миронова']").text
        return result

    def get_film(self) -> str:
        films = (WebDriverWait(self.__driver, 30).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "#bestMovies")))
            )
        fields = films.find_elements(By.TAG_NAME, 'li')
        film = fields[3].text
        return film.text
