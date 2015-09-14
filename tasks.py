from invoke import task
import logging
import models
from base import db, app
import webservice
import os, sys
import signal

logging.basicConfig(format='[%(asctime)s] -- %(message)s',
    level = logging.INFO,
    datefmt='%m/%d/%Y %H:%M:%S')

@task
def db_drop():
    db.drop_all()
    logging.info('Drop DB')

@task(db_drop)
def db_init():
    db.create_all()
    logging.info('Init DB')

@task
def serve():
    app.run()

@task
def console():
    import code
    code.InteractiveConsole(locals=globals()).interact()

# deployment using gunicorn
@task
def gunicorn_start():
    if not os.path.exists("tmp"):
        os.mkdir("tmp", 0755)
    os.system("gunicorn webservice:app -c gunicorn.cfg")
    logging.info('gunicorn deamon start')

@task
def gunicorn_stop():
    try:
        gunicorn_signal(signal.SIGKILL)
        os.remove('tmp/pid')
        logging.info('gunicorn deamon stop')
    except (OSError, IOError):
        logging.warning('gunicorn doesn\'t seem to be running')
        sys.exit()

@task
def gunicorn_restart():
    try:
        gunicorn_signal(signal.SIGUSR2)
        logging.info('gunicorn deamon restart')
    except (OSError, IOError):
        logging.warning('gunicorn doesn\'t seem to be running')
        gunicorn_start()

# Increase gunicorn worker
@task
def gunicorn_incr():
    try:
        gunicorn_signal(signal.SIGTTIN)
        logging.info('increase gunicorn worker')
    except (OSError, IOError):
        logging.warning('gunicorn doesn\'t seem to be running')
        sys.exit()

# Decrease gunicorn worker
@task
def gunicorn_decr():
    try:
        gunicorn_signal(signal.SIGTTOU)
        logging.info('decrease gunicorn worker')
    except (OSError, IOError):
        logging.warning('gunicorn doesn\'t seem to be running')
        sys.exit()

def gunicorn_pid():
    with open("tmp/pid") as f:
        return int(f.read())

def gunicorn_signal(sig):
    os.kill(gunicorn_pid(), sig)

# shortcuts
@task(console)
def c():
    pass

@task(serve)
def s():
    pass
