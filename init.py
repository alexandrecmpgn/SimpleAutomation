from vars import PATH_SESSIONS
import os

def main():
    print("Création du répertoire sessions/ ...")
    try: os.mkdir(PATH_SESSIONS)
    except FileExistsError: print("Répertoire déjà créé !")
    except: print("Erreur lors de la création :/")
if __name__ == '__main__': main()