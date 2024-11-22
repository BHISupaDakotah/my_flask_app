import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "postgresql://dakotahholmes:1234@localhost/my_flask_app")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
