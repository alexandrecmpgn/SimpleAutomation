from simpleautomation.recorder import RECORDER
from simpleautomation.cfg import generate_cfg_file, load_session_from_json, convert_session_to_json
from simpleautomation.player import PLAYER

def main():
    # Création d'une nouvelle session
    name = input("Nom de la session à créer >>> ")
    r = RECORDER()
    r.record_session(name=name, overwrite_session=True)
    # Génération du fichier de configuration
    generate_cfg_file(session_name=name)
    # Lecture des actions
    p = PLAYER()
    p.run_session(name=name)
if __name__ == '__main__': load_session_from_json("libreoffice")