from pydantic import BaseModel


class SchemaResult(BaseModel):
    test_id: int
    answer: str