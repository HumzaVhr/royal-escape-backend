from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "Royal Escape API"
    mongo_uri: str
    mongo_db: str = "royal--escape"


    jwt_secret: str
    jwt_algorithm: str = "HS256"
    jwt_exp_minutes: int = 60 * 24


    twilio_sid: str
    twilio_token: str
    twilio_from: str


    class Config:
        env_file = ".env"


settings = Settings()