import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver


class SearchPage:

    def __init__(self, driver: WebDriver) -> None:
        self.__driver = driver

    @allure.step("Найти фильм по названию")
    def search_film(self, name: str):
        (WebDriverWait(self.__driver, 10).
         until(EC.visibility_of_element_located((By.
                                                 ID, "find_film"))))
        (self.__driver.find_element(By.ID, "find_film").
         send_keys(name))
        
    @allure.step("Результат поиска фильма")
    def result_film(self) -> str:
        res = WebDriverWait(self.__driver, 10).until(
            EC.visibility_of_element_located((
                By.XPATH, "//a[text()='В джазе только девушки']")))
        result = res.text
        return result
        

    @allure.step("Найти фильм по стране производства")
    def search_country(self, name: str):
        (WebDriverWait(self.__driver, 10).
         until(EC.visibility_of_element_located((By.
                                                 ID, "country"))))
        (self.__driver.find_element(By.ID, "country").
         send_keys(name))

    @allure.step("Найти фильм по году производства")
    def search_year(self, number: int):
        (WebDriverWait(self.__driver, 10).
         until(EC.visibility_of_element_located((By.
                                                 ID, "year"))))
        (self.__driver.find_element(By.ID, "year").
         send_keys(number))

    @allure.step("Найти фильм по жанру")
    def search_genre(self):
        genre = (WebDriverWait(self.__driver, 10).until(
            EC.visibility_of_element_located((By.TAG_NAME, "nav"))))
        fields = genre.find_elements(By.ID, "m_act[genre]")
        fields[4].click()

    @allure.step("Найти актера по имени и фамилии")
    def search_people(self, name: str):
        element = self.__driver.find_element(
            By.ID, "find_film")
        self.__driver.execute_script(
            "arguments.scrollIntoView(true);", element)
        (self.__driver.find_element(By.ID, "find_people").
         send_keys(name))
    
    @allure.step("Задать поиск фильма")
    def search_button(self):
        (WebDriverWait(self.__driver, 10).until(
            EC.visibility_of_element_located((
                By.CSS_SELECTOR, "#nice_button")))).click()
