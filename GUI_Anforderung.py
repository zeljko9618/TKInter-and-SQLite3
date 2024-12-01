import tkinter as tk
import tkinter.font as tkfont
from tkinter import ttk

from Config_KB import path_1
from Funktionen_KB import PygletManager, UserSession
from def_OTK_Anlage import fill_Combobox
from def_Anforderung import fill_entry, Datenbank_Manager
from datetime import datetime


class Anforderung:
    eingabefeld_zka = None
    combobox_modul = None

    def __init__(self, root):
        self.root = root
        self.root.title("Anforderungen")

        # Größe des Hauptfensters auf die Bildschirmgröße setzen
        self.screen_width = root.winfo_screenwidth()
        self.screen_height = root.winfo_screenheight()
        root.geometry(f'{int(self.screen_width * 0.8)}x{int(self.screen_height * 0.8)}')

        #####################################################################################################################
        ########### Hier werden die Frames / Widgets erstellt
        #####################################################################################################################

        # Hier wird das Frame für die Audiringe erzeugt
        self.additional_frame = tk.Frame(root, width=int(root.winfo_screenwidth() * 0.5), padx=10, pady=10,
                                         bg='lightgreen')

        # Hier sollen die Audiringe angezeigt werden, bisher noch ohne Funktion
        self.label_Audi_Ringe = tk.Label(self.additional_frame, font=tkfont.Font(family='Audi Rings', size=30),
                                         text='A')

        # Scrollbar hinzufügen
        self.canvas = tk.Canvas(root)
        self.scrollbar = tk.Scrollbar(root, orient="vertical", command=self.canvas.yview)
        self.scrollable_frame = tk.Frame(self.canvas)

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(
                scrollregion=self.canvas.bbox("all")
            )
        )

        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        # Hier wird das Frame mit den Eingabefeldern erzeugt
        self.eingabe_frame = tk.Frame(self.scrollable_frame, width=int(root.winfo_screenwidth() * 0.5))

        # Modul Label und Combobox
        self.label_modul = tk.Label(self.eingabe_frame, text="Modul", font=("Audi Type", 15), fg='#BB0A30', pady=5,
                                    padx=5)
        self.combobox_modul = ttk.Combobox(self.eingabe_frame, font=("Audi Type", 12))

        # Datum Label und Eingabefeld (readonly)
        self.label_datum = tk.Label(self.eingabe_frame, text="Datum", font=("Audi Type", 15), fg='#BB0A30', pady=5,
                                    padx=5)
        self.eingabefeld_datum = tk.Entry(self.eingabe_frame, font=("Audi Type", 12))
        # Hier wird das Eingabefeld Datum gefüllt
        self.eingabefeld_datum.insert(0, datetime.now().strftime("%d.%m.%Y"))
        self.eingabefeld_datum.config(state='readonly')

        # Anforderer Label und Eingabefeld
        self.label_anforderer = tk.Label(self.eingabe_frame, text="Anforderer", font=("Audi Type", 15), fg='#BB0A30',
                                         pady=5, padx=5)
        self.eingabefeld_anforderer = tk.Entry(self.eingabe_frame, font=("Audi Type", 12))
        # Hier wird das Eingabefeld Datum gefüllt
        self.eingabefeld_anforderer.insert(0, UserSession().get_logged_in_user())
        self.eingabefeld_anforderer.config(state='readonly')

        # ZKA Label und Eingabefeld (readonly)
        self.label_zka = tk.Label(self.eingabe_frame, text="ZKA", font=("Audi Type", 15), fg='#BB0A30', pady=5, padx=5)
        self.eingabefeld_zka = ttk.Entry(self.eingabe_frame, font=("Audi Type", 12))
        self.eingabefeld_zka.config(state='readonly')

        # Kurztext Label und Eingabefeld
        self.label_kurztext = tk.Label(self.eingabe_frame, text="Kurztext", font=("Audi Type", 15), fg='#BB0A30',
                                       pady=5, padx=5)
        self.eingabefeld_kurztext = tk.Entry(self.eingabe_frame, font=("Audi Type", 12))

        # Anfo_Beschreibung Label und mehrzeiliges Eingabefeld
        self.label_anfo_beschreibung = tk.Label(self.eingabe_frame, text="Anforderungsbeschreibung", font=("Audi Type", 15), fg='#BB0A30',
                                                pady=5, padx=5)
        self.eingabefeld_anfo_beschreibung = tk.Text(self.eingabe_frame, font=("Audi Type", 12), height=3, width=30)

        # Kommentar Label und Eingabefeld
        self.label_kommentar = tk.Label(self.eingabe_frame, text="Kommentar", font=("Audi Type", 15), fg='#BB0A30',
                                        pady=5, padx=5)
        self.eingabefeld_kommentar = tk.Entry(self.eingabe_frame, font=("Audi Type", 12))

        # Prio Label und Eingabefeld
        self.label_prio = tk.Label(self.eingabe_frame, text="Prio", font=("Audi Type", 15), fg='#BB0A30', pady=5,
                                   padx=5)
        self.eingabefeld_prio = tk.Entry(self.eingabe_frame, font=("Audi Type", 12))

        # Status Label und Eingabefeld
        self.label_status = tk.Label(self.eingabe_frame, text="Status", font=("Audi Type", 15), fg='#BB0A30', pady=5,
                                     padx=5)
        self.eingabefeld_status = tk.Entry(self.eingabe_frame, font=("Audi Type", 12))

        # User story Label und Eingabefeld
        self.label_user_story = tk.Label(self.eingabe_frame, text="User story", font=("Audi Type", 15), fg='#BB0A30',
                                         pady=5, padx=5)
        self.eingabefeld_user_story = tk.Entry(self.eingabe_frame, font=("Audi Type", 12))

        # Ticket status Label und Eingabefeld
        self.label_ticket_status = tk.Label(self.eingabe_frame, text="Ticket status", font=("Audi Type", 15),
                                            fg='#BB0A30', pady=5, padx=5)
        self.eingabefeld_ticket_status = tk.Entry(self.eingabe_frame, font=("Audi Type", 12))

        # Speichern Button hinzufügen
        self.speichern_button = tk.Button(self.eingabe_frame, text="Speichern", font=("Audi Type", 15),
                                          command=self.save_data)

        ##############################################################################################################
        #### Hier werden die jeweiligen Frames / Widgets auf dem Bildschirm ausgegeben.
        ##############################################################################################################
        self.additional_frame.pack(side=tk.TOP, fill=tk.BOTH, pady=50, padx=5)
        self.label_Audi_Ringe.pack()

        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.eingabe_frame.pack()
        self.label_modul.grid(row=0, column=0, pady=10, padx=10, sticky="w")
        self.combobox_modul.grid(row=0, column=1, pady=10, padx=10, sticky="w")
        self.label_datum.grid(row=1, column=0, pady=10, padx=10, sticky="w")
        self.eingabefeld_datum.grid(row=1, column=1, pady=10, padx=10, sticky="w")
        self.label_anforderer.grid(row=2, column=0, pady=10, padx=10, sticky="w")
        self.eingabefeld_anforderer.grid(row=2, column=1, pady=10, padx=10, sticky="w")
        self.label_zka.grid(row=3, column=0, pady=10, padx=10, sticky="w")
        self.eingabefeld_zka.grid(row=3, column=1, pady=10, padx=10, sticky="w")
        self.label_kurztext.grid(row=4, column=0, pady=10, padx=10, sticky="w")
        self.eingabefeld_kurztext.grid(row=4, column=1, pady=10, padx=10, sticky="w")
        self.label_anfo_beschreibung.grid(row=5, column=0, pady=10, padx=10, sticky="w")
        self.eingabefeld_anfo_beschreibung.grid(row=5, column=1, pady=10, padx=10, sticky="w")
        self.label_kommentar.grid(row=6, column=0, pady=10, padx=10, sticky="w")
        self.eingabefeld_kommentar.grid(row=6, column=1, pady=10, padx=10, sticky="w")
        self.label_prio.grid(row=7, column=0, pady=10, padx=10, sticky="w")
        self.eingabefeld_prio.grid(row=7, column=1, pady=10, padx=10, sticky="w")
        self.label_status.grid(row=8, column=0, pady=10, padx=10, sticky="w")
        self.eingabefeld_status.grid(row=8, column=1, pady=10, padx=10, sticky="w")
        self.label_user_story.grid(row=9, column=0, pady=10, padx=10, sticky="w")
        self.eingabefeld_user_story.grid(row=9, column=1, pady=10, padx=10, sticky="w")
        self.label_ticket_status.grid(row=10, column=0, pady=10, padx=10, sticky="w")
        self.eingabefeld_ticket_status.grid(row=10, column=1, pady=10, padx=10, sticky="w")

        # Speichern Button
        self.speichern_button.grid(row=11, column=5, pady=10, padx=10, sticky="e")

        # Hier wird Combobox Modul gefüllt
        fill_Combobox(self.combobox_modul, "SELECT DISTINCT Modul FROM tbl_Anfo")

        # Hier wird Combobox ZKA gefüllt zum ersten Mal
        current_item = self.combobox_modul.get()
        fill_entry(self.eingabefeld_zka, f"SELECT ZKA FROM tbl_Anfo WHERE Modul = '{current_item}'")

        # Hier wird sichergestellt, dass jedes mal wenn sich Combobox_modul ändert, sich auch eingabewert_zka aktualisiert
        self.combobox_modul.bind("<<ComboboxSelected>>", self.on_dropdown_change)

    # Die Methode aktualisiert den ZKA jedes Mal wenn sich Modul ändert
    def on_dropdown_change(self, event):
        current_item = self.combobox_modul.get()
        sql_befehl = f"SELECT ZKA FROM tbl_Anfo WHERE Modul = '{current_item}'"
        fill_entry(self.eingabefeld_zka, sql_befehl)

    def save_data(self):
        modul = self.combobox_modul.get()
        datum = self.eingabefeld_datum.get()
        anforderer = self.eingabefeld_anforderer.get()
        zka = self.eingabefeld_zka.get()
        kurztext = self.eingabefeld_kurztext.get()
        anfo_beschreibung = self.eingabefeld_anfo_beschreibung.get("1.0", tk.END).strip()
        kommentar = self.eingabefeld_kommentar.get()
        prio = self.eingabefeld_prio.get()
        status = self.eingabefeld_status.get()
        user_story = self.eingabefeld_user_story.get()
        ticket_status = self.eingabefeld_ticket_status.get()

        sql_befehl = """
            INSERT INTO tbl_Anfo (Modul, Datum, Anforderer, ZKA, Kurztext, Anfo_Beschreibung, Kommentar, Prio, Status, User_Story, Ticket_Status)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """
        params = (
            modul, datum, anforderer, zka, kurztext, anfo_beschreibung, kommentar, prio, status, user_story,
            ticket_status)
        db_manager = Datenbank_Manager(path_1)
        db_manager.execute_query(sql_befehl, params)
        print("Daten erfolgreich gespeichert!")

        # Leere die Eingabefelder
        self.combobox_modul.set('')
        self.eingabefeld_datum.delete(0, tk.END)
        self.eingabefeld_anforderer.delete(0, tk.END)
        self.eingabefeld_zka.delete(0, tk.END)
        self.eingabefeld_kurztext.delete(0, tk.END)
        self.eingabefeld_anfo_beschreibung.delete("1.0", tk.END)
        self.eingabefeld_kommentar.delete(0, tk.END)
        self.eingabefeld_prio.delete(0, tk.END)
        self.eingabefeld_status.delete(0, tk.END)
        self.eingabefeld_user_story.delete(0, tk.END)
        self.eingabefeld_ticket_status.delete(0, tk.END)
        #########################################################################################################################
        ### Hier wird eine Instanz von der Schriftarten-Klasse erstellt
        #########################################################################################################################
        pyglet_manager = PygletManager()

        # Aktualisiere das Fenster, um sicherzustellen, dass alle Widgets korrekt angezeigt werden
        self.root.update()

    if __name__ == "__main__":
        root = tk.Tk()
        app = Anforderung(root)
        root.mainloop()
