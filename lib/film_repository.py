from lib.film import Film

class FilmRepository:
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute('SELECT * from films')
        films = []
        for row in rows:
            film = Film(id=row["id"], title=row["title"], release_year=row["release_year"])
            films.append(film)
        return films

    def create(self, film):
        self._connection.execute('INSERT INTO films (title, release_year) VALUES (%s, %s)', [film.title, film.release_year])