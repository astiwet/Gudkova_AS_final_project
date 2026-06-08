import requests
import allure
from typing import Dict, Any, Tuple, List
from dotenv import load_dotenv
import os
load_dotenv()


class KinoApi:

    def __init__(self, base_API_url: str) -> None:
        self.base_url = base_API_url

    my_headers: Dict[str, str] = {
            'X-API-KEY': os.getenv("API_KEY"),
            'Content-Type': 'application/json'
        }

    @allure.step("Найти все фильмы на странице")
    def get_movie(self) -> Tuple[requests.Response, Dict[str, Any]]:
        resp = requests.get(self.base_url + '/movie',
                            headers=self.my_headers)
        return resp, resp.json()

    @allure.step("Найти фильм по id")
    def get_movie_by_id(self, id: str) -> Tuple[requests.Response,
                                                Dict[str, Any]]:
        resp = requests.get(self.base_url + '/movie/' + str(id),
                            headers=self.my_headers)
        return resp, resp.json()

    @allure.step("Найти фильм по названию")
    def get_movie_by_name(self, name: str) -> Tuple[requests.Response,
                                                    List[Dict[str, Any]]]:
        resp = requests.get(self.base_url + '/movie/search?query='
                            + str(name), headers=self.my_headers)
        return resp, resp.json()

    @allure.step("Найти актера по имени и фамилии")
    def get_people_by_name(self, name: str) -> Tuple[requests.Response,
                                                     List[Dict[str, Any]]]:
        resp = requests.get(self.base_url + '/person/search?query='
                            + str(name), headers=self.my_headers)
        return resp, resp.json()

    @allure.step("Найти актера по id")
    def get_people_by_id(self, id: str) -> Tuple[requests.Response,
                                                 Dict[str, Any]]:
        resp = requests.get(self.base_url + '/person/'
                            + str(id), headers=self.my_headers)
        return resp, resp.json()

    @allure.step("Найти фильм по году выпуска и жанру")
    def get_film_year_and_genre(self, year: str, genre: str) -> Tuple:
        resp = requests.get(self.base_url + '/movie?year=' + year
                            + '&genres.name=' + genre, headers=self.my_headers)
        return resp, resp.json()
