from platformdirs import user_documents_path

PATH_SESSIONS = str(user_documents_path()) + "/SimpleAutomationSessions/"
PATH_JSON_CFG = str(user_documents_path()) + "/.SimpleAutomationData/"
STOP_KEY_FILENAME = PATH_JSON_CFG + "/stop_key.pkl"
LOG = True
LENGTH_ACTION_KBRD = 3
LENGTH_ACTION_MOUSE = 5

DELIMITER_VARS = "$=$"
VARS_FILE_PATH = PATH_JSON_CFG + "vars.txt"

import os
import simpleautomation.log

def load_all_vars():
    # A retravailler plus propre
    simpleautomation.log.log("Chargement des variables...")
    file = open(VARS_FILE_PATH, "r")
    l = file.read()
    file.close()
    l = l.split(DELIMITER_VARS)
    __vars = []
    __content = []
    for i in range(0, len(l)):
        if not (i % 2) and l[i] != '' and l[i] != '\n': __vars.append(l[i].replace('\n', ''))
        else: 
            if l[i] != '\n' and l[i] != '': __content.append(l[i])
    if len(__vars) != len(__content):
        raise IndexError("Taille de __vars et __content différentes : " + str((__vars, __content)))
    return ((__vars, __content))