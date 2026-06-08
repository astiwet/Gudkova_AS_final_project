import pytest
import allure
from pages.KinoApi import KinoApi
from dotenv import load_dotenv
import os
load_dotenv()

api = KinoApi(os.getenv("BASE_API_URL"))


@pytest.mark.api
@allure.story("Поиск фильма по ID через API")
@allure.title("Тест: поиск фильма по ID и проверка соответствия данных")
def test_find_film_id():
    with allure.step("Получить список фильмов через API"):
        resp, list_data = api.get_movie()

    with allure.step("Проверить статус ответа API для списка фильмов"):
        assert resp.status_code == 200

    with allure.step("Проверить, что полученный список содержит"
                     "более одного фильма"):
        assert len(list_data) > 1

    with allure.step("Извлечь данные первого фильма из списка"):
        doc = list_data['docs']
    films = doc[0]
    film_id = films['id']
    film_name = films['alternativeName']

    with allure.step("Выполнить запрос к API для поиска"
                     "фильма по ID"):
        resp, movie = api.get_movie_by_id(film_id)

    with allure.step("Проверить статус ответа API для запроса по ID фильма"):
        assert resp.status_code == 200

    with allure.step("Извлечь данные найденного фильма"):
        movie_name = movie['alternativeName']

    with allure.step("Проверить соответствие названий: "
                     "из списка и по ID"):
        assert movie_name == film_name


@pytest.mark.api
@allure.story("Поиск фильма по названию через API")
@allure.title("Тест: поиск фильма по названию и проверка результата")
def test_find_film_name():
    name = "Аватар"
    with allure.step("Выполнить запрос к API для поиска фильма по названию"):
        resp, info = api.get_movie_by_name(name)

    with allure.step("Проверить статус ответа API"):
        assert resp.status_code == 200

    with allure.step("Извлечь данные первого найденного фильма"):
        doc = info["docs"][0]
    film_name = doc["name"]

    with allure.step("Проверить, что полученное название фильма"
                     "cовпадает с искомым"):
        assert film_name == name


@pytest.mark.api
@allure.story("Поиск персоны по имени через API")
@allure.title("Тест: поиск персоны по имени и проверка результата")
def test_find_people_name():
    name = "Мария Миронова"
    with allure.step("Выполнить запрос к API для поиска человека по имени"):
        resp, info = api.get_people_by_name(name)

    with allure.step("Проверить статус ответа API"):
        assert resp.status_code == 200

    with allure.step("Извлечь данные первого найденного человека"):
        doc = info["docs"][0]
        people_name = doc["name"]

    with allure.step("Проверить, что полученное имя персоны"
                     "совпадает с искомым"):
        assert people_name == name


@pytest.mark.api
@allure.story("Поиск персоны по ID через API")
@allure.title("Тест: поиск персоны по ID и проверка данных персоны")
def test_find_people_id():
    name = "Иван Охлобыстин"
    with allure.step("Выполнить запрос к API для поиска человека по имени"):
        resp, info = api.get_people_by_name(name)

    with allure.step("Проверить статус ответа API для поиска по имени"):
        assert resp.status_code == 200

    with allure.step("Извлечь данные первого найденного человека"
                     "и получить его ID"):
        doc = info["docs"][0]
    people_id = doc['id']

    with allure.step("Выполнить запрос к API для поиска человека"
                     "по ID"):
        resp, person = api.get_people_by_id(people_id)

    with allure.step("Проверить статус ответа API для запроса по ID"):
        assert resp.status_code == 200

    with allure.step("Извлечь данные человека, найденного по ID"):
        person_name = person['name']
    person_id = person['id']

    with allure.step("Проверить, что ожидаемый ID совпадает с полученным"):
        assert person_id == people_id

    with allure.step("Проверить, что полученное имя совпадает с искомым"):
        assert person_name == name


@pytest.mark.api
@allure.story("Расширенный поиск фильмов по параметрам")
@allure.title("Тест: поиск фильмов по году и жанру через API")
def test_find_film():
    with allure.step("Задать параметры поиска: год — '2020',"
                     "жанр — 'фантастика'"):
        year = '2020'
    genre = "фантастика"

    with allure.step("Выполнить запрос к API для поиска фильма по году и жанру"
                     ):
        resp, film = api.get_film_year_and_genre(year, genre)

    with allure.step("Проверить статус ответа API"):
        assert resp.status_code == 200

    with allure.step("Извлечь данные первого найденного фильма"):
        doc = film["docs"][0]
    film_genres = doc["genres"][1]
    film_genre = film_genres['name']
    film_year = doc['year']

    with allure.step("Проверить, что жанр совпадает"):
        assert film_genre == genre

    with allure.step("Проверить, что год совпадает"):
        assert str(film_year) == year
