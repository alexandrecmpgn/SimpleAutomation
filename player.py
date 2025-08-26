import pickle
import os
from time import sleep
from random import randint

from strct import ACTION_MOUSE, ACTION_KBRD, SESSION

import pynput.keyboard, pynput.mouse

from vars import PATH_SESSIONS, STOP_KEY_FILENAME

ACTIONS = []
RANDOMIZE_SLEEP = 0

def do_actions():
    global ACTIONS
    keyboard = pynput.keyboard.Controller()
    mouse = pynput.mouse.Controller()
    for action in ACTIONS:
        print(action)
        if type(action) == ACTION_KBRD:
            sleep(action.delay + (randint(0, int(RANDOMIZE_SLEEP * 1000)) / 1000))
            keyboard.press(action.event)
            keyboard.release(action.event)
        else:
            sleep(action.delay + (randint(0, int(RANDOMIZE_SLEEP * 1000)) / 1000))
            mouse.position = (action.x, action.y)
            if action.pressed: mouse.press(action._type)
            else: mouse.release(action._type)
def main():
    global ACTIONS, RANDOMIZE_SLEEP
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
                project = pickle.load(f)
            ACTIONS = project.actions
            if project.randomize_sleep != 0: print("Randomize_sleep détecté avec une valeur de " + str(project.randomize_sleep) + " sec !")
            RANDOMIZE_SLEEP = project.randomize_sleep
            f.close()
            print(str(len(ACTIONS)) + " actions chargées !")
        except:
            raise FileNotFoundError("Impossible de charger PATH_SESSIONS" + name + ".pkl !")
        for i in range(project.timer_start):
            if project.timer_start - i != 0 and project.timer_start - i != 1: print("Démarrage dans " + str(project.timer_start - i) + " secondes...")
            else: print("Démarrage dans " + str(project.timer_start - i) + " seconde...")
            sleep(1)
        do_actions()
if __name__ == '__main__': main()