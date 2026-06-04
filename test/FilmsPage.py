import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver


class FilmsPage:

    def __init__(self, driver: WebDriver) -> None:
        self.__driver = driver

    @allure.step("Получить текущий URL")
    def get_current_url(self) -> str:
        return self.__driver.current_url

    @allure.step("Перейти к поиску по году выпуска")
    def get_years(self):
        (WebDriverWait(self.__driver, 30).until(
            EC.visibility_of_element_located((By.XPATH, "//h1[text()='Списки']"
                                              ))))
        (self.__driver.find_element(By.XPATH, "//a[text()='Годы']")).click()
        element = self.__driver.find_element(
            By.XPATH, "//span[text()='2000-e']")
        self.__driver.execute_script(
            "arguments.scrollIntoView(true);", element)
        (WebDriverWait(self.__driver, 15).until(
            EC.visibility_of_element_located((
                By.XPATH, "//span[text()='2000-e']")))).click()

    @allure.step("Перейти к фильтру по названию")
    def select_filter(self) -> str:
        self.__driver.find_element(By.CSS_SELECTOR, "#arrowIcon").click()
        items = (WebDriverWait(self.__driver, 30).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "#itemWrapper"
                                              ))))
        item = items.find_elements(By.TAG_NAME, 'label')
        item[4].click()
        film = WebDriverWait(self.__driver, 30).until(
            EC.visibility_of_element_located((
                By.XPATH, "//span[text()='Аватар']"))).text
        return film
