from pydantic import BaseModel, StrictInt, Field

class DatabaseConfig(BaseModel):
    host: str
    port: StrictInt = Field(ge=1, le=65535)
    database: str

