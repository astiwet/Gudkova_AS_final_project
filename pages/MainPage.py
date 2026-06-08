import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver
from dotenv import load_dotenv
import os
load_dotenv()


class MainPage:

    def __init__(self, driver: WebDriver) -> None:
        self.__url = os.getenv("BASE_URL")
        self.__driver = driver
        self.wait = WebDriverWait(self.__driver, 10)

    @allure.step("Получить текущий URL")
    def go(self):
        self.__driver.get(self.__url)

    @allure.step("Найти фильм по названию")
    def found_film(self, name: str) -> None:
        self.wait.until(EC.visibility_of_element_located((By.TAG_NAME, "input")
                                                         ))
        self.__driver.find_element(By.TAG_NAME, "input").send_keys(name)
        element = self.wait.until(EC.visibility_of_element_located((
            By.XPATH, "//div[contains(@class, 'kinopoisk-header-suggest-group'"
            ")][1]//article")))
        element.click()

    @allure.step("Найти актера по фамилии и имени")
    def found_person(self, name: str) -> None:
        self.wait.until(EC.visibility_of_element_located((By.TAG_NAME, "input")
                                                         ))
        self.__driver.find_element(By.TAG_NAME, "input").send_keys(name)
        person = self.wait.until(EC.visibility_of_element_located((
                By.XPATH, "//a[@id='suggest-item-person-231266']")))
        person.click()

    @allure.step("Перейти в поиск фильмов в меню")
    def get_films(self) -> None:
        search = self.wait.until(EC.visibility_of_element_located((
                By.XPATH, "//a[@href='/lists/categories/movies/1/']")))
        search.click()

    @allure.step("Перейти в расширенный поиск")
    def advanced_search(self) -> None:
        search = self.wait.until(
            EC.visibility_of_element_located((
                By.XPATH, "//a[@aria-label='Расширенный поиск']")))
        search.click()
