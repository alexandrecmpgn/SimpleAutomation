from pynput import mouse, keyboard
from strct import ACTION_KBRD, ACTION_MOUSE
from time import time
import pickle
import os
from vars import PATH_SESSIONS, STOP_KEY_FILENAME

ACTIONS = []

START_TIMESTAMP = None

mouse_listener = None 
keyboard_listener = None

STOP_KEY = None
NAME = None

def save_data():
    global ACTIONS, NAME 
    print("Sauvegarde des actions dans le fichier " + str(NAME) + ".pkl ...")
    with open(PATH_SESSIONS + str(NAME) + ".pkl", "wb") as f:
        pickle.dump(ACTIONS, f)
    f.close()

def on_click(x, y, button, pressed):
    global START_TIMESTAMP
    _timestamp = time()
    if pressed:
        print("Enregistrement d\'un click " + str(button) + " en " + str((x, y)) + " avec un délai de " + str(_timestamp - START_TIMESTAMP) + " secondes...")
    else:
        print("Enregistrement d\'un relâchement de click " + str(button) + " " + str((x, y)) + " avec un délai de " + str(_timestamp - START_TIMESTAMP) + " secondes...")
    new_event = ACTION_MOUSE(x, y, button, pressed, _timestamp - START_TIMESTAMP)
    ACTIONS.append(new_event)
    START_TIMESTAMP = _timestamp

def on_press(key):
    global START_TIMESTAMP, mouse_listener, keyboard_listener, ACTIONS
    _timestamp = time()
    try:
        if key == STOP_KEY: 
            print("Arrêt des listeners...")
            save_data()
            mouse_listener.stop()
            keyboard_listener.stop()
        else:
            print("Enregistrement d\'une touche " + str(key.char) + " avec un délai de " + str(_timestamp - START_TIMESTAMP) + " secondes...")
            new_event = ACTION_KBRD(key, _timestamp - START_TIMESTAMP)
            ACTIONS.append(new_event)
    except AttributeError:
        if key == STOP_KEY: 
            print("Arrêt des listeners...")
            save_data()
            mouse_listener.stop()
            keyboard_listener.stop()
        else:
            print("Enregistrement d\' une touche spéciale " + str(key) + " avec un délai de " + str(_timestamp - START_TIMESTAMP) + " secondes...")
            new_event = ACTION_KBRD(key, _timestamp - START_TIMESTAMP)
            ACTIONS.append(new_event)
    START_TIMESTAMP = _timestamp

def main():
    global START_TIMESTAMP, mouse_listener, keyboard_listener, STOP_KEY, NAME
    print("Chargement de la touche d\'arrêt...")
    try:
        with open(STOP_KEY_FILENAME, 'rb') as f:
            STOP_KEY = pickle.load(f)
        f.close()
        print("Touche d\'arrêt : " + str(STOP_KEY) + " !")
    except:
        raise FileNotFoundError("Impossible de charger le fichier stop_key.pkl ! Avez-vous enregistrer une touche avec save_stop_key.py ?")
    sessions = os.listdir(PATH_SESSIONS)
    print("Liste des sessions disponibles : ")
    for session in sessions:
        try: print("+ " + session.split(".pkl")[0])
        except: pass 
    NAME = input("Entrez le nom de la session >>> ")
    if NAME + ".pkl" in sessions:
        if input(NAME + " est déjà une session enregistrée, l\'écraser ? o/n >>> ").lower() != 'o': exit()
        else: pass

    mouse_listener = mouse.Listener(on_click=on_click)
    keyboard_listener = keyboard.Listener(on_press=on_press)
    
    mouse_listener.start()
    keyboard_listener.start()

    print("Démarrage de l\'enregistrement des actions...")
    START_TIMESTAMP = time()

    mouse_listener.join()
    keyboard_listener.join()



if __name__ == '__main__': main()