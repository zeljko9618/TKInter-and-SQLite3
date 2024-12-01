import sqlite3
import tkinter as tk
import pyglet
from Config_KB import path_1
from tkinter import messagebox

#############################################################################
### Hier werden die Daten aus der Datenbank abgerufen für die Stammdaten
############################################################################# 
class Datenbank_Manager:
    def __init__(self):
        pass
    def select_data(self, sql):
        #item_values = self.treeview.item(item, "values")
           # self.Berichts_Element = item_values[0]  # Zugriff a
        self.select = sql[0]
        self.params = sql[1]
        self.conn = sqlite3.connect(path_1)  # Initialisiere die Verbindung zur Datenbank
        self.cursor = self.conn.cursor()
        try:
            if self.params:
                self.cursor.execute(self.select, self.params)
            else:
                self.cursor.execute(sql)
            result = self.cursor.fetchall()
            return result
        except sqlite3.Error as e:
            print(f"Fehler beim Ausführen des SELECT-Befehls: {e}")
        finally:
            self.conn.close()

###################################################################################
### Hier wird das one_click ereignis im Template aufgerufen 
###################################################################################
class MyTreeViewHandler_Anforderungs_Management:
    def __init__(self, treeview, tab1, tab2, tab3):
        self.tab1 = tab1
        self.tab2 = tab2
        self.tab3 = tab3
        self.treeview = treeview
        print(f"Treeview objekt: {self.treeview}")
        self.treeview.bind("<<TreeviewSelect>>", self.on_treeview_click)

    def on_treeview_click(self, event):
        selected_item = self.treeview.selection()  # Ändere diese Zeile
        print(selected_item)
        item = self.treeview.item(selected_item)
        if selected_item:
            item = selected_item[0]
            # Werte der ausgewählten Zeile
            item_text = self.treeview.item(item, "text")
            item_values = self.treeview.item(item, "values")
            self.ID = item_values[0]  # Zugriff auf den ersten Wert
            self.Anforderer = item_values[2]
            print(item_values)

            # Diese Schleifen löschen alle Elemente in den tab1, tab2 und tab3 Widgets.
            for item in self.tab1.get_children():
                self.tab1.delete(item)
            for item in self.tab2.get_children():
                self.tab2.delete(item)
            for item in self.tab3.get_children():
                self.tab3.delete(item)

            # Hier werden die Daten aus der Datenbank abgerufen,
            self.sql = f"SELECT Kurztext from tbl_Anfo where Kurztext = '{self.ID}'"
            self.db_manager_tab1 = Datenbank_Manager()
            data = self.db_manager_tab1.select_data(self.sql)
            # Füge die Daten in Kurztext
            for i, Kurztext in enumerate(data):
                self.tab1.insert('', 'end', iid=i, values=Kurztext)

            # Hier werden die Daten aus der Datenbank abgerufen,
            self.sql = "SELECT Kommentar from tbl_Anfo where ID = '" + self.ID + "'"
            self.db_manager_tab2 = Datenbank_Manager()
            data = self.db_manager_tab2.select_data(self.sql)
            # Füge die Daten in Kommentar
            for i, Kommentar in enumerate(data):
                self.tab2.insert('', 'end', iid=i, values=Kommentar)

            # Hier werden die Daten aus der Datenbank abgerufen,
            self.sql = "SELECT Anforderungsbeschreibung from tbl_Anfo where ID = '" + self.ID + "'"
            self.db_manager_tab3 = Datenbank_Manager()
            data = self.db_manager_tab3.select_data(self.sql)
            # Füge die Daten in Kommentar
            for i, Anforderungsbeschreibung in enumerate(data):
                self.tab3.insert('', 'end', iid=i, values=Anforderungsbeschreibung)

