from simpleautomation.player import PLAYER

def main():
    player = PLAYER()
    player.run_session(input("Nom de la session à lire >>> "))

if __name__ == '__main__': main()