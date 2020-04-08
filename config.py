import os


class Config:
    DEBUG = False
    TESTING = False

    SECRET_KEY = os.environ.get('SECRET_KEY') or 'SECRET_KEY'
    NSSL_SERVER_URL = os.environ.get('NSSL_SERVER_URL')


class ProductionConfig(Config):
    pass


class DevelopConfig(Config):
    DEBUG = True


class TestConfig(Config):
    TESTING = True
