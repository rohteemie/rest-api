import os


class Config(object):
    DEBUG = False
    CSRF_ENABLED = True
    SECRET_KEY = 'secret-key'
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class ProductionConfig(Config):
    DEBUG = False
    TESTING = False


app_config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}
