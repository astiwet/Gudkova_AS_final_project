from MainPage import MainPage
from CartPage import CartPage
from FilmsPage import FilmsPage
from SearchPage import SearchPage
from PersonPage import PersonPage


def test_film(browser):
    main_page = MainPage(browser)
    main_page.go()
    main_page.found_film("Аватар")
    cart_page = CartPage(browser)
    result = cart_page.result_name()
    total = cart_page.get_feedback()
    person = cart_page.get_actor()
    assert result == 'Аватар (2009)'
    assert total == '2452 рецензии'
    assert person == 'Зои Салдана'


def test_person(browser):
    main_page = MainPage(browser)
    main_page.go()
    main_page.found_person("Мария Миронова")
    person_page = PersonPage(browser)
    actor = person_page.result_people_name()
    film = person_page.get_film()
    assert actor == 'Мария Миронова'
    assert film == 'Роднина'


def test_find_films(browser):
    main_page = MainPage(browser)
    main_page.go()
    main_page.get_films()
    films_page = FilmsPage(browser)
    films_page.get_years()
    film = films_page.select_filter()
    assert film == 'Аватар'


def test_search_film(browser):
    main_page = MainPage(browser)
    main_page.go()
    main_page.advanced_search()
    search_page = SearchPage(browser)
    search_page.search_film("В джазе только девушки")
    film = search_page.result_film()
    assert film == 'В джазе только девушки'


def test_search_movie(browser):
    main_page = MainPage(browser)
    main_page.go()
    main_page.advanced_search()
    search_page = SearchPage(browser)
    search_page.search_country("Россия")
    search_page.search_year("2017")
    search_page.search_genre()
    year = search_page.result_search()
    assert year == 'Россия'


def test_search_person(browser):
    main_page = MainPage(browser)
    main_page.go()
    main_page.advanced_search()
    search_page = SearchPage(browser)
    search_page.search_people("Зои Салдана")
    person_page = PersonPage(browser)
    actor = person_page.result_people_name()
    film = person_page.get_film()
    assert actor == 'Зои Салдана'
    assert film == 'Аватар'
