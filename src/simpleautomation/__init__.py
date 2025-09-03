import os
from simpleautomation.vars import PATH_SESSIONS, STOP_KEY_FILENAME, PATH_JSON_CFG
import simpleautomation.save_stop_key

if not os.path.exists(PATH_SESSIONS): os.makedirs(PATH_SESSIONS)
else: pass
if not os.path.exists(PATH_JSON_CFG): os.makedirs(PATH_JSON_CFG)
else: pass

try:
    file = open(STOP_KEY_FILENAME, "r")
    file.close()
except: simpleautomation.save_stop_key.main()