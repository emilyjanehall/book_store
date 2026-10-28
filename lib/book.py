class Book:
    def __init__(self, title, author, id = None):
        self.title = title
        self.author = author
        self.id = id

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __repr__(self):
        return f"Book({self.id}, {self.title}, {self.author})"
    