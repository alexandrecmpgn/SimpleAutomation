import os
from simpleautomation.vars import PATH_SESSIONS

def get_sessions(): return os.listdir(PATH_SESSIONS)