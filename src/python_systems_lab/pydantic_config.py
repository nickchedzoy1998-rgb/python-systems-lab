from pydantic import BaseModel, StrictInt, Field

class DatabaseConfig(BaseModel):
    host: str = Field(min_length=1, pattern=r'\S')
    port: StrictInt = Field(ge=1, le=65535)
    database: str = Field(min_length=1, pattern=r'\S')