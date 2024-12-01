import tkinter as tk
import tkinter.font as tkfont
from tkinter import ttk

from Funktionen_KB import PygletManager
from Projekt_KB import Projekt
from def_Objektkatalog import template_suche
from def_Objektkatalog import TreeviewWithMenu
from def_Objektkatalog import Datenbank_Manager_S
from def_Objektkatalog import Treeview_Füller_Template
from def_Objektkatalog import MyTreeViewHandler_Template


from Config_KB import PygletOptions


class Objektkatalog:
    def __init__(self, root):
        self.root = root
        self.root.title("Stammdaten Relevanz")      
       
       # Größe des Hauptfensters auf die Bildschirmgröße setzen
        self.screen_width = root.winfo_screenwidth()
        self.screen_height = root.winfo_screenheight()
        root.geometry(f'{int(self.screen_width * 0.8)}x{int(self.screen_height * 0.8)}')


#####################################################################################################################
########### Hier werden die Frames / Widgets erstellt
#####################################################################################################################
        
        # Hier wird das Frame für die Audiringe erzeugt
        self.additional_frame = tk.Frame(root, width=int(root.winfo_screenwidth() * 0.5), padx=1, pady=1, bg='lightgreen')
        # Hier sollen die Audiringe angezeigt werden, bisher noch ohne funktion
        self.label_Audi_Ringe = tk.Label(self.additional_frame, font=tkfont.Font(family='Audi Rings', size=30), text='A')

        self.additional_frame.pack(side=tk.TOP, fill=tk.BOTH, pady=5, padx=5)        
        self.label_Audi_Ringe.pack(side=tk.TOP, fill=tk.BOTH, pady=5, padx=5)

        # Vertikales PanedWindow erstellen
        self.vertical_paned_window = ttk.PanedWindow(root, orient=tk.VERTICAL)
        self.vertical_paned_window.pack(fill=tk.BOTH, expand=True)

        # Horizontales PanedWindow erstellen
        self.horizontal_paned_window = ttk.PanedWindow(root, orient=tk.HORIZONTAL)
        self.vertical_paned_window.add(self.horizontal_paned_window, weight=4)

        # Zwei Frames zum horizontalen PanedWindow hinzufügen
        self.left_frame = tk.Frame(self.horizontal_paned_window, width=200, height=300, relief=tk.SUNKEN)
        self.right_frame = tk.Frame(self.horizontal_paned_window, width=400, height=300, relief=tk.SUNKEN)
        #self.treeview_left_frame = ttk.Treeview(self.left_frame, show="tree")  
         # Erstelle das Treeview-Widget
        self.treeview_left_frame = ttk.Treeview(self.left_frame , columns=('Team_Name', 'Objekt_Name', 'Taetigkeit', 'OE'), show='headings')
        self.treeview_left_frame.pack(expand=True, fill="both", side=tk.LEFT, pady=5, padx=5)
    
        vscrollbar = ttk.Scrollbar(self.left_frame, orient="vertical", command=self.treeview_left_frame.yview)
        self.treeview_left_frame.configure(yscrollcommand=vscrollbar.set)

        # Treeview und Scrollbalken packen
        self.treeview_left_frame.pack(fill="both", expand=True)
        vscrollbar.pack(side="right", fill="y")

        
        # Spaltenüberschriften
        self.treeview_left_frame.heading('Team_Name', text='Team_Name')
        self.treeview_left_frame.heading('Objekt_Name', text='Objekt_Name')
        self.treeview_left_frame.heading('Taetigkeit', text='Taetigkeit')
        self.treeview_left_frame.heading('OE', text='OE')


        # Setze die Spaltenbreite
        self.treeview_left_frame.column('Team_Name', width=100)
        self.treeview_left_frame.column('Objekt_Name', width=150)
        self.treeview_left_frame.column('Taetigkeit', width=100)
        self.treeview_left_frame.column('OE', width=100)
        

        # Frames zum horizontalen PanedWindow hinzufügen
        self.horizontal_paned_window.add(self.left_frame, weight=5)
        self.horizontal_paned_window.add(self.right_frame, weight=1)

        # Frame unterhalb des horizontalen PanedWindow hinzufügen
        self.bottom_frame = tk.Frame(self.vertical_paned_window, height=150, relief=tk.RAISED)
        self.vertical_paned_window.add(self.bottom_frame, weight=1)

        # Notebook (Registerkarten) erstellen
        self.notebook = ttk.Notebook(self.bottom_frame)
        self.notebook.pack(fill=tk.BOTH, expand=True)

        # Drei Registerkarten hinzufügen
        self.tab1 = tk.Frame(self.notebook)
        self.tab2 = tk.Frame(self.notebook)
        self.tab3 = tk.Frame(self.notebook)

        
        self.notebook.add(self.tab2, text="Steckbrief")
        self.notebook.add(self.tab3, text="Teams mit Genehmiger")
        self.notebook.add(self.tab1, text="Freischaltungen")
        

        style = ttk.Style()
        style.configure('TNotebook.Tab', font=("Audi Type", 12), foreground='#BB0A30', padding=[10,10])
        style.configure("Treeview.Heading", background="grey", font=("Audi Type", 12), foreground='#BB0A30', padding=[10,10])

       
        # Tabs
        self.tree_guiN = ttk.Treeview(self.tab2, columns=("Team", "Objekt", "Tätigkeit", "Kst"), show='headings', selectmode="extended")
        self.tree_guiN.heading("Team", text="Team")
        self.tree_guiN.heading("Objekt", text="Objekt")
        self.tree_guiN.heading("Tätigkeit", text= "Tätigkeit")
        self.tree_guiN.heading("Kst", text= "Kst")
        self.tree_guiN.pack(expand=True, fill='both', padx=10, pady=10)   
        

        self.tree_Teams = ttk.Treeview(self.tab3, columns=("Berichtselement", "Team", "BteBesteller"), show='headings')
        self.tree_Teams.heading("Berichtselement", text="Berichtselement")
        self.tree_Teams.heading("Team", text="Team")
        self.tree_Teams.heading("BteBesteller", text="BteBesteller")
        self.tree_Teams.pack(expand=True, fill='both', padx=10, pady=10) 
        

        self.tree = ttk.Treeview(self.tab1, columns=("Kostenträger", "Kostenstelle", "Gültig_von", "Gültig_bis", "Jahresscheibe", "EL_FL"), show='headings')
        self.tree.heading("Kostenträger", text="Kostenträger")
        self.tree.heading("Kostenstelle", text="Kostenstelle")
        self.tree.heading("Gültig_von", text= "Gültig_von")
        self.tree.heading("Gültig_bis", text= "Gültig_bis")
        self.tree.heading("Jahresscheibe", text="Jahresscheibe")
        self.tree.heading("EL_FL", text= "EL_FL")
        self.tree.pack(expand=True, fill='both', padx=10, pady=10)       
               
        
       
               
        # sämtliche Beschriftungs und Eingabe Felder
        self.label_ID = tk.Label(self.right_frame, text="Team", font=("Audi Type", 15), fg='#BB0A30', pady=5, padx=5)   
        self.eingabefeld_wert_ID = tk.StringVar()
        self.eingabefeld_ID = tk.Entry(self.right_frame, font=("Audi Type", 15), textvariable=str(self.eingabefeld_wert_ID)) 
        #self.eingabefeld_ID.config(state='readonly')
        self.label_1 = tk.Label(self.right_frame, text="Object", font=("Audi Type", 15), fg='#BB0A30', pady=5, padx=5)                
        self.eingabefeld_wert_1 = tk.StringVar()
        self.eingabefeld_1 = tk.Entry(self.right_frame, font=("Audi Type", 15), textvariable=str(self.eingabefeld_wert_1))   
        self.label_2 = tk.Label(self.right_frame, text="Tätigkeit", font=("Audi Type", 15), fg='#BB0A30', pady=5, padx=5)
        self.eingabefeld_wert_2 = tk.StringVar()
        self.eingabefeld_2 = tk.Entry(self.right_frame, font=("Audi Type", 15), textvariable=str(self.eingabefeld_wert_2))  
        self.label_3 = tk.Label(self.right_frame, text="OE", font=("Audi Type", 15), fg='#BB0A30', pady=5, padx=5)
        self.eingabefeld_wert_3 = tk.StringVar()
        self.eingabefeld_3 = tk.Entry(self.right_frame, font=("Audi Type", 15), textvariable=str(self.eingabefeld_wert_3))         
           
        # sämtliche Buttons zum speichern
        self.suchen_1 = tk.Button(self.right_frame, text="suchen", font=("Audi Type", 10), fg='#BB0A30', pady=10, padx=10, command=lambda: (template_suche.suchen(self, self.eingabefeld_wert_ID.get(), self.eingabefeld_wert_1.get(), self.eingabefeld_wert_2.get(), self.eingabefeld_wert_3.get())))
        #self.suchen_2 = tk.Button(self.right_frame, text="suchen", font=("Audi Type", 10), fg='#BB0A30', pady=10, padx=10, command=lambda: (template_suche.suchen(self,"BE_Text Like '%"+(str(self.eingabefeld_wert_1.get()))+"%'" ),self.eingabefeld_1.delete(0,tk.END)))
        #self.suchen_3 = tk.Button(self.right_frame, text="suchen", font=("Audi Type", 10), fg='#BB0A30', pady=10, padx=10, command=lambda: (template_suche.suchen(self,"Kostentraeger Like '%"+(str(self.eingabefeld_wert_2.get()))+"%'" ),self.eingabefeld_2.delete(0,tk.END)))
        #self.suchen_4 = tk.Button(self.right_frame, text="suchen", font=("Audi Type", 10), fg='#BB0A30', pady=10, padx=10, command=lambda: (template_suche.suchen(self,"KT_Text Like '%"+(str(self.eingabefeld_wert_3.get()))+"%'" ),self.eingabefeld_3.delete(0,tk.END)))
        
