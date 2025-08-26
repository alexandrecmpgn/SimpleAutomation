import pickle
import os
from time import sleep

from strct import ACTION_MOUSE, ACTION_KBRD

import pynput.keyboard, pynput.mouse

from vars import PATH_SESSIONS, STOP_KEY_FILENAME

ACTIONS = []

def do_actions():
    global ACTIONS
    keyboard = pynput.keyboard.Controller()
    mouse = pynput.mouse.Controller()
    for action in ACTIONS:
        print(action)
        if type(action) == ACTION_KBRD:
            sleep(action.delay)
            keyboard.press(action.event)
            keyboard.release(action.event)
        else:
            sleep(action.delay)
            mouse.position = (action.x, action.y)
            if action.pressed: mouse.press(action._type)
            else: mouse.release(action._type)
def main():
    global ACTIONS
    sessions = os.listdir(PATH_SESSIONS)
    if not len(sessions):
        print("Aucune session enregistrée ! Utilisez recorder.py pour en créer une !")
        exit()
    else:
        print("Liste des sessions disponibles : ")
        for session in sessions:
            try: print("+ " + session.split(".pkl")[0])
            except: pass 
        name = input("Entrez le nom de la session à charger >>> ")
        try:
            print("Chargement des actions...")
            with open(PATH_SESSIONS + name + ".pkl", 'rb') as f:
                ACTIONS = pickle.load(f)
            f.close()
            print(str(len(ACTIONS)) + " actions chargées !")
        except:
            raise FileNotFoundError("Impossible de charger PATH_SESSIONS" + name + ".pkl !")
        for i in range(5):
            if 5 - i != 0 and 5 - i != 1: print("Démarrage dans " + str(5 - i) + " secondes...")
            else: print("Démarrage dans " + str(5 - i) + " seconde...")
            sleep(1)
        do_actions()
if __name__ == '__main__': main()