from os.path import join
from pathlib import Path
from subprocess import call
from threading import Thread


CUR_PATH = Path(__file__).resolve().parent
PYTHON = join(CUR_PATH, "venv/bin/python")


def run_server():
    call([PYTHON, f'{join(CUR_PATH, "manage.py")}', 'runserver'])


def run_messenger():
    msg = join(CUR_PATH, 'Telegram/bot_messenger.py')
    call([PYTHON, msg])


def run_tracker():
    track = join(CUR_PATH, 'Tracker/tracker.py')
    call([PYTHON, track])


if __name__ == '__main__':
    runserver = Thread(target=run_server)
    messenger = Thread(target=run_messenger)
    tracker = Thread(target=run_tracker)

    runserver.start()
    messenger.start()
    tracker.start()

    runserver.join()
    messenger.join()
    tracker.join()
