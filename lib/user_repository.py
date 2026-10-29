from lib.user import User

class UserRepository:

    def __init__(self, connection):
        self._connection = connection

    def create(self, user):
        self._connection.execute(
            'INSERT INTO users (username, password) VALUES (%s, %s)',
            [user.username, user.password]
        )
        return None

    def find_by_username(self, username):
        rows = self._connection.execute(
            'SELECT * FROM users WHERE username = %s', [username]
        )

        if not rows:
            return None

        user_details = rows[0]

        return User(
            user_details["username"],
            user_details["password"],
            user_details["id"]
        )
    