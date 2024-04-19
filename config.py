import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY= "hard to guess "
    MAIL_USERNAME = "jceanciens@gmail.com"
    MAIL_PASSWORD = "sinf zkoq kmva dnxy"
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_SERVER = "smtp.googlemail.com"
    APP_MAIL_SENDER = "<jceanciens@gmail.com>"
    APP_MAIL_SUBJECT_PREFIX = "[ajce]"
    SQLALCHEMY_TRACK_MODIFICATION = False

    @staticmethod
    def init_app(app):
        pass

class TestingConfig(Config):
    TESTING=True
    SQLALCHEMY_DATABASE_URI = "sqlite://"

class DevelopmentConfig(Config):
    DEBUG=True
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir, "data-dev.sqlite3")


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir, "data.sqlite3")


config= {
    'testing' : TestingConfig,
    'development' : DevelopmentConfig,
    'production'  : ProductionConfig,
    'default': DevelopmentConfig
}