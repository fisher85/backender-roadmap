class Configuration(object):
    DEBUG = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    #SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root@localhost/test1'
    MYSQL_DATABASE_USER = 'user'
    MYSQL_DATABASE_PASSWORD = 'password'
    MYSQL_DATABASE_DB = 'test1'
    MYSQL_DATABASE_HOST = 'localhost'
