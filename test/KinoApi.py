import requests
import allure


class KinoApi:

    def __init__(self, base_url: str) -> None:
        self.base_url = base_url

    @allure.step("Найти все фильмы на странице")
    def get_movie(self):
        my_headers = {
            'X-API-KEY': "P3KJA14-2AHM4E1-H29RM91-772YQ1R",
            'Content-Type': 'application/json'
        }
        resp = requests.get(self.base_url + '/v1.4/movie', headers=my_headers)
        return resp, resp.json()

    @allure.step("Найти фильм по id")
    def get_movie_by_id(self, id: str):
        my_headers = {
            'X-API-KEY': "P3KJA14-2AHM4E1-H29RM91-772YQ1R",
            'Content-Type': 'application/json'
        }
        resp = requests.get(self.base_url + '/v1.4/movie/' + str(id), headers=my_headers)
        return resp, resp.json()
 
    @allure.step("Найти фильм по названию")
    def get_movie_by_name(self, name: str) -> list:
        my_headers = {
            'X-API-KEY': "P3KJA14-2AHM4E1-H29RM91-772YQ1R",
            'Content-Type': 'application/json'
        }
        resp = requests.get(self.base_url + '/v1.4/movie/search?query='
                            + str(name), headers=my_headers)
        return resp, resp.json()
    
    @allure.step("Найти актера по имени и фамилии")
    def get_people_by_name(self, name: str) -> list:
        my_headers = {
            'X-API-KEY': "P3KJA14-2AHM4E1-H29RM91-772YQ1R",
            'Content-Type': 'application/json'
        }
        resp = requests.get(self.base_url + '/v1.4/person/search?query=' + str(name),
                            headers=my_headers)
        return resp, resp.json()

    @allure.step("Найти актера по id")
    def get_people_by_id(self, id: str) -> list:
        my_headers = {
            'X-API-KEY': "P3KJA14-2AHM4E1-H29RM91-772YQ1R",
            'Content-Type': 'application/json'
        }
        resp = requests.get(self.base_url + '/v1.4/person/'
                            + str(id), headers=my_headers)
        return resp, resp.json()
    
    @allure.step("Найти фильм по году выпуска и жанру")
    def get_film_year_and_genre(self, year: str, genre: str) -> list:
        my_headers = {
            'X-API-KEY': "P3KJA14-2AHM4E1-H29RM91-772YQ1R",
            'Content-Type': 'application/json'
        }
        resp = requests.get(self.base_url + '/v1.4/movie?year=' + year + '&genres.name='
                            + genre, headers=my_headers)
        return resp, resp.json()
    
