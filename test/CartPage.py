import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver


class CartPage:

    def __init__(self, driver: WebDriver) -> None:
        self.__driver = driver

    @allure.step("Получить текущий URL")
    def get_current_url(self) -> str:
        return self.__driver.current_url

    @allure.step("Получить название фильма")
    def result_name(self) -> str:
        WebDriverWait(self.__driver, 15).until(
            EC.visibility_of_element_located((
                By.XPATH, "//span[text()='Аватар (2009)']")))
        result = self.__driver.find_element(
            By.XPATH, "//span[text()='Аватар (2009)']").text
        return result

    @allure.step("Перейти к просмотру отзывов")
    def get_feedback(self) -> str:
        (WebDriverWait(self.__driver, 15).until(
            EC.visibility_of_element_located((
                By.CSS_SELECTOR, "#reviewCountLight"))))
        (self.__driver.find_element(By.CSS_SELECTOR, "#reviewCountLight")
         ).click()
        total = self.wait.until(EC. visibility_of_element_located((
            By.CLASS_NAME, "styles_count__09zG8"))).text
        return total

    @allure.step("Перейти к просмотру актера")
    def get_actor(self) -> str:
        feedbacks = (WebDriverWait(self.__driver, 15).until(
            EC.visibility_of_element_located((
                By.CLASS_NAME, "styles_list__ByeEF"))))
        fields = feedbacks.find_elements(By.TAG_NAME, 'li')
        actor = fields[1].text
        return actor
