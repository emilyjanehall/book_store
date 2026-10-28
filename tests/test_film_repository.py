from lib.film_repository import FilmRepository
from lib.film import Film
from lib.database_connection import DatabaseConnection

def test_get_all_films(connection):
    connection.seed("seeds/films.sql")
    repository = FilmRepository(connection)

    films = repository.all()

    assert films == [
        Film(1, "Tangled", 2011)
    ]

def test_create_film(connection):
    connection.seed("seeds/films.sql")
    repository = FilmRepository(connection)

    repository.create(Film(None, "Brand New Day", 2026))

    films = repository.all()
    assert films == [
        Film(1, "Tangled", 2011),
        Film(2, "Brand New Day", 2026)
    ]
    