from pydantic import BaseModel

class DatabaseConfig(BaseModel):
    host: str
    port: int
    database: str

