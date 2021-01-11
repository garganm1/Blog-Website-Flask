import os

class Config():
    SECRET_KEY = '8488ee65ac9581927ecb8b2e021cc63f'
    SQLALCHEMY_DATABASE_URI = "sqlite:///blogsite.db"
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('USER_EMAIL')
    MAIL_PASSWORD = os.environ.get('USER_PASS')
