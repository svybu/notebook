
import os
import subprocess
from pathlib import Path
from decorator import input_error
import time
import datetime

"""class Notebook(UserDict):
    #def __init__(self):

    def save(self):

    def load(self):
        if os.path.exists('notes') == False:
            os.mkdir('notes')
        conn = sqlite3.connect('.//notes//db.csv')
        cur = conn.cursor()
        return cur

    def open_note(self, name):


    def add_note(self, note):


    def change_note(self, note):

    def remove_note(self, note):

"""



class Note():
    def __init__(self, name: str, created=datetime.datetime.now().strftime('%m/%d/%Y, %H:%M'), tag = '', changed = None):
        self.name = name
        self.created = created

    def open_note(self, change=False):
        try:
            subprocess.call(['open', '-a', 'TextEdit', f'.//notes//{self.name}.txt'])
        except:
            try:
                subprocess.call(['notepad', f'.//notes//{self.name}.txt'])
            except FileNotFoundError:
                print("Text editor not found")
        if change:
            self.changed = datetime.datetime.now().strftime('%m/%d/%Y, %H:%M')

    def change_note(self):
        self.changed = datetime.datetime.now().strftime('%m/%d/%Y, %H:%M')
        self.open_note()

    def remove_note(self):
        os.remove(f'.//notes//{self.name}.txt')

    def change_tag(self, tag):
        self.tag = tag

    def remove_tag(self):
        self.tag = ''



