import os
from vars import PATH_SESSIONS, STOP_KEY_FILENAME
import save_stop_key

if not os.path.exists(PATH_SESSIONS): os.makedirs(PATH_SESSIONS)
else: pass

try:
    file = open(STOP_KEY_FILENAME, "r")
    file.close()
except: save_stop_key.main()