class Config(object):
    """
    Common configurations
    """

    # Put any configurations here that are common across all environments
    SECRET_KEY = 'p9Bv<3Eid9%$i01'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = True


class DevelopmentConfig(Config):
    """
    Development configurations
    """

    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:@localhost:3306/python-dream-team?charset=utf8'
    # SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://python-dream-team:python-dream-team@localhost:3306/python-dream-team?charset=utf8'
    SQLALCHEMY_ECHO = True


class ProductionConfig(Config):
    """
    Production configurations
    """

    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://python-dream-team:python-dream-team@localhost:3306/python-dream-team?charset=utf8'
    DEBUG = False


class TestingConfig(Config):
    """
    Testing configurations
    """

    TESTING = True


app_config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig
}
