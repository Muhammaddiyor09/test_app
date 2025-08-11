from pydantic import BaseModel


class SchemaUser(BaseModel):
    fullname: str
    username: str
    password: str
