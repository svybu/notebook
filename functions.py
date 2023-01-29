from classes import Note, df
from decorator import input_error
"""*****************основна логіка роботи та функції*****************"""


# @input_error
def hello(a):
    return 'How can I help you?'


def wrong_command():
    return 'Wrong command('


# @input_error
def parser_string(u_input):
    command, *args = u_input.split()
    if args:
        if ((command + ' ' + args[0]).lower()) in ['show all', 'good bye']:
            command = (command + ' ' + args[0]).lower()
        handler = OPTIONS.get(command.lower(), wrong_command())
    else:
        handler = OPTIONS.get(command.lower(), wrong_command())
    return handler, args

@input_error
def add_note(args):
    name = args[0]
    if df['name'].isin([name]).any():
        raise FileExistsError
    else:
        ex_note = Note(name)
        ex_note.add_note()
        df.to_csv('df.csv', index=False, sep=';')
    return f'{ex_note.name.value} added'

@input_error
def change_note(args):
    name = args[0]
    if df['name'].isin([name]).any() == False:
        raise FileNotFoundError
    else:
        ex_note = Note(name)
        ex_note.change_note()
        df.to_csv('df.csv', index=False, sep=';')
        return f'{ex_note.name.value} changed'

@input_error
def remove_note(args):
    global df
    name = args[0]
    if df['name'].isin([name]).any() == False:
        raise FileNotFoundError
    else:
        ex_note = Note(name)
        df = ex_note.remove()
        df.to_csv('df.csv', index=False, sep=';')
        return f'{ex_note.name.value} removed'


def show_all(a):
    result = df
    return result


OPTIONS = {"hello": hello,
           "add": add_note,
           'change': change_note,
           'delete': remove_note,
           'remove': remove_note,
           'show all': show_all,
           'good bye': exit,
           'close': exit,
           'exit': exit,
           '.': exit
           }
