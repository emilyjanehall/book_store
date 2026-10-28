from playwright.sync_api import Page, expect
from lib.database_connection import *

def test_has_welcome_title(page: Page):
    page.goto("http://127.0.0.1:5001")

    h1 = page.locator("h1")

    expect(h1).to_have_text("Welcome to AceReads")

def test_has_books_title(page: Page):
    page.goto("http://127.0.0.1:5001/books")

    h1 = page.locator("h1")

    expect(h1).to_have_text("Books")

def test_new_book_added_to_list(page: Page):
    connection = DatabaseConnection()
    connection.connect()
    connection.seed("./seeds/books.sql")

    page.goto("http://127.0.0.1:5001/books")

    page.get_by_label("Title").fill("title")
    page.get_by_label("Author").fill("author")
    page.get_by_role("button", name="Submit").click()

    books_list = page.locator("ul > li")

    assert books_list.all_inner_texts()[4] == "title by author"

def test_has_books_list(page: Page):
    connection = DatabaseConnection()
    connection.connect()
    connection.seed("./seeds/books.sql")

    page.goto("http://127.0.0.1:5001/books")

    books_list = page.locator("ul > li")

    expect(books_list).to_have_text([
        "The Gruffalo by Julia Donaldson",
        "Ada Twist, Scientist by Andrea Beaty",
        "The Girl Who Drank the Moon by Kelly Barnhill",
        "Dragons in a Bag by Zetta Elliott"
        ])

def test_book_list_contains_all_books(page: Page):
    connection = DatabaseConnection()
    connection.connect()
    connection.seed("./seeds/books.sql")
