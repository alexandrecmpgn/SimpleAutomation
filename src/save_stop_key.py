from pynput import keyboard
import pickle

from vars import STOP_KEY_FILENAME

import log

keyboard_listener = None

def on_press(key):
    global keyboard_listener
    log.log("Nouvelle touche d\'arrêt : " + str(key) + " !")
    with open(STOP_KEY_FILENAME, 'wb') as f:
        pickle.dump(key, f)
    f.close()
    keyboard_listener.stop()
    

def main():
    global keyboard_listener
    keyboard_listener = keyboard.Listener(on_press=on_press)
    
    keyboard_listener.start()
    
    log.log("Pressez la touche qui servira à arrêter l\'enregistrement...")
    keyboard_listener.join()



if __name__ == '__main__': main()