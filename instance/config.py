class Config(object):
    """Parent configuration class that contains general settings
    as default settings for other classes to inherit.
    """
    DEBUG = False


class DevelopmentConfig(Config):
    """Configuration settings for Development."""
    DEBUG = True


class TestingConfig(Config):
    """Configuration settings for Testing."""
    TESTING = True
    DEBUG = True


class ProductionConfig(Config):
    """Configuration settings for Production."""
    DEBUG = False
    TESTING = False

