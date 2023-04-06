# This handle communication between the user and the computer.
# lets assume we have a library object created from the class Library

def main():
    while (True):
        print(f"You're welcome to the {libray.name} library")

        choice = '''
        1. Display books
        2. Add book
        3. Lend book
        4. Return book'''
        print(choice)

        userInput = input('Press C to continue and Q to quit')

        if userInput == 'C':
            userChoice = int(input('Select an option to continue'))
            if userChoice == 1:
                library.name.DisplayBooks()

            elif userChoice == 2:
                book = input('Enter the name of the book you will like to add')
                library.name.addBook(book)

            elif userChoice == 3:
                user = input('Enter the name of the user')
                book = input('Enter the book you want to lend')
                library.name.lendBook(book, user)

            elif userChoice == '4':
                book = input('Enter the book you want to return')
                library.name.returnBook(book)

            else:
                print('Please enter a valid option')

        elif userInput == 'Q':
            print(f'Thanks for visiting {library.name}')

        else:
            print('Please enter a valid option')
