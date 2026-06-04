from KinoApi import KinoApi
api = KinoApi("https://api.poiskkino.dev/v.1.4",
              "P3KJA14-2AHM4E1-H29RM91-772YQ1R")


def test_find_film_id():
    resp, list = api.get_movie()
    doc = list['docs'][0]
    film_id = doc['id']
    film_name = list["alternativeName"]
    film, resp = api.get_movie_by_id(film_id)

    assert film["alternativeName"] == film_name
    assert len(list) > 1
    assert resp.status_code == 200


def test_find_film_name():
    name = "Аватар"
    resp, info = api.get_movie_by_name(name)
    doc = info["docs"][0]
    film_name = doc["name"]

    assert film_name == name
    assert resp.status_code == 200


def test_find_people_name():
    name = "Мария Миронова"
    resp, info = api.get_people_by_name(name)
    doc = info["docs"][0]
    people_name = doc["name"]

    assert people_name == name
    assert resp.status_code == 200


def test_find_people_id():
    name = "Иван Охлобыстин"
    resp, info = api.get_people_by_name(name)
    doc = info["docs"][0]
    people_id = doc['id']
    people_name, resp = api.get_people_by_id(people_id)
    person_name = people_name['name']
    person_id = people_name['id']

    assert resp.status_code == 200
    assert person_id == people_id
    assert person_name == name


def test_find_film():
    year = "2020"
    genre = "фантастика"
    resp, film = api.get_film_year_and_genre(year, genre)
    doc = film["docs"][0]
    film_genre = doc["genres"][1]
    film_year = doc["year"]

    assert resp.status_code == 200
    assert film_genre == genre
    assert film_year == year
