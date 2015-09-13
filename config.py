import os

def get_db_uri(user='root', password='test', name='test_dev', addr='localhost'):
    return 'mysql://{}:{}@{}/{}?charset=utf8'.format(user, password, addr, name)

class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = 'this-really-needs-to-be-changed'
    SQLALCHEMY_DATABASE_URI = get_db_uri

class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = get_db_uri('root', 'test', 'test', 'localhost')

class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = get_db_uri('root', 'test', 'test_dev', 'localhost')

class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = get_db_uri(name = 'test_test')
