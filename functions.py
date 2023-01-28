from classes import Note, df

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


def add_note(args):
    name = args[0]
    ex_note = Note(name)
    ex_note.add_note()
    df.to_csv('df.csv', index=False, sep=';')
    return f'{ex_note.name.value} added'


def change_note(args):
    name = args[0]
    ex_note = Note(name)
    ex_note.change_note()
    df.to_csv('df.csv', index=False, sep=';')
    return f'{ex_note.name.value} changed'


def remove_note(args):
    global df
    name = args[0]
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
