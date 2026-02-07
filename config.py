import os

class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY", "dev-secret-key-change-me")
    SQLALCHEMY_DATABASE_URI = (os.environ.get("DATABASE_URL")
                               or "oracle+cx_oracle://c##SALE:123@localhost:1521/?service_name=ORCL")
    SQLALCHEMY_TRACK_MODIFICATIONS = False