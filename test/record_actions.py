import simpleautomation.recorder

def main():
    recorder = simpleautomation.recorder.RECORDER()
    recorder.record_session(name=input("Nom de la session à créer >>> "), overwrite_session=True)


if __name__ == '__main__': main()