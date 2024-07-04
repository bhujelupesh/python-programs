class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
    
    def __str__(self):
        return f"{self.title} by {self.author} ({self.year})"
    
book1 = Book("The Misfits","Devil",1998)

print(book1)
