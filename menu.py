def main():
    while (True):
        print(f"You're welcome to {libray.name} library")

        choice = '''
        1. Display books
        2. Add book
        3. Lend book
        4. Return book'''
        print(choice)

        userChoice = input('Select C to continou or Q to quit')

        if userChoice == 'C':
            userInput = input('Enter an option')
            if userInput == '1':
                library.name.DisplayBooks()

            elif userInput == '2':
                library.name.addBook()

            elif userInput == '3':
                library.name.lendBook()

            elif userInput == '4':
                library.name.returnBook()

            else:
                print('Please enter a valid option')

        else:
            print(f'Thanks for visiting {library.name}')
