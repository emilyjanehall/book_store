from flask import Flask, render_template, request, redirect
from lib.database_connection import DatabaseConnection
from lib.book_repository import BookRepository
from lib.book import Book
from lib.film import Film
from lib.film_repository import FilmRepository
from lib.user import User
from lib.user_repository import UserRepository

# instantiate a Flask app object
app = Flask(__name__)

# Declares a route that listens for a GET request to the path /hello
# and a method to execute when that request comes in
@app.route('/hello', methods=['GET'])
def hello():
    return "Hello to you too"

# NEW PART START

# duplicate route
@app.route('/hello', methods=['GET'])
def hello_again():
    return "Hello, hello and hello again!"

# NEW PART END

@app.route('/books', methods=['GET'])
def get_all_books():
    connection = DatabaseConnection()
    connection.connect()
    book_repository = BookRepository(connection)
    books = book_repository.all()
    return render_template("books.html", books=books)

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route('/books', methods=['POST'])
def create_book():
    connection = DatabaseConnection()
    connection.connect()
    book_repository = BookRepository(connection)
    book_details = request.form
    book = Book(title=book_details["title"], author=book_details["author"])
    book_repository.create(book)
    return redirect("/books")

@app.route('/users/new', methods=['GET'])
def get_signup_form():
    return render_template("signup_form.html")

@app.route('/users', methods=['POST'])
def create_user():
    connection = DatabaseConnection()
    connection.connect()
    user_repository = UserRepository(connection)
    
    user_details = request.form
    user = User(username = user_details["username"], password = user_details["password"])
    user_repository.create(user)
    return redirect("/books")

@app.route('/films', methods=['POST'])
def create_film():
    connection = DatabaseConnection()
    connection.connect()
    film_repository = FilmRepository(connection)

    film_details = request.form
    film = Film(id=None, title=film_details["title"], release_year=film_details["release_year"])
    film_repository.create(film)
    return redirect("/films")

@app.route('/films', methods=['GET'])
def get_all_films():
    connection = DatabaseConnection()
    connection.connect()
    film_repository = FilmRepository(connection)

    films = film_repository.all()
    return render_template("films.html", films=films)

# make the server run in response to `python app.py`
# on port 5001 (you'll learn more about what this means later)
# and use debug mode so that changing code restarts the app
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)
