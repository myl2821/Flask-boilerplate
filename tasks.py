from invoke import task
import logging
import models
from base import db, app
import webservice

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

# shortcuts
@task(console)
def c():
    pass

@task(serve)
def s():
    pass
