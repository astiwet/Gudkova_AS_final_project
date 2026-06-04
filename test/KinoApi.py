import requests
import allure


class KinoApi:

    def __init__(self, base_url: str, token: str) -> None:
        self.base_url = base_url
        self.token = token

    @allure.step("Найти все фильмы на странице")
    def get_movie(self) -> list:
        my_headers = {}
        my_headers['Authorization'] = self.token
        my_headers['Content-type'] = 'application/json'
        resp = requests.get(self.base_url + '/movie', headers=my_headers)
        return resp, resp.json()

    @allure.step("Найти фильм по id")
    def get_movie_by_id(self, id: str) -> list:
        resp = requests.get(self.base_url + '/movie/' + str(id) + self.token)
        return resp, resp.json()
 
    @allure.step("Найти фильм по названию")
    def get_movie_by_name(self, name: str) -> list:
        resp = requests.get(self.base_url + '/movie/search?query=' + str(name) +
                            self.token)
        return resp, resp.json()
    
    @allure.step("Найти актера по имени и фамилии")
    def get_people_by_name(self, name: str) -> list:
        resp = requests.get(self.base_url + '/person/search?query=' + str(name) +
                            self.token)
        return resp, resp.json()

    @allure.step("Найти актера по id")
    def get_people_by_id(self, id: str) -> list:
        resp = requests.get(self.base_url + '/person/search?query=' + str(id) +
                            self.token)
        return resp, resp.json()
    
    @allure.step("Найти фильм по году выпуска и жанру")
    def get_film_year_and_genre(self, year: str, genre: str) -> list:
        resp = requests.get(self.base_url + '/movie?year=' + year + '&genres.name='
                            + genre + self.token)
        return resp, resp.json()
