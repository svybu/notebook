from functions import parser_string, wrong_command
from decorator import input_error
from classes import synk


@input_error
def main():
    try:
        while True:
            u_input = input('Enter command ')
            handler, *args = parser_string(u_input)
            if handler == wrong_command:
                print('Wrong command(')
            elif handler == exit:
                print("Good bye!")
                break
            else:
                result = handler(*args)
                print(result)
    finally:
        print(" ")


if __name__ == '__main__':
    synk()
    print('Welcome to NoteBook')
    main()
