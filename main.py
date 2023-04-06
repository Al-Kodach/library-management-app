class Library():
    def __init__(self, booksList, name):
        self.name = name
        self.booksList = booksList
        self.lendDict = {}

    # behavior to display all books in library
    def displayBooks(self):
        print(f'we have following books in our library {self.name}')
        for book in self.booksList:
            print(book)

    # behaviou to add books to the library

    def addBook(self, book):
        if book in self.booksList:
            print('Book already exits')
        else:
            self.booksList.append(book)
            print('Book added')

    # behavoir to lend a book

    def lendDict(self, book, user):
        if book in self.booksList:
            if book not in self.lendDict.keys():
                print(f'{book} is available and can be lend')
                self.lendDict.update({book: user})
                print('Book has been lended: Database updated')
            else:
                print(f'Sorry, {book} is already being used by {self.lendDict[book]}')
        else:
            print(f'Appologies!, we dont have this book in our library')

    # behavour to return lend books

    def returnBook(self, book):
        if book in self.lendDict.keys():
            self.lendDict.pop(book)
            print('Book Returned Successfully')

        else:
            print('The book does not exit in the book lending Database')


zee =  Library(['dancing cat', 'flying mat'], 'zee')
print(zee.displayBooks())
print(zee.addBook('getter'))
print(zee.displayBooks())
print(zee.lendDict('getter'))
print(zee.lendDict('getter'))
