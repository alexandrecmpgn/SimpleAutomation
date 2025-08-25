from pynput import keyboard
import pickle

keyboard_listener = None

def on_press(key):
    global keyboard_listener
    print("Nouvelle touche d\'arrêt : " + str(key) + " !")
    with open('stop_key.pkl', 'wb') as f:
        pickle.dump(key, f)
    f.close()
    keyboard_listener.stop()
    

def main():
    global keyboard_listener
    keyboard_listener = keyboard.Listener(on_press=on_press)
    
    keyboard_listener.start()
    
    print("Pressez la touche qui servira à arrêter l\'enregistrement...")
    keyboard_listener.join()



if __name__ == '__main__': main()