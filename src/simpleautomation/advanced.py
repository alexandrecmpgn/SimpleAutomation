import os
import pickle
from simpleautomation.vars import PATH_SESSIONS
from simpleautomation.strct import SESSION, ACTION_KBRD, ACTION_MOUSE

def main():
    print("Configuration avancée des sessions : ")
    sessions = os.listdir(PATH_SESSIONS)
    print("Liste des sessions :")
    for session in sessions:
        try: print("+ " + session.split(".pkl")[0])
        except: pass 
    _session = input("Entrez le nom de la session à modifier >>> ")
    if _session + ".pkl" not in sessions:
        raise FileNotFoundError("Le nom de la session est incorrecte !")
    else:
        print("Chargement de la session...")
        with open(PATH_SESSIONS + _session + ".pkl", 'rb') as f:
            project = pickle.load(f)
        f.close()
    randomize_sleep = input("Entrez la durée maximale aléatoire à ajouter aux délais (pour rendre le comportement plus humain), par exemple\n\t2.5 signifie que pour toute action, on rajoute un delta compris entre 0 et 2.5sec (aléatoire) au délai enregistré\n\tDurée actuelle : " + str(project.randomize_sleep) + " sec" + "\nVotre valeur (0 par défaut) >>> ")
    try:
        randomize_sleep = float(randomize_sleep.replace(',', '.'))
        project.randomize_sleep = randomize_sleep
    except:
        print("Valeur incorrecte ou vide laissé, le delta reste nul !")
        project.randomize_sleep = 0
    timer_start = input("Entrez le temps à attendre avant de démarrer l\'automatisation (par défaut 5 secondes) >>> ")
    try:
        project.timer_start = int(timer_start)
    except:
        project.timer_start = 5
    print("Mise à jour du projet...")
    with open(PATH_SESSIONS + _session + ".pkl", 'wb') as f:
        pickle.dump(project, f)
    f.close()
    print("Fait !")
if __name__ == '__main__': main()