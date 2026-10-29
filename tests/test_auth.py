from app import app
from lib.database_connection import DatabaseConnection
from playwright.sync_api import Page

def test_auth_integration():
    client = app.test_client()
    connection = DatabaseConnection()
    connection.connect()
    connection.execute("TRUNCATE TABLE users;")
    connection.execute("INSERT INTO users (username, password) values ('user', 'pword');")

    response = client.post('/sessions', data={
        'username': 'user',
        'password': 'pword'
    })

    assert response.status_code == 302
    assert response.headers['Location'].endswith('/books')

def test_auth_playwright(page: Page):

    connection = DatabaseConnection()
    connection.connect()
    connection.execute("TRUNCATE TABLE users;")
    connection.execute("INSERT INTO users (username, password) values ('user', 'pword');")

    page.goto("http://localhost:5001/sessions/new")
    page.get_by_label("username").fill("user")
    page.get_by_label("password").fill("pword")
    page.get_by_role("button").click()

    assert page.url == "http://localhost:5001/books"
