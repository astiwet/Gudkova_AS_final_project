import pytest
import allure
from pages.MainPage import MainPage
from pages.CartPage import CartPage
from pages.FilmsPage import FilmsPage
from pages.SearchPage import SearchPage
from pages.PersonPage import PersonPage


@pytest.mark.ui
@allure.story("Поиск и просмотр информации о фильме")
@allure.title("Тест: поиск фильма 'Аватар' и проверка данных на странице: "
              "отзывы и актеры")
def test_film(browser):
    with allure.step("Инициализировать главную страницу и перейти на сайт"):
        main_page = MainPage(browser)
        main_page.go()

    with allure.step("Найти фильм 'Аватар' на главной странице"):
        main_page.found_film("Аватар")

    with allure.step("Инициализировать страницу фильма"):
        cart_page = CartPage(browser)

    with allure.step("Получить название фильма со страницы"):
        result = cart_page.result_name()

    with allure.step("Получить количество рецензий"):
        total = cart_page.get_feedback()

    with allure.step("Получить имя актёра из списка"):
        person = cart_page.get_actor()

    with allure.step("Проверить, что название фильма соответствует ожидаемому"
                     ):
        assert result == 'Аватар (2009)'

    with allure.step("Проверить, что количество рецензий "
                     "соответствует ожидаемому"):
        assert total == '2452 рецензии'

    with allure.step("Проверить, что имя актёра соответствует ожидаемому"):
        assert person == 'Зои Салдана'


@pytest.mark.ui
@allure.story("Поиск и просмотр информации об актёре")
@allure.title("Тест: поиск актёра 'Мария Миронова' и проверка фильмографии")
def test_person(browser):
    with allure.step("Инициализировать главную страницу и перейти на сайт"):
        main_page = MainPage(browser)
        main_page.go()

    with allure.step("Найти актёра 'Мария Миронова' на главной странице"):
        main_page.found_person("Мария Миронова")

    with allure.step("Инициализировать страницу актёра"):
        person_page = PersonPage(browser)

    with allure.step("Получить имя актёра с страницы"):
        actor = person_page.result_people_name()

    with allure.step("Получить название фильма из фильмографии актёра"):
        film = person_page.get_film()

    with allure.step("Проверить, что имя актёра соответствует ожидаемому"):
        assert actor == 'Мария Миронова'
    with allure.step("Проверить, что фильм в фильмографии "
                     "соответствует ожидаемому"):
        assert film == 'Роднина'


@pytest.mark.ui
@allure.story("Просмотр фильмов с применением фильтров")
@allure.title("Тест: фильтрация фильмов по годам и выбор фильма")
def test_find_films(browser):
    with allure.step("Инициализировать главную страницу и перейти на сайт"):
        main_page = MainPage(browser)
        main_page.go()

    with allure.step("Перейти к просмотру фильмов"):
        main_page.get_films()

    with allure.step("Инициализировать страницу фильмов"):
        films_page = FilmsPage(browser)

    with allure.step("Установить фильтры по годам"):
        films_page.get_years()

    with allure.step("Выбрать фильм через фильтр"):
        film = films_page.select_filter()

    with allure.step("Проверить, что найденный по критериям фильм"
                     "соответствует ожидаемому"):
        assert film == 'Аватар'


@pytest.mark.ui
@allure.story("Расширенный поиск фильма по названию")
@allure.title("Тест: поиск фильма 'В джазе только девушки' через расширенный "
              "поиск")
def test_search_film(browser):
    with allure.step("Инициализировать главную страницу и перейти на сайт"):
        main_page = MainPage(browser)
        main_page.go()

    with allure.step("Перейти к расширенному поиску фильмов"):
        main_page.advanced_search()

    with allure.step("Инициализировать страницу поиска"):
        search_page = SearchPage(browser)

    with allure.step("Выполнить поиск фильма 'В джазе только девушки'"):
        search_page.search_film("В джазе только девушки")

    with allure.step("Получить результат поиска — название фильма"):
        film = search_page.result_film()

    with allure.step("Проверить, что найденный фильм соответствует ожидаемому"
                     ):
        assert film == 'В джазе только девушки'


@pytest.mark.ui
@allure.story("Расширенный поиск фильмов по параметрам")
@allure.title("Тест: поиск фильмов с фильтрами по стране, году и жанру")
def test_search_movie(browser):
    with allure.step("Инициализировать главную страницу и перейти на сайт"):
        main_page = MainPage(browser)
        main_page.go()

    with allure.step("Перейти к расширенному поиску фильмов"):
        main_page.advanced_search()

    with allure.step("Инициализировать страницу поиска"):
        search_page = SearchPage(browser)

    with allure.step("Установить фильтр: страна — 'Россия'"):
        search_page.search_country("Россия")

    with allure.step("Установить фильтр: год — '2017'"):
        search_page.search_year("2017")

    with allure.step("Установить фильтр по жанру"):
        search_page.search_genre()

    with allure.step("Получить результаты поиска"):
        year = search_page.result_search()

    with allure.step("Проверить, что страна в результатах поиска "
                     "соответствует ожидаемой"):
        assert year == 'Россия'


@pytest.mark.ui
@allure.story("Расширенный поиск персоны и просмотр фильмографии")
@allure.title("Тест: поиск персоны 'Зои Салдана' и проверка фильмографии")
def test_search_person(browser):
    with allure.step("Инициализировать главную страницу и перейти на сайт"):
        main_page = MainPage(browser)
        main_page.go()

    with allure.step("Перейти к расширенному поиску"):
        main_page.advanced_search()

    with allure.step("Инициализировать страницу поиска"):
        search_page = SearchPage(browser)

    with allure.step("Выполнить поиск персоны 'Зои Салдана'"):
        search_page.search_people("Зои Салдана")

    with allure.step("Инициализировать страницу персоны"):
        person_page = PersonPage(browser)

    with allure.step("Получить имя персоны с страницы"):
        actor = person_page.result_people_name()

    with allure.step("Получить название фильма из фильмографии персоны"):
        film = person_page.get_film()

    with allure.step("Проверить, что найденная персона соответствует ожидаемой"
                     ):
        assert actor == 'Зои Салдана'
    with allure.step("Проверить, что фильм в фильмографии соответствует "
                     "ожидаемому"):
        assert film == 'Аватар'