##############################################################################################################
#### Hier werden die jeweiligen Frames / Widgets auf dem Bildschirm ausgegeben.
##############################################################################################################     
       
        self.label_ID.grid(row=0, column= 0, pady=5, padx=10)
        self.eingabefeld_ID.grid(row=1, column=0, pady=5, padx=10) 
        self.label_1.grid(row=2, column=0, pady=5, padx=10)
        self.eingabefeld_1.grid(row=3, column=0, pady=5, padx=10)  
        self.label_2.grid(row=4, column=0, pady=5, padx=10)
        self.eingabefeld_2.grid(row=5, column=0, pady=5, padx=10)  
        self.label_3.grid(row=6, column=0, pady=5, padx=10)
        self.eingabefeld_3.grid(row=7, column=0, pady=5, padx=10)  
        self.suchen_1.grid(row=1, column=1, pady=10, padx=5) 
        #self.suchen_2.grid(row=3, column=1, pady=10, padx=5) 
        #self.suchen_3.grid(row=5, column=1, pady=10, padx=5)
        #self.suchen_4.grid(row=7, column=1, pady=10, padx=5)

#########################################################################################################################
### Hier wird der Projekt_treeview oben Quer aus der Datenbank mit dem Datenbank_Manager befüllt
#########################################################################################################################

        rechts_click = TreeviewWithMenu(self.treeview_left_frame)

#########################################################################################################################
### Hier wird eine Instanz von der schrieftarten Class erstellt
#########################################################################################################################         
        pyglet_manager = PygletManager()

if __name__ == "__main__":
    root = tk.Tk()
    app = Objektkatalog(root)    
    root.mainloop()
