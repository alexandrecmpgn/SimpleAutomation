from simpleautomation.cfg import generate_cfg_file, update_session_from_cfg_file

def main():
    session_name = input("Nom de la session à modifier >>> ")
    generate_cfg_file(session_name)
    input("Modifiez le fichier généré puis appuyez sur Entrée !")
    update_session_from_cfg_file(session_name)

if __name__ == '__main__': main()