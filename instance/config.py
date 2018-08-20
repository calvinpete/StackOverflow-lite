class Config(object):
    """Parent configuration class that contains general settings
    as default settings for other classes to inherit.
    """
    DEBUG = False
    SECRET = 'SECRET'


class DevelopmentConfig(Config):
    """Configurations for Development."""
    DEBUG = True


class TestingConfig(Config):
    """Configurations for Testing."""
    TESTING = True
    DEBUG = True


class ProductionConfig(Config):
    """Configurations for Production."""
    DEBUG = False
    TESTING = False


# This dictionary is used to export the environments specified below.
app_config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig
}
