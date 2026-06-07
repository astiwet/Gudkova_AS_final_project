from KinoApi import KinoApi
api = KinoApi("https://api.poiskkino.dev")


def test_find_film_id():
    resp, list_data = api.get_movie()
    assert len(list_data) > 1
    assert resp.status_code == 200
    doc = list_data['docs']
    films = doc[0]
    film_id = films['id']
    film_name = films['alternativeName']
    resp = api.get_movie_by_id(film_id)
    movie = resp[1]
    movie_name = movie['alternativeName']
    assert movie_name == film_name


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
    assert resp.status_code == 200
    doc = info["docs"][0]
    people_id = doc['id']
    resp, person = api.get_people_by_id(people_id)
    assert resp.status_code == 200
    person_name = person['name']
    person_id = person['id']

    assert resp.status_code == 200
    assert person_id == people_id
    assert person_name == name


def test_find_film():
    year = '2020'
    genre = "фантастика"
    resp, film = api.get_film_year_and_genre(year, genre)
    doc = film["docs"][0]
    film_genres = doc["genres"][1]
    film_genre = film_genres['name']
    film_year = doc['year']

    assert resp.status_code == 200
    assert film_genre == genre
    assert str(film_year) == year

