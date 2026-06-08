import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement


class SearchPage:

    def __init__(self, driver: WebDriver) -> None:
        self.__driver = driver
        self.wait = WebDriverWait(self.__driver, 10)

    @allure.step("Найти фильм по названию")
    def search_film(self, name: str) -> None:
        self.wait.until(EC.visibility_of_element_located((By.ID, "find_film")))
        self.__driver.find_element(By.ID, "find_film").send_keys(name)
        element = self.wait.until(EC.visibility_of_element_located((
                By.XPATH, "//input[@value='поиск']")))
        element.click()

    @allure.step("Результат поиска фильма")
    def result_film(self) -> str:
        res = self.wait.until(EC.visibility_of_element_located((
                By.XPATH, "//a[text()='В джазе только девушки']")))
        result = res.text
        return result

    @allure.step("Ввести страну производства для поиска фильма")
    def search_country(self, name: str) -> None:
        self.wait.until(EC.visibility_of_element_located((By.ID, "country")))
        (self.__driver.find_element(By.ID, "country").
         send_keys(name))

    @allure.step("Ввести год производства для поиска фильма")
    def search_year(self, number: int) -> None:
        (WebDriverWait(self.__driver, 10).
         until(EC.visibility_of_element_located((By.
                                                 ID, "year"))))
        (self.__driver.find_element(By.ID, "year").
         send_keys(number))

    @allure.step("Выбрать жанр для поиска фильма")
    def search_genre(self):
        self.wait.until(EC.visibility_of_element_located((
            By.XPATH, "//select[@id='m_act[genre]']")))
        genres: list[WebElement] = self.__driver.find_elements(
            By.TAG_NAME, 'option')
        genres[4].click()

    @allure.step("Получить результаты поиска по параметрам")
    def result_search(self) -> str:
        element = self.wait.until(EC.visibility_of_element_located((
                By.XPATH, "//input[@value='поиск']")))
        element.click()
        self.wait.until(EC.visibility_of_element_located((
                By.CLASS_NAME, "search_results")))
        res = self.__driver.find_element(By.CLASS_NAME, "search_results")
        result = res.find_element(
            By.XPATH, "//span[@class='gray' and contains(text(), 'Россия,')]")
        info = result.text.strip()
        films = info.split(',')[0]
        return films

    @allure.step("Найти актера по имени и фамилии")
    def search_people(self, name: str) -> None:
        element = self.wait.until(EC.element_to_be_clickable((
            By.XPATH, "//p[contains(text(), 'Искать актера')]")))
        self.__driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});", element)
        self.wait.until(lambda _: True)
        person = self.__driver.find_element(
            By.ID, "find_people")
        person.send_keys(name)
        button = self.wait.until(EC.element_to_be_clickable((
                By.XPATH, "//input[@wfd-id='id25' and @value='поиск' "
                "and contains(@class, 'nice_button')]")))
        button.click()
