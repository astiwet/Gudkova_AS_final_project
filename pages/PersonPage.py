import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement


class PersonPage:

    def __init__(self, driver: WebDriver) -> None:
        self.__driver = driver
        self.wait = WebDriverWait(self.__driver, 10)

    @allure.step("Получить имя и фамилию персоны")
    def result_people_name(self) -> str:
        self.wait.until(EC.visibility_of_element_located((
                By.XPATH, "//h1[@data-tid='f22e0093']")))
        result = self.__driver.find_element(
            By.XPATH, "//h1[@data-tid='f22e0093']").text
        return result

    @allure.step("Найти фильм на странице персоны")
    def get_film(self) -> str:
        container = self.wait.until(
            EC.visibility_of_element_located((
                By.XPATH, "//div[@class='styles_panel__tOgnC']")))
        films: list[WebElement] = container.find_elements(By.TAG_NAME, 'div')
        fields: list[WebElement] = films[0].find_elements(By.TAG_NAME, 'li')
        film = fields[1].text
        return film