###################################################################################
### Hier wird das rechts_click ereignis im Template aufgerufen 
###################################################################################
class TreeviewWithMenu:
    def __init__(self, treeview):
        self.treeview_rechtsklick = treeview

        # Kontextmenü erstellen
        self.menu = tk.Menu(self.treeview_rechtsklick, tearoff=0)
        self.menu.add_command(label="Änderung -> Objekt Tätigkeit OE Team", command=self.delete_item)

        self.menu1 = tk.Menu(self.treeview_rechtsklick, tearoff=0)
        self.menu1.add_command(label="Löschen1", command=self.delete_item)
        self.menu1.add_command(label="Freischalten1", command=self.delete_item)

        self.menu2 = tk.Menu(self.treeview_rechtsklick, tearoff=0)
        self.menu2.add_command(label="Löschen2", command=self.delete_item)
        self.menu2.add_command(label="Freischalten2", command=self.delete_item)

        self.menu3 = tk.Menu(self.treeview_rechtsklick, tearoff=0)
        self.menu3.add_command(label="Löschen3", command=self.delete_item)
        self.menu3.add_command(label="Freischalten3", command=self.delete_item)

        self.menu4 = tk.Menu(self.treeview_rechtsklick, tearoff=0)
        self.menu4.add_command(label="Löschen4", command=self.delete_item)
        self.menu4.add_command(label="Freischalten4", command=self.delete_item)

        self.menu5 = tk.Menu(self.treeview_rechtsklick, tearoff=0)
        self.menu5.add_command(label="Löschen5", command=self.delete_item)
        self.menu5.add_command(label="Freischalten5", command=self.delete_item)

        self.menu6 = tk.Menu(self.treeview_rechtsklick, tearoff=0)
        self.menu6.add_command(label="Löschen6", command=self.delete_item)
        self.menu6.add_command(label="Freischalten6", command=self.delete_item)

        self.menu7 = tk.Menu(self.treeview_rechtsklick, tearoff=0)
        self.menu7.add_command(label="Löschen7", command=self.delete_item)
        self.menu7.add_command(label="Freischalten7", command=self.delete_item)
        # Rechtsklick-Ereignis binden
        self.treeview_rechtsklick.bind("<Button-3>", self.on_right_click)

    def on_right_click(self, event):
        # Get the region where the click occurred
        region = self.treeview_rechtsklick.identify_region(event.x, event.y)
        if region == "cell":
            # Get the column where the click occurred
            column = self.treeview_rechtsklick.identify_column(event.x)
            if column == "#1":
                self.menu.post(event.x_root, event.y_root)
            elif column == "#2":
                self.menu1.post(event.x_root, event.y_root)
            elif column == "#3":
                self.menu2.post(event.x_root, event.y_root)
            elif column == "#4":
                self.menu3.post(event.x_root, event.y_root)
            elif column == "#5":
                self.menu4.post(event.x_root, event.y_root)
            elif column == "#6":
                self.menu5.post(event.x_root, event.y_root)
            elif column == "#7":
                self.menu6.post(event.x_root, event.y_root)
            elif column == "#8":
                self.menu7.post(event.x_root, event.y_root)

    def delete_item(self):
        try:
            selected_item = self.treeview_rechtsklick.selection()[0]
            item = self.treeview_rechtsklick.item(selected_item)
            # Werte der ausgewählten Zeile
            text = item['text']
            col1_value = item['values'][0]
            col2_value = item['values'][1]
            col3_value = item['values'][2]

            print(f"Text: {text}")
            print(f"Spalte 1: {col1_value}")
            print(f"Spalte 2: {col2_value}")
            print(f"Spalte 3: {col3_value}")

            KT_fenster = tk.Toplevel()
            KT_fenster.grab_set()  # Macht das Fenster modal
            app = MyTreeViewHandler_Anforderungs_Management(KT_fenster, item)
        except IndexError:
            messagebox.showerror("Fehler", "Bitte einen Datensatz markieren")
            self.treeview_rechtsklick.focus_set()  # Setzt den Fokus zurück auf das Treeview-Widget

#########################################################################################################################
### Wird ausgeführt, wenn ich auf dem Button Suchen im Template clicke
##########################################################################################################################
class Anforderungssuche_suche:
    def suchen(self, text_1, text_2, text_3):
        self.text_1 = text_1
        self.text_2 = text_2
        self.text_3 = text_3

        self.query = "SELECT Modul, Datum, Anforderer, ZKA, Prio, Status, User_Story, Ticket_Status from tbl_Anfo"

        # Dynamische Filter erstellen
        self.filters = []
        self.params = []

        if self.text_1:
            self.filters.append("Modul LIKE ?")
            self.params.append(f"%{self.text_1}%")

        if self.text_2:
            self.filters.append("ZKA LIKE ?")
            self.params.append(f"%{self.text_2}%")

        if self.text_3:
            self.filters.append("Kurztext LIKE ?")
            self.params.append(f"%{self.text_3}%")

        # Wenn Filter vorhanden sind, WHERE-Klausel hinzufügen
        if self.filters:
            self.query += " WHERE " + " AND ".join(self.filters)

        self.db_manager = Datenbank_Manager()
        self.select_command = (self.query, self.params)  # Dein SELECT-Befehl hier
        self.tree_filler = Treeview_Fueller_Anforderungsmanagement(self.treeview_left_frame, self.db_manager)
        self.tree_filler.fill_treeview(self.select_command)
        print(self.tree_filler)


    ### Hier wird ein Projekt_Treeview gefüllt mit Daten aus der Datenbank
############################################################################# 
class Treeview_Fueller_Anforderungsmanagement:
    def __init__(self, parent, db_manager_s):
        self.tree = parent
        self.db_manager = db_manager_s
        self.tree.pack(expand=True, fill="both", side=tk.LEFT, pady=5, padx=5)

    def fill_treeview(self, select_command):
        # Leere das Treeview
        for item in self.tree.get_children():
            self.tree.delete(item)

        # Beispiel-Daten
        data = self.db_manager.select_data(select_command)

        # Füge die Daten hinzu
        for i, (Kurztext, Kommeentar, Anforderungsbeschreibung) in enumerate(data):
            self.tree.insert('', 'end', iid=i, values=(Kurztext, Kommeentar, Anforderungsbeschreibung))