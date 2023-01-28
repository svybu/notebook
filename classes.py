import datetime
import subprocess
from pathlib import Path
import pandas as pd
import os


def create_df():
    try:
        df = pd.read_csv('df.csv', delimiter=';')
    except FileNotFoundError:
        df = pd.DataFrame(columns=['id', 'tags', 'name', 'created', 'changed'])
    return df


df = create_df()


class Field:
    def __init__(self, value):
        self._value = str(value)
        self.value = str(value)

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value


class Name(Field):
    @Field.value.setter
    def value(self, value):
        try:
            fle = Path(f'.//notes//{value}.txt')
            fle.touch(exist_ok=False)
            self.value = str(value)
        except FileExistsError:
            return f'Note with this name already exists'


class Tag(Field):
    @Field.value.setter
    def value(self, value):
        self.value = str(value)
        try:
            self.value = value.lower()
        except:
            pass


class Note():
    def __init__(self, name, tags=[], created=datetime.datetime.now().strftime('%m/%d/%Y, %H:%M')):
        self.name = Name(name)
        self.tags = tags
        if tags:
            self.tags.add_tag
        self.created = created

    # @input_error
    def add_tag(self, tag):
        self.tag.append(Tag(tag))

    def add_note(self):
        try:
            subprocess.call(['open', '-a', 'TextEdit', f'.//notes//{self.name.value}.txt'])
            df.loc[len(df), ['name', 'created']] = [self.name.value, self.created]
        except:
            try:
                subprocess.call(['notepad', f'.//notes//{self.name.value}.txt'])
                df.loc[len(df), ['name', 'created']] = [self.name.value, self.created]
            except FileNotFoundError:
                print("Text editor not found")

    def change_note(self, changed=datetime.datetime.now().strftime('%m/%d/%Y, %H:%M')):
        try:
            subprocess.call(['open', '-a', 'TextEdit', f'.//notes//{self.name.value}.txt'])
            df.loc[df['name'] == self.name.value, ['changed']] = changed
        except:
            try:
                subprocess.call(['notepad', f'.//notes//{self.name.value}.txt'])
                df.loc[df['name'] == self.name.value, ['changed']] = changed
            except FileNotFoundError:
                print("Text editor not found")

    def remove(self):
        global df
        os.remove(f'.//notes//{self.name.value}.txt')
        df = df.loc[df['name'] != self.name.value]
        return df
