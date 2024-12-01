import tkinter as tk
import tkinter.font as tkfont
from tkinter import ttk
from Funktionen_KB import projekt_speichern
from Funktionen_KB import Datenbank_Manager
from Funktionen_KB import Database_insert
from Funktionen_KB import Treeview_Füller_Projekt
from Funktionen_KB import PygletManager
from Funktionen_KB import MyTreeViewHandler_felder_füllen
from Funktionen_KB import MyTreeViewHandler
from Config_KB import PygletOptions
from def_OTK_Anlage import fill_Combobox, Item_Combobox


class OTK_Anlage:
    def __init__(self, root, text):
        self.root = root
        self.root.title("OTK_Anlage -> GUI_OTK_Anlage")

        self.test_text = text
        self.value_1 = self.test_text['values'][0]
        self.value_2 = self.test_text['values'][1]
        self.value_3 = self.test_text['values'][2]
        self.value_4 = self.test_text['values'][3]

        # Größe des Hauptfensters auf die Bildschirmgröße setzen
        self.screen_width = root.winfo_screenwidth()
        self.screen_height = root.winfo_screenheight()
        root.geometry(f'{int(self.screen_width * 0.8)}x{int(self.screen_height * 0.8)}')

        #####################################################################################################################
        ########### Hier werden die Frames / Widgets erstellt
        #####################################################################################################################

        # Hier wird das Frame für die Audiringe erzeugt,
        self.additional_frame = tk.Frame(root, width=int(root.winfo_screenwidth() * 0.5), padx=10, pady=10,
                                         bg='lightgreen')

        # Hier sollen die Audiringe angezeigt werden, bisher noch ohne Funktion
        self.label_Audi_Ringe = tk.Label(self.additional_frame, font=tkfont.Font(family='Audi Rings', size=40),
                                         text='A')

        # Hier wird das Projektframe erstellt, für den Projektview
        self.projekt_frame = tk.Frame(root, width=int(root.winfo_screenwidth() * 0.5), padx=5, pady=5, bg="red")
        self.tree = ttk.Treeview(self.projekt_frame, columns=("Team", "Object", "Tätigkeit", "OE"), show="headings")
        self.tree.heading("Team", text="Team")
        self.tree.heading("Object", text="Object")
        self.tree.heading("Tätigkeit", text="Tätigkeit")
        self.tree.heading("OE", text="OE")

        # Scrollbar erstellen und mit dem Treeview verbinden
        self.scrollbar = ttk.Scrollbar(self.projekt_frame, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscrollcommand=self.scrollbar.set)

        # Hier wird das Frame mit den Eingabefeldern erzeugt
        self.eingabe_frame = tk.Frame(root, width=int(root.winfo_screenwidth() * 0.5))

        # Sämtliche Beschriftungs- und Eingabefelder
        self.combobox_wert_1 = tk.StringVar()
        self.combobox_wert_2 = tk.StringVar()
        self.combobox_wert_3 = tk.StringVar()
        self.combobox_wert_4 = tk.StringVar()

        self.combobox_wert_1.set(self.value_1)
        self.combobox_wert_2.set(self.value_2)
        self.combobox_wert_3.set(self.value_3)
        self.combobox_wert_4.set(self.value_4)

        self.label_3 = tk.Label(self.eingabe_frame, text="Team", font=("Audi Type", 15), fg='#BB0A30', pady=5, padx=5)
        self.combobox_1 = ttk.Combobox(self.eingabe_frame, font=("Audi Type", 15),
                                       textvariable=str(self.combobox_wert_1))

        self.label_4 = tk.Label(self.eingabe_frame, text="Object", font=("Audi Type", 15), fg='#BB0A30', pady=5, padx=5)
        self.combobox_2 = ttk.Combobox(self.eingabe_frame, font=("Audi Type", 15),
                                       textvariable=str(self.combobox_wert_2))

        self.label_5 = tk.Label(self.eingabe_frame, text="Tätigkeit", font=("Audi Type", 15), fg='#BB0A30', pady=5,
                                padx=5)
        self.combobox_3 = ttk.Combobox(self.eingabe_frame, font=("Audi Type", 15),
                                       textvariable=str(self.combobox_wert_3))

        self.label_6 = tk.Label(self.eingabe_frame, text="OE", font=("Audi Type", 15), fg='#BB0A30', pady=5, padx=5)
        self.combobox_4 = ttk.Combobox(self.eingabe_frame, font=("Audi Type", 15),
                                       textvariable=str(self.combobox_wert_4))

        # Sämtliche Buttons zum Speichern
        self.speichern_1 = tk.Button(self.eingabe_frame, text="Eintragen", font=("Audi Type", 15), fg='#BB0A30', pady=5,
                                     padx=5, command=lambda: (
                Item_Combobox(self.combobox_1.get(), self.combobox_2.get(), self.combobox_3.get(),
                              self.combobox_4.get(), self.tree)))
        self.zurück_1 = tk.Button(root, text="zurück", font=("Audi Type", 15), fg='#BB0A30', pady=10, padx=10,
                                  command=lambda: (root.destroy()))

        ##############################################################################################################
        #### Hier werden die jeweiligen Frames / Widgets auf dem Bildschirm ausgegeben.
        ##############################################################################################################
        self.additional_frame.pack(side=tk.TOP, fill=tk.BOTH, pady=50, padx=5)
        self.label_Audi_Ringe.pack()
        self.projekt_frame.pack(side=tk.BOTTOM, fill="x", pady=5, padx=5)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.eingabe_frame.pack()

        self.label_3.grid(row=3, column=0, pady=10, padx=10)
        self.combobox_1.grid(row=4, column=0, pady=10, padx=10)

        self.label_4.grid(row=3, column=1, pady=10, padx=10)
        self.combobox_2.grid(row=4, column=1, pady=10, padx=10)

        self.label_5.grid(row=3, column=2, pady=10, padx=10)
        self.combobox_3.grid(row=4, column=2, pady=10, padx=10)

        self.label_6.grid(row=3, column=3, pady=10, padx=10)
        self.combobox_4.grid(row=4, column=3, pady=10, padx=10)

        self.speichern_1.grid(row=7, column=3, pady=10, padx=10)
        self.zurück_1.pack(side="right", anchor="se", pady=10, padx=10)

        # Hier werden die Comboboxen gefüllt
        fill_Combobox(self.combobox_1, "SELECT Team_Name FROM tbl_Team")
        fill_Combobox(self.combobox_2, "SELECT Object_Name FROM tbl_Objekt")
        fill_Combobox(self.combobox_3, "SELECT Name FROM tbl_Taetigkeit")
        fill_Combobox(self.combobox_4, "SELECT Name FROM tbl_OE")
        pyglet_manager = PygletManager()


if __name__ == "__main__":
    root = tk.Tk()
    app = OTK_Anlage(root, text={"values": ["Team1", "Object1", "Tätigkeit1", "OE1"]})
    root.mainloop()
