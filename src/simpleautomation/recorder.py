from pynput import mouse, keyboard
from simpleautomation.strct import ACTION_KBRD, ACTION_MOUSE, SESSION
from time import time
import pickle
import os
from simpleautomation.vars import PATH_SESSIONS, STOP_KEY_FILENAME
import simpleautomation.log
from simpleautomation.tools import get_sessions
import simpleautomation.cfg

class RECORDER(object):
    def __init__(self):
        self.actions = []
        self.START_TIMESTAMP = None
        self.mouse_listener = None 
        self.keyboard_listener = None
        self.stop_key = None
        self.name = ""
    def save_data(self): 
        project = SESSION()
        project.actions = self.actions
        simpleautomation.log.log("Sauvegarde des actions dans le fichier " + str(self.name) + ".pkl ...")
        with open(PATH_SESSIONS + str(self.name) + ".pkl", "wb") as f:
            pickle.dump(project, f)
        f.close()
    def on_click(self, x, y, button, pressed):
        _timestamp = time()
        if pressed:
            simpleautomation.log.log("Enregistrement d\'un click " + str(button) + " en " + str((x, y)) + " avec un délai de " + str(_timestamp - self.START_TIMESTAMP) + " secondes...")
        else:
            simpleautomation.log.log("Enregistrement d\'un relâchement de click " + str(button) + " " + str((x, y)) + " avec un délai de " + str(_timestamp - self.START_TIMESTAMP) + " secondes...")
        new_event = ACTION_MOUSE(x, y, button, pressed, _timestamp - self.START_TIMESTAMP)
        self.actions.append(new_event)
        self.START_TIMESTAMP = _timestamp
    def stop_listeners(self):
        simpleautomation.log.log("Arrêt des listeners...")
        self.save_data()
        self.mouse_listener.stop()
        self.keyboard_listener.stop()
        self.generate_add_files()
    def on_press(self, key):
        _timestamp = time()
        try:
            if key == self.stop_key: self.stop_listeners()
            else:
                simpleautomation.log.log("Enregistrement d\'une touche " + str(key.char) + " avec un délai de " + str(_timestamp - self.START_TIMESTAMP) + " secondes...")
                new_event = ACTION_KBRD(key, _timestamp - self.START_TIMESTAMP, 1)
                self.actions.append(new_event)
        except AttributeError:
            if key == self.stop_key: self.stop_listeners()
            else:
                simpleautomation.log.log("Enregistrement d\' une touche spéciale " + str(key) + " avec un délai de " + str(_timestamp - self.START_TIMESTAMP) + " secondes...")
                new_event = ACTION_KBRD(key, _timestamp - self.START_TIMESTAMP, 1)
                self.actions.append(new_event)
        self.START_TIMESTAMP = _timestamp
    def on_release(self, key):
        _timestamp = time()
        try:
            simpleautomation.log.log("Enregistrement d\'une touche " + str(key.char) + " avec un délai de " + str(_timestamp - self.START_TIMESTAMP) + " secondes...")
            new_event = ACTION_KBRD(key, _timestamp - self.START_TIMESTAMP, 0)
            self.actions.append(new_event)
        except:
            simpleautomation.log.log("Enregistrement d\' une touche spéciale " + str(key) + " avec un délai de " + str(_timestamp - self.START_TIMESTAMP) + " secondes...")
            new_event = ACTION_KBRD(key, _timestamp - self.START_TIMESTAMP, 0)
            self.actions.append(new_event)
        self.START_TIMESTAMP = _timestamp

    def record_session(self, name=None, overwrite_session=False):
        self.name = name 
        self.overwrite_session = overwrite_session
        simpleautomation.log.log("Chargement de la touche d\'arrêt...")
        try:
            with open(STOP_KEY_FILENAME, 'rb') as f:
                self.stop_key = pickle.load(f)
            f.close()
            simpleautomation.log.log("Touche d\'arrêt : " + str(self.stop_key) + " !")
        except:
            raise FileNotFoundError("Impossible de charger le fichier stop_key.pkl ! Avez-vous enregistrer une touche avec save_stop_key.py ?")
        sessions = get_sessions()
        simpleautomation.log.log("Liste des sessions disponibles : ")
        for session in sessions:
            try: simpleautomation.log.log("+ " + session.split(".pkl")[0])
            except: pass 
        if self.name is None: self.name = input("Entrez le nom de la session >>> ")
        if self.name + ".pkl" in sessions and not self.overwrite_session:
            if input(self.name + " est déjà une session enregistrée, l\'écraser ? o/n >>> ").lower() != 'o': exit()
            else: pass

        self.mouse_listener = mouse.Listener(on_click=self.on_click)
        self.keyboard_listener = keyboard.Listener(on_press=self.on_press, on_release=self.on_release)
        
        self.mouse_listener.start()
        self.keyboard_listener.start()

        simpleautomation.log.log("Démarrage de l\'enregistrement des actions...")
        self.START_TIMESTAMP = time()

        self.mouse_listener.join()
        self.keyboard_listener.join()
    def generate_add_files(self):
        if self.name != "":
            simpleautomation.cfg.generate_cfg_file(session_name=self.name)
            simpleautomation.cfg.convert_session_to_json(session_name=self.name)