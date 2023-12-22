# type: ignore
# flake8: noqa
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#| label: basic-class
class Bookstore:
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.books = []

    def __getitem__(self, index):
        return self.books[index]

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return f"Bookstore[{self.get_num_books()} books]"

    def add_books(self, book_list):
        self.books.extend(book_list)

    def get_books(self):
        return self.books

    def get_inventory(self):
        book_lines = []
        for book_index, book in enumerate(self.get_books()):
            cur_book_line = f"{book_index}. {str(book)}"
            book_lines.append(cur_book_line)
        return "\n".join(book_lines)

    def get_num_books(self):
        return len(self.get_books())

    def sort_books(self, sort_key):
        self.books.sort(key=sort_key)

class Book:
    def __init__(self, title, authors, num_pages):
        self.title = title
        self.authors = authors
        self.num_pages = num_pages

    def __str__(self):
        return f"Book[title={self.get_title()}, authors={self.get_authors()}, pages={self.get_num_pages()}]"

    def get_authors(self):
        return self.authors

    def get_first_author(self):
        return self.authors[0]

    def get_num_pages(self):
        return self.num_pages

    def get_title(self):
        return self.title

class Person:
    def __init__(self, family_name, given_name):
        self.family_name = family_name
        self.given_name = given_name

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return f"Person[{self.get_family_name()}, {self.get_given_name()}]"

    def get_family_name(self):
        return self.family_name

    def get_given_name(self):
        return self.given_name
#
#
#
#
#
#
#| label: create-objs
my_bookstore = Bookstore("Bookland", "Washington, DC")
plath = Person("Plath", "Sylvia")
bell_jar = Book("The Bell Jar", [plath], 244)
marx = Person("Marx", "Karl")
engels = Person("Engels", "Friedrich")
manifesto = Book("The Communist Manifesto", [marx, engels], 43)
elster = Person("Elster", "Jon")
cement = Book("The Cement of Society", [elster], 311)
my_bookstore.add_books([bell_jar, manifesto, cement])
print(my_bookstore)
print(my_bookstore[0])
print("Inventory:")
print(my_bookstore.get_inventory())
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#| label: sort-alpha
sort_alpha = lambda x: x.get_first_author().get_family_name()
my_bookstore.sort_books(sort_key = sort_alpha)
print(my_bookstore.get_inventory())
#
#
#
#
#
#
#
#
#
#
#| label: sort-pages
sort_pages = lambda x: x.get_num_pages()
my_bookstore.sort_books(sort_key = sort_pages)
print(my_bookstore.get_inventory())
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#| label: fiction-property
from enum import Enum
class BookType(Enum):
    NONFICTION = 0
    FICTION = 1

class Book:
    def __init__(self, title: str, authors: list[Person], num_pages: int, type: BookType):
        self.title = title
        self.authors = authors
        self.num_pages = num_pages
        self.type = type

    def __str__(self):
        return f"Book[title={self.title}, authors={self.authors}, pages={self.num_pages}, type={self.type}]"
#
#
#
#| label: use-fiction-property
joyce = Person("Joyce", "James")
ulysses = Book("Ulysses", [joyce], 732, BookType.FICTION)
schelling = Person("Schelling", "Thomas")
micromotives = Book("Micromotives and Macrobehavior", [schelling], 252, BookType.NONFICTION)
print(ulysses)
print(micromotives)
#
#
#
#
#
#
#
#
#
#
#| label: fiction-separate-classes-setup
class Book:
    def __init__(self, title, authors, num_pages):
        self.title = title
        self.authors = authors
        self.num_pages = num_pages

    def __str__(self):
        return f"Book[title={self.get_title()}, authors={self.get_authors()}, pages={self.get_num_pages()}]"

    def get_authors(self):
        return self.authors

    def get_first_author(self):
        return self.authors[0]

    def get_num_pages(self):
        return self.num_pages

    def get_title(self):
        return self.title
#
#
#
#| label: fiction-separate-classes
# class Book defined as earlier
class FictionBook(Book):
    def __init__(self, title, authors, num_pages, characters):
        super().__init__(title, authors, num_pages)
        self.characters = characters

class NonfictionBook(Book):
    def __init__(self, title, authors, num_pages, topic):
        self.__super__(title, authors, num_pages)
        self.topic = topic
#
#
#
#| label: use-fiction-separate-classes
joyce = Person("Joyce", "James")
ulysses = FictionBook("Ulysses", [joyce], 732, ["Daedalus"])
schelling = Person("Schelling", "Thomas")
micromotives = NonfictionBook("Micromotives and Macrobehavior", [schelling], 252, "Economics")
print(ulysses)
print(micromotives)
#
#
#
#
#
#
