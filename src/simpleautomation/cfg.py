from simpleautomation.vars import PATH_SESSIONS, PATH_JSON_CFG, LENGTH_ACTION_KBRD, LENGTH_ACTION_MOUSE
from simpleautomation.strct import ACTION_MOUSE, ACTION_KBRD, SESSION
from simpleautomation.log import log
import pickle 
import json

def generate_cfg_file(session_name):
    log("Chargement de la session...")
    try:
        with open(PATH_SESSIONS + session_name + ".pkl", 'rb') as f:
            project = pickle.load(f)
        f.close()
    except FileNotFoundError:
        log("Impossible de charger le fichier " + PATH_SESSIONS + session_name + ".pkl !")
        return
    log("Génération du fichier de configuration...")
    with open(PATH_JSON_CFG + session_name + ".json", "w", encoding="utf-8") as f:
        json.dump(project.to_dict(), f, ensure_ascii=False, indent=4)
    f.close()
    log("Le fichier se trouve à ce chemin : " + PATH_JSON_CFG + session_name + ".json ...")
def update_session_from_cfg_file(session_name):
    log("Chargement du fichier de configuration...")
    with open(PATH_JSON_CFG + session_name + ".json", "r", encoding="utf-8") as f:
        json_project = json.load(f)
    f.close()
    with open(PATH_SESSIONS + session_name + ".pkl", 'rb') as f:
        project = pickle.load(f)
    f.close()
    log("Mise à jour de la session...")
    project.from_dict(json_project)
    with open(PATH_SESSIONS + session_name + ".pkl", 'wb') as f:
        pickle.dump(project, f)
    f.close()
    log("Fait.")
def convert_session_to_json(session_name):
    log("Chargement de la session...")
    try:
        with open(PATH_SESSIONS + session_name + ".pkl", 'rb') as f:
            project = pickle.load(f)
        f.close()
    except FileNotFoundError:
        log("Impossible de charger le fichier " + PATH_SESSIONS + session_name + ".pkl !")
        return
    with open(PATH_JSON_CFG + session_name + "_actions.json", "w", encoding="utf-8") as f:
        for action in project.actions: json.dump(action.to_dict(), f, ensure_ascii=False, indent=4)
    f.close()
def load_session_from_json(session_name):
    log("Chargement de la session JSON...")
    try:
        with open(PATH_JSON_CFG + session_name + "_actions.json", "r", encoding="utf-8") as f:
            data = f.read()
        f.close()
    except FileNotFoundError:
        log("Impossible de charger le fichier " + PATH_JSON_CFG + session_name + "_actions.json !")
        return 
    objects_str = data.replace('}{', '}|{').split('|')
    objects = []
    for obj_str in objects_str:
        try:
            obj = json.loads(obj_str)
            objects.append(obj)
        except json.JSONDecodeError as e:
            log(f"Erreur de décodage JSON: {e}")
            return
    session = SESSION()
    for obj in objects:
        if len(obj) == LENGTH_ACTION_KBRD:
            new_action = ACTION_KBRD(obj["event"], obj["delay"])
        elif len(obj) == LENGTH_ACTION_MOUSE:
            new_action = ACTION_MOUSE(obj["x"], obj["y"], obj["_type"], obj["pressed"], obj["delay"])
        else:
            log("Erreur de length pour cette action => " + str(obj))
            return 
        session.actions.append(new_action)
    log("Sauvegarde des actions dans le fichier " + str(session_name) + ".pkl ...")
    with open(PATH_SESSIONS + str(session_name) + ".pkl", "wb") as f:
            pickle.dump(session, f)
    f.close()