import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///{0}/clockit.db'.format(basedir)
    SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
