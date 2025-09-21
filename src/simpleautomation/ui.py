import tkinter as tk
from tkinter import ttk
import simpleautomation.tools
import simpleautomation.save_stop_key
from time import sleep

class SimpleAutomationGUI(object):
    def __init__(self):
        self.width = 1000
        self.height = 1000
        self.root = tk.Tk()
        self.root.title("Simple Automation GUI")
        self.screen_width = self.root.winfo_screenwidth()
        self.screen_height = self.root.winfo_screenheight()
        self.x_pos = (self.screen_width // 2) - (self.width // 2)
        self.y_pos = (self.screen_height // 2) - (self.height // 2)
        self.root.geometry(f"{self.width}x{self.height}+{self.x_pos}+{self.y_pos}")
        self.recording_key = False
        self.display_frame()
    def display_frame(self):
        self.clear()
        self.sessions = simpleautomation.tools.get_sessions()
        frame = tk.Frame(self.root)
        frame.pack(fill='x', padx=20, pady=20)
        label = tk.Label(frame, text="Liste des sessions :", font=("Arial", 14))
        label.pack(fill='x')
        combo = ttk.Combobox(frame, values=self.sessions, state="readonly", font=("Arial", 12))
        combo.current(0)  # Sélection du premier élément par défaut
        combo.pack(fill='x', pady=20)  # Remplit horizontalement le frame (donc aligné à gauche)
        if not self.recording_key: label = tk.Label(frame, text="Touche d\'arrêt d\'enregistrement des actions : " + simpleautomation.save_stop_key.get_str_stop_key(), font=("Arial", 14))
        else: label = tk.Label(frame, text="Appuyez sur la nouvelle touche d\'arrêt...", font=("Arial", 14))
        label.pack(fill='x')
        style = ttk.Style()
        style.configure("Custom.TButton", font=("Arial", 12))
        button = ttk.Button(self.root, text="Mettre à jour la touche", style="Custom.TButton", command=self.change_stop_key)
        button.pack()
    def change_stop_key(self):
        self.recording_key = True 
        self.display_frame()
        simpleautomation.save_stop_key.main()
        self.recording_key = False 
        self.display_frame()
    def clear(self):
        for widget in self.root.winfo_children(): widget.destroy()
    def run(self): self.root.mainloop()
s = SimpleAutomationGUI()
s.run()