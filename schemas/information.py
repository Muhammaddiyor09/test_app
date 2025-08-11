from pydantic import BaseModel


class SchemaInformation(BaseModel):
    description: str
    examole: str
    lessone_id: int
