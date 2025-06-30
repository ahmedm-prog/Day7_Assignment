import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'a_default_secret_key'
    SQLALCHEMY_DATABASE_URI = (
        os.environ.get('DATABASE_URL')
        or 'mysql+pymysql://root:admin@localhost:3306/devopsbootcamp'
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False