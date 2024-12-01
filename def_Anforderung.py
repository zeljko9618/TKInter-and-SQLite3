import sqlite3
from Config_KB import path_1
import tkinter as tk


class Datenbank_Manager:
    def __init__(self, path_1):
        self.path_1 = path_1  # Speichert den Pfad zur Datenbank

    def select_data(self, sql):
        self.connect = sqlite3.connect(self.path_1)  # Initialisiere die Verbindung zur Datenbank
        self.cursor = self.connect.cursor()
        try:
            self.sql = sql
            self.cursor.execute(self.sql)
            result = self.cursor.fetchall()
            return result
        except sqlite3.Error as e:
            print(f"Fehler beim Ausführen des SELECT-Befehls: {e}")
        finally:
            self.connect.close()

    def execute_query(self, sql, params=()):
        self.connect = sqlite3.connect(self.path_1)  # Initialisiere die Verbindung zur Datenbank
        self.cursor = self.connect.cursor()
        try:
            self.cursor.execute(sql, params)
            self.connect.commit()
        except sqlite3.Error as e:
            print(f"Fehler beim Ausführen des SQL-Befehls: {e}")
        finally:
            self.connect.close()

#####################################################################################################################
##### Hier werden die zwei methoden definiert, die dafür zuständig sind, dynamische Felder in Anforderungen zu füllen
#####################################################################################################################
class fill_Combobox:
    def __init__(self, combobox, sql_befehl):
        # Stelle die Verbindung zur Datenbank her
        db_manager = Datenbank_Manager(path_1)
        self.sql_befehl = sql_befehl
        # Speichere die selektierten Elemente in aufruf
        self.aufruf = db_manager.select_data(self.sql_befehl)
        # Fülle die übergebene ComboBox mit den selektierten Werten, aber nur nicht-leere Werte
        combobox['values'] = [item[0] for item in self.aufruf if item[0]]  # Extrahiere die Werte aus den Tupeln und filtere leere Werte


def fill_entry(entry, sql_befehl):
    # Stelle die Verbindung zur Datenbank her
    db_manager = Datenbank_Manager(path_1)
    # Speichere die selektierten Elemente in aufruf
    aufruf = db_manager.select_data(sql_befehl)

    entry.config(state='normal')  # Setze den Zustand auf normal
    entry.delete(0, tk.END)  # Lösche den aktuellen Inhalt des Eingabefelds
    if aufruf:
        entry.insert(0, aufruf[0][0])  # Füge den neuen Text ein (erster Wert des ersten Tupels)
    entry.config(state='readonly')  # Setze den Zustand zurück auf readonly



