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
            bookDataBase = open(dbName, 'a')
            bookDataBase.write(book)
            print('Book added')

    # behavoir to lend a book

    def lendBook(self, book, user):
        if book in self.booksList:
            if book not in self.lendDict.keys():
                print(f'{book} is available and can be lend')
                self.lendDict.update({book: user})
                print('Book has been lended: Database updated')
            else:
                print(
                    f'Sorry, {book} is already being used by {self.lendDict[book]}')
        else:
            print(f'Appologies!, we dont have this book in our library')

    # behavour to return lend books

    def returnBook(self, book):
        if book in self.lendDict.keys():
            self.lendDict.pop(book)
            print('Book Returned Successfully')

        else:
            print('The book does not exit in the book lending Database')


def main():
    print(f"You're welcome to the {library.name} library")
    while (True):
        choice = '''
        1. Display all books
        2. Add a book
        3. Lend a book
        4. Return a book
        '''
        print(choice)

        userInput = input('Press C to continue and Q to quit: ').capitalize()

        if userInput == 'C':
            userChoice = int(input('Select an option to continue: '))

            if userChoice == 1:
                library.displayBooks()

            elif userChoice == 2:
                book = input('Enter the name of the book you want to add: ')
                library.addBook(book)

            elif userChoice == 3:
                user = input('Enter the name of the user:')
                book = input('Enter the name of the book you want to lend: ')
                library.lendBook(book, user)

            elif userChoice == 4:
                book = input('Enter the book you want to return: ')
                library.returnBook(book)

            else:
                print('Please choose a valid option')

        elif userInput == 'Q':
            break

        else:
            print('Please enter a valid option')


if __name__ == '__main__':
    booksList = []
    libraryName = input('Enter library name: ')

    dbName = input('Enter the name of the database with extention: ')
    bookdb = open(dbName, 'r')

    for book in bookdb:
        booksList.append(book)

    library = Library(booksList, libraryName)
main()
