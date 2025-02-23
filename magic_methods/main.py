class Book:
    def __init__(self, title, author, num_pages):
        self.title = title
        self.author = author
        self.num_pages = num_pages

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, Pages: {self.num_pages}"

    def __eq__(self, other):
        return self.title == other.title and self.author == other.author

    def __lt__(self, other):
        return self.num_pages < other.num_pages

    def __gt__(self, other):
        return self.num_pages > other.num_pages

    def __add__(self, other):
        return self.num_pages + other.num_pages

    def __contains__(self, item):
        return item in self.title and item in self.author

    def __getitem__(self, item):
        if item == 'title':
            return self.title
        elif item == 'author':
            return self.author
        elif item == 'num_pages':
            return self.num_pages
        else:
            return f"{item} is not a valid option"


book1 = Book('The Hobbit', 'J.R.R Tolkien', 310)
book2 = Book('Harry Potter', 'J.K. Rowling', 223)

print(book1 < book2)