import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver


class MainPage:

    def __init__(self, driver: WebDriver) -> None:
        self.__url = "https://www.kinopoisk.ru/"
        self.__driver = driver

    @allure.step("Получить текущий URL")
    def go(self):
        self.__driver.get(self.__url)

    @allure.step("Найти фильм по названию")
    def found_film(self, name: str):
        (WebDriverWait(self.__driver, 10).
         until(EC.visibility_of_element_located((By.
                                                 TAG_NAME, "input"))))

        (self.__driver.find_element(By.TAG_NAME, "input").
         send_keys(name))
        (WebDriverWait(self.__driver, 10).until(
            EC.visibility_of_element_located((
                By.ID, "suggest_item_film_251733")))).click()

    @allure.step("Получить текущий URL")
    def get_current_url(self) -> str:
        return self.__driver.current_url

    @allure.step("Найти актера по фамилии и имени")
    def found_person(self, name: str):
        (WebDriverWait(self.__driver, 10).
         until(EC.visibility_of_element_located((By.
                                                 TAG_NAME, "input"))))
        (self.__driver.find_element(By.TAG_NAME, "input").
         send_keys(name))
        (WebDriverWait(self.__driver, 10).until(
            EC.visibility_of_element_located((
                By.ID, "suggest_item_person_231266"))))
        (self.__driver.find_element(By.ID, "suggest_item_person_231266")
         ).click()

    @allure.step("Перейти в поиск фильмов в меню")
    def get_films(self):
        WebDriverWait(self.__driver, 10).until(
            EC.visibility_of_element_located((
                By.CLASS_NAME, "styles_title__Jmj_H"))).click()

    @allure.step("Перейти в расширенный поиск")
    def advanced_search(self):
        (WebDriverWait(self.__driver, 10).until(
            EC.visibility_of_element_located((
                By.CLASS_NAME, "styles_advancedSearch__gh_09")))).click()
