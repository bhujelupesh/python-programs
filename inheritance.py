class book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"Title : {self.title}, Author:{self.author}"
    
    def display(self):
        print("This is the display function of parent class")

class xx(book):
    def __init__(self, title, author, pages):
        super().__init__(title,author)
        self.pages = pages
    
    def output(self):
        print(f"Pages{self.pages}, Title: {self.title}")
        
newBook = xx("The Broken Heart","Cupid",528)
print(newBook)
newBook.display()
newBook.output()
