from simpleautomation.vars import PATH_SESSIONS, PATH_JSON_CFG
from simpleautomation.strct import ACTION_MOUSE, ACTION_KBRD, SESSION
from simpleautomation.log import log
import pickle 
import json

def generate_config_file(session_name):
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
    project.timer_start = json_project["timer_start"]
    project.randomize_sleep = json_project["randomize_sleep"]
    with open(PATH_SESSIONS + session_name + ".pkl", 'wb') as f:
        pickle.dump(project, f)
    f.close()
    log("Fait.")
if __name__ == '__main__': update_session_from_cfg_file("demo")