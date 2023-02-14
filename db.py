import os
import sqlite3
from classes_new import Note
from prettytable import from_db_cursor
from abc import abstractmethod, ABC





class Database():
    def __init__(self ):
        if os.path.exists('notes') == False:
            os.mkdir('notes')
        self.connection = sqlite3.connect('.//notes//notes.db')
        self.cur = self.connection.cursor()
        self.cur.execute("""CREATE TABLE IF NOT EXISTS notes(
                   note_id INTEGER PRIMARY KEY,
                   tag TEXT,
                   name TEXT,
                   created TEXT,
                   changed TEXT);
                """)
        self.connection.commit()

    def add_record(self, note: Note):
        try:
            with self.connection:
                values = (note.name, note.created)
                self.cur.execute(f"""INSERT INTO notes(name, created) 
                           VALUES(?,?);""", values)
                self.connection.commit()
        except sqlite3.Error as error:
            raise f"Error creating attribute: {error}"
        finally:
            self.connection.commit()

    def change_record(self, note):
        try:
            with self.connection:
                self.cur.execute(f"""UPDATE notes
                                    SET changed = f{note.changed} 
                                    WHERE name = {note.name});""")
                self.connection.commit()
        except sqlite3.Error as error:
            raise f"Error creating attribute: {error}"
        finally:
            self.connection.commit()

    def remove_record(self, note):
        try:
            with self.connection:
                self.cur.execute(f"""DELETE FROM  notes 
                                    WHERE name = {note.name});""")
                self.connection.commit()
        except sqlite3.Error as error:
            raise f"Error creating attribute: {error}"
        finally:
            self.connection.commit()

    def add_tag(self, note):
        note.change_tag()
        try:
            with self.connection:
                self.cur.execute(f"""UPDATE notes
                                    SET tag = f{note.tag} 
                                    WHERE name = {note.name});""")
                self.connection.commit()
        except sqlite3.Error as error:
            raise f"Error creating attribute: {error}"
        finally:
            self.connection.commit()

    def remove_tag(self, note):
        note.remove_tag()
        try:
            with self.connection:
                self.cur.execute(f"""UPDATE notes
                                    SET tag = f{note.tag} 
                                    WHERE name = {note.name});""")
                self.connection.commit()
        except sqlite3.Error as error:
            raise f"Error creating attribute: {error}"
        finally:
            self.connection.commit()

    """def show_records(self):
        try:
            with self.connection:
                self.cur.execute("SELECT * FROM notes")
                table = from_db_cursor(self.cur)
                print(table)
        except sqlite3.Error as error:
            raise f"Error creating attribute: {error}"
        finally:
            self.connection.commit()"""

    def check_name(self, name):
        try:
            with self.connection:
                self.cur.execute("SELECT name FROM notes")
                if name in self.cur.fetchall():
                    r = True
                else:
                    r = False
                return r
        except sqlite3.Error as error:
            raise f"Error creating attribute: {error}"
        finally:
            self.connection.commit()

    def filter(self,tag):
        try:
            with self.connection:
                self.cur.execute(f"SELECT name, created, changed FROM notes WHERE tag={tag}")
                table = from_db_cursor(self.cur)
                print(table)
        except sqlite3.Error as error:
            raise f"Error creating attribute: {error}"
        finally:
            self.connection.commit()

"""    def sort(self):
        try:
            with self.connection:
                self.cur.execute(f"SELECT name, created, changed FROM notes ORDER BY created;")
                table = from_db_cursor(self.cur)
                print(table)
        except Exception as error:
            raise f"Error creating attribute: {error}"
        finally:
            self.connection.commit()"""

class Table(ABC):
    @abstractmethod
    def show_all(self, db: Database):
        pass

    @abstractmethod
    def sort(self, db: Database):
        pass

    @abstractmethod
    def filter(self, db: Database, tag):
        pass

class Notes_table(Table):
    def show_all(self, db: Database):
        try:
            with db.connection:
                db.cur.execute("SELECT * FROM notes")
                table = from_db_cursor(db.cur)
                print(table)
        except sqlite3.Error as error:
            raise f"Error creating attribute: {error}"
        finally:
            db.connection.commit()

    def sort(self, db: Database):
        try:
            with db.connection:
                db.cur.execute(f"SELECT name, created, changed FROM notes ORDER BY created;")
                table = from_db_cursor(db.cur)
                print(table)
        except Exception as error:
            raise f"Error creating attribute: {error}"
        finally:
            db.connection.commit()

    def filter(self, db: Database, tag):
        try:
            with db.connection:
                db.cur.execute(f"SELECT name, created, changed FROM notes WHERE tag={tag}")
                table = from_db_cursor(db.cur)
                print(table)
        except sqlite3.Error as error:
            raise f"Error creating attribute: {error}"
        finally:
            db.connection.commit()

db = Database()
