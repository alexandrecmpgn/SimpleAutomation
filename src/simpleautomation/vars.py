from platformdirs import user_documents_path

PATH_SESSIONS = str(user_documents_path()) + "/SimpleAutomationSessions/"
PATH_JSON_CFG = str(user_documents_path()) + "/.SimpleAutomationData/"
STOP_KEY_FILENAME = PATH_JSON_CFG + "/stop_key.pkl"
LOG = True
LENGTH_ACTION_KBRD = 2
LENGTH_ACTION_MOUSE = 5