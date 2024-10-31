class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f"'{self.title}' by {self.author}, {self.pages} pages"


class Bookshelf:
    total_books = 0

    def __init__(self):
        self.books = []
        self.history = []

    def add_book(self, title, author, pages):
        if pages >= 0:
            new_book = Book(title, author, pages)
        else:
            print(f"Page number of the book: '{title}' was negative! Auto-set pages to 0!")
            new_book = Book(title, author, 0)
        Bookshelf.total_books += 1
        self.books.append(new_book)
        self.history.append(f"Book added: '{new_book}'")

    def remove_book(self, title):
        for book in self.books:
            if book.title == title:
                self.books.remove(book)
                self.history.append(f"Book removed: '{book}'")
                Bookshelf.total_books -= 1
                return
        print(f"'{title}' was not found on the bookshelf!")

    def set_pages(self, title, pages):
        for book in self.books:
            if book.title == title:
                if pages > 0:
                    book.pages = pages
                    self.history.append(f"Pages of '{title}' was changed to {pages}")
                else:
                    book.pages = 0
                    print(f"Page number of the book: '{title}' was negative! Auto-set pages to 0!")

    def list_books(self):
        if not self.books:
            print("\nNo books on the shelf. Start reading st00p1d!")
        else:
            for book in self.books:
                print(book)

    def show_history(self):
        print(f"\nBook history:")
        for record in self.history:
            print(record)

    def show_totalbooks(self):
        print(f"\nNumber of books on the shelf: {self.total_books}")


def main():
    # ------------------------------------- #
    # Exemple of complex usage of the class:
    # ------------------------------------- #
    shelf = Bookshelf()
    shelf.add_book("The Prince", "Niccolo Machiavelli", 134)
    shelf.add_book("Metro 2033", "Dmitri Gluhovski", -1)
    shelf.set_pages("Metro 2033", 323)
    new = input("Title of the book to add: ")
    shelf.add_book(new, input("Author of the book: "), int(input("Pages of the book: ")))
    print("\nShelf before removing the new book: ")
    shelf.list_books()
    shelf.show_totalbooks()
    shelf.remove_book(new)
    shelf.show_history()
    print("\nShelf after removing the new book: ")
    shelf.list_books()
    shelf.show_totalbooks()


main()
