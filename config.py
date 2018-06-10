import os

basedir = os.path.abspath(os.path.dirname(__file__))


class DbConfig:
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') \
                              or 'sqlite:///{}'.format(os.path.join(basedir, 'db/data.db'))
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    def __init__(self, local_database_name=None):
        if local_database_name:
            DbConfig.SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') \
                              or 'sqlite:///{}'.format(os.path.join(basedir, 'db/{}'.format(local_database_name)))

