from pynput import mouse, keyboard
from strct import ACTION_KBRD, ACTION_MOUSE, SESSION
from time import time
import pickle
import os
from vars import PATH_SESSIONS, STOP_KEY_FILENAME

class RECORDER(object):
    def __init__(self, name=None, overwrite_session=False):
        self.ACTIONS = []
        self.START_TIMESTAMP = None
        self.mouse_listener = None 
        self.keyboard_listener = None
        self.STOP_KEY = None
        self.NAME = name
        self.overwrite_session = overwrite_session

    def save_data(self): 
        project = SESSION()
        project.actions = self.ACTIONS
        print("Sauvegarde des actions dans le fichier " + str(self.NAME) + ".pkl ...")
        with open(PATH_SESSIONS + str(self.NAME) + ".pkl", "wb") as f:
            pickle.dump(project, f)
        f.close()
    def on_click(self, x, y, button, pressed):
        _timestamp = time()
        if pressed:
            print("Enregistrement d\'un click " + str(button) + " en " + str((x, y)) + " avec un délai de " + str(_timestamp - self.START_TIMESTAMP) + " secondes...")
        else:
            print("Enregistrement d\'un relâchement de click " + str(button) + " " + str((x, y)) + " avec un délai de " + str(_timestamp - self.START_TIMESTAMP) + " secondes...")
        new_event = ACTION_MOUSE(x, y, button, pressed, _timestamp - self.START_TIMESTAMP)
        self.ACTIONS.append(new_event)
        self.START_TIMESTAMP = _timestamp

    def on_press(self, key):
        _timestamp = time()
        try:
            if key == self.STOP_KEY: 
                print("Arrêt des listeners...")
                self.save_data()
                self.mouse_listener.stop()
                self.keyboard_listener.stop()
            else:
                print("Enregistrement d\'une touche " + str(key.char) + " avec un délai de " + str(_timestamp - self.START_TIMESTAMP) + " secondes...")
                new_event = ACTION_KBRD(key, _timestamp - self.START_TIMESTAMP)
                self.ACTIONS.append(new_event)
        except AttributeError:
            if key == self.STOP_KEY: 
                print("Arrêt des listeners...")
                self.save_data()
                self.mouse_listener.stop()
                self.keyboard_listener.stop()
            else:
                print("Enregistrement d\' une touche spéciale " + str(key) + " avec un délai de " + str(_timestamp - self.START_TIMESTAMP) + " secondes...")
                new_event = ACTION_KBRD(key, _timestamp - self.START_TIMESTAMP)
                self.ACTIONS.append(new_event)
        self.START_TIMESTAMP = _timestamp

    def main(self):
        print("Chargement de la touche d\'arrêt...")
        try:
            with open(STOP_KEY_FILENAME, 'rb') as f:
                self.STOP_KEY = pickle.load(f)
            f.close()
            print("Touche d\'arrêt : " + str(self.STOP_KEY) + " !")
        except:
            raise FileNotFoundError("Impossible de charger le fichier stop_key.pkl ! Avez-vous enregistrer une touche avec save_stop_key.py ?")
        sessions = os.listdir(PATH_SESSIONS)
        print("Liste des sessions disponibles : ")
        for session in sessions:
            try: print("+ " + session.split(".pkl")[0])
            except: pass 
        if self.NAME is None: self.NAME = input("Entrez le nom de la session >>> ")
        if self.NAME + ".pkl" in sessions and not self.overwrite_session:
            if input(self.NAME + " est déjà une session enregistrée, l\'écraser ? o/n >>> ").lower() != 'o': exit()
            else: pass

        self.mouse_listener = mouse.Listener(on_click=self.on_click)
        self.keyboard_listener = keyboard.Listener(on_press=self.on_press)
        
        self.mouse_listener.start()
        self.keyboard_listener.start()

        print("Démarrage de l\'enregistrement des actions...")
        self.START_TIMESTAMP = time()

        self.mouse_listener.join()
        self.keyboard_listener.join()


def main():
    recorder = RECORDER(name="mail", overwrite_session=True)
    recorder.main()

if __name__ == '__main__': main()