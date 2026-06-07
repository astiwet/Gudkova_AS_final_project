import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver


class FilmsPage:

    def __init__(self, driver: WebDriver) -> None:
        self.__driver = driver
        self.wait = WebDriverWait(self.__driver, 10)

    @allure.step("Перейти к поиску по году выпуска")
    def get_years(self):
        self.wait.until(EC.visibility_of_element_located((
             By.XPATH, "//h1[text()='Списки']")))
        years_link = self.wait.until(EC.element_to_be_clickable((
            By.XPATH, "//a[contains(text(), 'Годы')]")))
        years_link.click()
        element = self.wait.until(EC.element_to_be_clickable((
            By.XPATH, "//span[text()='2000-е']")))
        self.__driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});", element)
        self.wait.until(lambda _: True)
        element.click()

    @allure.step("Перейти к фильтру 'по названию'")
    def select_filter(self) -> str:
        self.__driver.find_element(
            By.XPATH, "//span[@class='styles_arrowIcon__1CH4G']").click()
        items = self.wait.until(EC.visibility_of_element_located((
            By.XPATH, "//div[@class='styles_itemWrapper__C3kJd']")))
        item = items.find_elements(By.TAG_NAME, 'label')
        item[4].click()
        film = self.wait.until(EC.visibility_of_element_located((
                By.XPATH, "//span[contains(text(), 'Аватар')]")))
        movie = film.text
        return movie
