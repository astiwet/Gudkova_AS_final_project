import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement


class CartPage:

    def __init__(self, driver: WebDriver) -> None:
        self.__driver = driver
        self.wait = WebDriverWait(self.__driver, 10)

    @allure.step("Получить название фильма")
    def result_name(self) -> str:
        self.wait.until(EC.visibility_of_element_located((
                By.XPATH, "//span[text()='Аватар (2009)']")))
        result = self.__driver.find_element(
            By.XPATH, "//span[text()='Аватар (2009)']").text
        return result

    @allure.step("Найти отзывы")
    def get_feedback(self) -> str:
        count = self.wait.until(EC.visibility_of_element_located((
                By.XPATH, "//button[contains(@aria-label, "
                "'Перейти к рецензиям')]")))
        total = count.text
        return total

    @allure.step("Перейти к просмотру актера")
    def get_actor(self) -> str:
        feedbacks = self.wait.until(
            EC.visibility_of_element_located((
                By.CLASS_NAME, "styles_list__ByeEF")))
        fields: list[WebElement] = feedbacks.find_elements(By.TAG_NAME, 'li')
        actor = fields[1].text
        return actor
