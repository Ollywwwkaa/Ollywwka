class Book:
    def __init__(self, title: str, author: str, year: int):
        self.title = title
        self.author = author
        self.year = year
    def __str__(self) -> str:
        return f'"{self.title}" ({self.author}, {self.year})'
    def __repr__(self) -> str:
        return f"Book('{self.title}', '{self.author}', {self.year})"
if __name__ == "__main__":
    book = Book("1984", "George Orwell", 1949)
    print(book)  
    print(repr(book)) 