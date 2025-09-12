import os
from simpleautomation.vars import PATH_SESSIONS
import socket


def get_sessions(): return os.listdir(PATH_SESSIONS)

def check_internet_connection(host="8.8.8.8", port=53, timeout=3):
    try:
        socket.setdefaulttimeout(timeout)
        socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host, port))
        return True
    except socket.error:
        return False
if __name__ == '__main__': print(check_internet_connection())