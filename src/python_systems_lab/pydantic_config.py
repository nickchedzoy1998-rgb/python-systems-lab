from pydantic import BaseModel
from pydantic import StrictInt

class DatabaseConfig(BaseModel):
    host: str
    port: StrictInt
    database: str

