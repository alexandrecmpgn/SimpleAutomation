import simpleautomation.recorder

def main():
    recorder = simpleautomation.recorder.RECORDER()
    recorder.record_session(name="demo", overwrite_session=True)


if __name__ == '__main__': main()