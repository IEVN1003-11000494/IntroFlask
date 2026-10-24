class DevelopmentConfig():
    DEBUG = True
    MYSQL_HOST = '127.0.0.1'
    MYSQL_USER = 'carlos'
    MYSQL_PASSWORD = 'root'
    MYSQL_DB = 'api_utl'
    MYSQL_PORT = 8889
    MYSQL_CURSORCLASS='Cursor'
config = {
    'development': DevelopmentConfig
}