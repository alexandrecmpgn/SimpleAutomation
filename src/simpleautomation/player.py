import pickle
import os
from time import sleep
from random import randint
import simpleautomation.log

from simpleautomation.strct import ACTION_MOUSE, ACTION_KBRD, SESSION

import pynput.keyboard, pynput.mouse

from simpleautomation.vars import PATH_SESSIONS, STOP_KEY_FILENAME

class PLAYER(object):
    def __init__(self):
        self.actions = []
        self.randomize_sleep = 0
        self.keyboard = pynput.keyboard.Controller()
        self.mouse = pynput.mouse.Controller()
    def do_actions(self):
        for action in self.actions:
            simpleautomation.log.log(action)
            sleep(action.delay + (randint(0, int(self.randomize_sleep * 1000)) / 1000))
            if type(action) == ACTION_KBRD:
                self.keyboard.press(action.event)
                self.keyboard.release(action.event)
            else:
                self.mouse.position = (action.x, action.y)
                if action.pressed: self.mouse.press(action._type)
                else: self.mouse.release(action._type)
    def run_session(self, name=None, timer_start=None):
        sessions = os.listdir(PATH_SESSIONS)
        if not len(sessions):
            simpleautomation.log.log("Aucune session enregistrée ! Utilisez recorder.py pour en créer une !")
            exit()
        else:
            simpleautomation.log.log("Liste des sessions disponibles : ")
            for session in sessions:
                try: simpleautomation.log.log("+ " + session.split(".pkl")[0])
                except: pass 
            if name is None: name = input("Entrez le nom de la session à charger >>> ")
            try:
                simpleautomation.log.log("Chargement des actions...")
                with open(PATH_SESSIONS + name + ".pkl", 'rb') as f:
                    project = pickle.load(f)
                self.actions = project.actions
                if timer_start is not None and type(timer_start) == int: 
                    simpleautomation.log.log("La session sera effectuée après une attente de " + str(timer_start) + " sec !")
                    project.timer_start = timer_start
                if project.randomize_sleep != 0: simpleautomation.log.log("randomize_sleep détecté avec une valeur de " + str(project.randomize_sleep) + " sec !")
                self.randomize_sleep = project.randomize_sleep
                f.close()
                simpleautomation.log.log(str(len(self.actions)) + " actions chargées !")
            except:
                raise FileNotFoundError("Impossible de charger " + PATH_SESSIONS + name + ".pkl !")
            for i in range(project.timer_start):
                if project.timer_start - i != 0 and project.timer_start - i != 1: simpleautomation.log.log("Démarrage dans " + str(project.timer_start - i) + " secondes...")
                else: simpleautomation.log.log("Démarrage dans " + str(project.timer_start - i) + " seconde...")
                sleep(1)
            self.do_actions()
