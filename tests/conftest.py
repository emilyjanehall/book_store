import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pytest
from lib.database_connection import DatabaseConnection

@pytest.fixture(autouse=True)
def reset_database():
    connection = DatabaseConnection()
    connection.connect()
    
    connection.execute("DELETE FROM books")
    
    connection.execute("INSERT INTO books (title, author) VALUES ('The Gruffalo', 'Julia Donaldson')")
    connection.execute("INSERT INTO books (title, author) VALUES ('Ada Twist, Scientist', 'Andrea Beaty')")
    connection.execute("INSERT INTO books (title, author) VALUES ('The Girl Who Drank the Moon', 'Kelly Barnhill')")
    connection.execute("INSERT INTO books (title, author) VALUES ('Dragons in a Bag', 'Zetta Elliott')")

@pytest.fixture
def connection():
    connection = DatabaseConnection()
    connection.connect()
    return connection
