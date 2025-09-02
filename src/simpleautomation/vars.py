from platformdirs import user_documents_path

PATH_SESSIONS = str(user_documents_path()) + "/SimpleAutomationSessions/"
STOP_KEY_FILENAME = str(user_documents_path()) + "/.stop_key.pkl"
LOG = True