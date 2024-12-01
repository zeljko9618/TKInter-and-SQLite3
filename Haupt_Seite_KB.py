import tkinter as tk
import customtkinter as ctk
#from Config_KB import path
from Funktionen_KB import PygletManager, UserSession
from Kosten_Buch_KB import Kosten_Buch
from Projekt_KB import Projekt
#from Projekt_KB import Projekt_Planung
from Template import Template
from GUI_Objektkatalog import Objektkatalog
from GUI_Anforderung import Anforderung
from GUI_Anforderungsmanagement import Anforderungs_Management


class Hauptseite:
    def __init__(self, root):
        self.root = root
        session = UserSession()
        #session.login("MaxMustermann")
        #print(f"Angemeldeter Benutzer: {session.get_logged_in_user()}")
        self.root.title("Übersicht -> Hauptseite" + (f" Angemeldeter Benutzer: {session.get_logged_in_user()}"))

        # Widgets auf der Hauptseite
        self.label = tk.Label(root, text="Willkommen zur Hauptseite", font=("Audi Type", 15), fg='#BB0A30', pady=10, padx=10)
        self.label.pack()

        # Schaltfläche zur Unterseite
        #self.button = tk.Button(root, text="Zur Unterseite", command=self.zeige_unterseite)
        #self.button.pack()
        
        ctk.set_appearance_mode("light")

        main_frame = ctk.CTkFrame(root, fg_color=("#ffffff", "#262626"))
        main_frame.pack(fill="both", expand=True, side="top")


        button_border_color=("#000000", "#ffffff")
        button_fg_color=("#b3b3b3", "#666666")
        button_text_color=("#1a1a1a", "#e5e5e5")


        button_frame = ctk.CTkFrame(main_frame, fg_color=("#F4F4F4", "#363636"))
        button_frame.pack(fill="both", expand=True, side="top", padx=30, pady=30)
        button_frame.grid_columnconfigure((0, 1, 2), weight=1)
        button_frame.grid_rowconfigure((0, 1, 2), weight=1)

#####################################################################################################################
########### Hier wird der Button für die Projekt_Planung erstellt und der Befehl command ausgeführt 
#####################################################################################################################
        btn = ctk.CTkButton(button_frame, text="Projektplanung\n erstellen", font=("Audi Type Bold", 28), width=400, height=100, corner_radius=5, border_width=1,
                             border_color=button_border_color, fg_color=button_fg_color, text_color=button_text_color, command=self.zeige_Projekt_Planung)
        btn.grid(column=0, row=0, pady=75, padx=75, sticky="nsew")

#####################################################################################################################
########### Hier wird der Button für das Kostenbuch erstellt und der Befehl command ausgeführt 
#####################################################################################################################
        btn2 = ctk.CTkButton(button_frame, text="Kostenbuch füllen", font=("Audi Type Bold", 28), width=400, height=100, corner_radius=5, border_width=1,
                             border_color=button_border_color, fg_color=button_fg_color, text_color=button_text_color, command=self.zeige_Kosten_Buch)
        btn2.grid(column=1, row=0, pady=75, padx=75, sticky="nsew")

#####################################################################################################################
########### Hier wird der Button für die Projekt_Anlage erstellt und der Befehl command ausgeführt 
#####################################################################################################################
        btn3 = ctk.CTkButton(button_frame, text="neues Projekt anlegen", font=("Audi Type Bold", 28), width=400, height=100, corner_radius=5, border_width=1,
                             border_color=button_border_color, fg_color=button_fg_color, text_color=button_text_color, command=self.zeige_Projekt)
        btn3.grid(column=2, row=0, pady=75, padx=75, sticky="nsew")

#####################################################################################################################
########### Hier wird der Button für die Projekt_Anlage erstellt und der Befehl command ausgeführt 
#####################################################################################################################
        btn4 = ctk.CTkButton(button_frame, text="Template", font=("Audi Type Bold", 28), width=400, height=100, corner_radius=5, border_width=1,
                             border_color=button_border_color, fg_color=button_fg_color, text_color=button_text_color, command=self.zeige_Template)
        btn4.grid(column=0, row=1, pady=75, padx=75, sticky="nsew")

