import pickle
import os
from time import sleep
from random import randint
import simpleautomation.log
from simpleautomation.tools import get_sessions

from simpleautomation.strct import ACTION_MOUSE, ACTION_KBRD, SESSION

import pynput.keyboard, pynput.mouse

from simpleautomation.vars import PATH_SESSIONS, STOP_KEY_FILENAME

import simpleautomation.cfg

class PLAYER(object):
    def __init__(self):
        self.actions = []
        self.randomize_sleep = 0
        self.keyboard = pynput.keyboard.Controller()
        self.mouse = pynput.mouse.Controller()
        self.name = ""
    def do_actions(self):
        for action in self.actions:
            simpleautomation.log.log(action)
            sleep(action.delay + (randint(0, int(self.randomize_sleep * 1000)) / 1000))
            if type(action) == ACTION_KBRD:
                if len(str(action.event)) > 1 and type(action.event) is str:
                    # Une variable
                    v = list(str(action.event))
                    for nn in range(0, len(v)):
                        self.keyboard.press(v[nn])
                        self.keyboard.release(v[nn])
                else:
                    if action.pressed: self.keyboard.press(action.event)
                    else: self.keyboard.release(action.event)
            else:
                if action.pressed == "True": action.pressed = True 
                if action.pressed == "False": action.pressed = False
                self.mouse.position = (int(action.x), int(action.y))
                if action.pressed: self.mouse.press(getattr(pynput.mouse.Button, action._type.split(".")[1]))
                else: self.mouse.release(getattr(pynput.mouse.Button, action._type.split(".")[1]))
    def run_session(self, name=None, timer_start=None, cfg_file=True):
        self.name = name
        if name is None: return 
        if cfg_file:
            simpleautomation.cfg.update_session_from_cfg_file(session_name=name)
            simpleautomation.cfg.load_session_from_json(session_name=name)
        sessions = get_sessions()
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
