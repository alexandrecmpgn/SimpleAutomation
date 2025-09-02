import os
from simpleautomation.vars import PATH_SESSIONS, STOP_KEY_FILENAME

def clean_all():
    first_choice = input("Voulez-vous supprimer toutes les données (sessions, stop_key, ...) ? o/n >>> ")
    if first_choice.lower() != 'o': exit()
    second_choice = input("Seconde confirmation o/n >>> ")
    if second_choice.lower() != 'o': exit()

    print("Nettoyage de la stop_key")
    try: os.remove(STOP_KEY_FILENAME)
    except:
        print("Fichier non présent !")
    print("Nettoyage des sessions...")
    sessions = os.listdir(PATH_SESSIONS)
    for session in sessions:
        print("Suppression de la session : " + session + "...")
        try: os.remove(PATH_SESSIONS + session)
        except: print("Erreur lors de la suppression !")
    print("Nettoyage terminé !")