#####################################################################################################################
########### Hier wird der Button für den Objektkatalog erstellt und der Befehl command ausgeführt 
#####################################################################################################################
        btn5 = ctk.CTkButton(button_frame, text="Objektkatalog", font=("Audi Type Bold", 28), width=400, height=100, corner_radius=5, border_width=1,
                             border_color=button_border_color, fg_color=button_fg_color, text_color=button_text_color, command=self.zeige_OTOT_anderung)
        btn5.grid(column=1, row=1, pady=75, padx=75, sticky="nsew")

#####################################################################################################################
########### Hier wird der Button für die Projekt_Anlage erstellt und der Befehl command ausgeführt 
#####################################################################################################################
        btn6 = ctk.CTkButton(button_frame, text="Kostenträgerer Anforderung", font=("Audi Type Bold", 24), width=400, height=100, corner_radius=5, border_width=1,
                             border_color=button_border_color, fg_color=button_fg_color, text_color=button_text_color, command=self.zeige_Template)
        btn6.grid(column=2, row=1, pady=75, padx=75, sticky="nsew")

#####################################################################################################################
########### Hier wird der Button für die Projekt_Anlage erstellt und der Befehl command ausgeführt 
#####################################################################################################################
        btn7 = ctk.CTkButton(button_frame, text="Anforderungen", font=("Audi Type Bold", 28), width=400, height=100, corner_radius=5, border_width=1,
                             border_color=button_border_color, fg_color=button_fg_color, text_color=button_text_color, command=self.zeige_Anforderung)
        btn7.grid(column=0, row=2, pady=75, padx=75, sticky="nsew")

#####################################################################################################################
########### Hier wird der Button für die Projekt_Anlage erstellt und der Befehl command ausgeführt
#####################################################################################################################
        btn4 = ctk.CTkButton(button_frame, text="Anforderung- Management", font=("Audi Type Bold", 24), width=400, height=100, corner_radius=5, border_width=1,
                             border_color=button_border_color, fg_color=button_fg_color, text_color=button_text_color, command=self.zeige_Anforderungsmanagement)
        btn4.grid(column=2, row=2, pady=75, padx=75, sticky="nsew")

#####################################################################################################################
########### Hier wird die Seite der Projekt_Planung aufgerufen 
#####################################################################################################################
    def zeige_Projekt_Planung(self):
        Projekt_Planung_fenster = tk.Toplevel(self.root)
        app = Projekt_Planung(Projekt_Planung_fenster)

#####################################################################################################################
########### Hier wird die Seite des Kostenbuch ansich auf gerufen um es zu befüllen 
#####################################################################################################################
    def zeige_Kosten_Buch(self):
        Kosten_Buch_fenster = tk.Toplevel(self.root)
        app = Kosten_Buch(Kosten_Buch_fenster)

#####################################################################################################################
########### Hier wird die Seite zur Erstellung eines Projektes aufgerufen 
#####################################################################################################################
    def zeige_Projekt(self):
        Projekt_fenster = tk.Toplevel(self.root)
        app = Projekt(Projekt_fenster)

#####################################################################################################################
########### Hier wird die Seite zur Erstellung eines Templates aufgerufen 
#####################################################################################################################
    def zeige_Template(self):
        Template_fenster = tk.Toplevel(self.root)
        app = Template(Template_fenster)


#####################################################################################################################
########### Hier wird die Seite zur Erstellung eines Templates aufgerufen 
#####################################################################################################################
    def zeige_OTOT_anderung(self):
        GUI_Objektkatalog = tk.Toplevel(self.root)
        app = Objektkatalog(GUI_Objektkatalog)

#####################################################################################################################
########### Hier wird die Seite zur Anforderungen aufgerufen
#####################################################################################################################
    def zeige_Anforderung(self):
        GUI_Anforderung = tk.Toplevel(self.root)
        app = Anforderung(GUI_Anforderung)

#####################################################################################################################
########### Hier wird die Seite zur Anforderungstemplate aufgerufen
#####################################################################################################################
    def zeige_Anforderungsmanagement(self):
        GUI_Anforderungsmanagement = tk.Toplevel(self.root)
        app = Anforderungs_Management(GUI_Anforderungsmanagement)

#########################################################################################################################
### Hier wird eine Instanz von der schrieftarten Class erstellt
#########################################################################################################################

    pyglet_manager = PygletManager()

if __name__ == "__main__":
    root = tk.Tk()
    app = Hauptseite(root)
    root.mainloop()
