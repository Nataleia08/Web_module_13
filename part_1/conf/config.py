from pydantic import BaseSettings


class Settings(BaseSettings):
    sqlalchemy_database_url: str = "postgresql+psycopg2://USER:PASSWORD@localhost:PORT/DB"
    secret_key: str = "secret"
    algorithm: str = "H256"
    mail_username: str = "example@gmail.com"
    mail_password: str = "password"
    mail_from: str = ""
    mail_port: int = 465
    mail_server: str = ""
    redis_host: str = 'localhost'
    redis_port: int = 6379
    cloudinary_name: str = "name"
    cloudinary_api_key: str = "00000000000000"
    cloudinary_api_secret: str = "api_secret"

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()