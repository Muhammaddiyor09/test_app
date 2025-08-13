from typing import Optional

from pydantic import BaseModel


class SchemaTest(BaseModel):
    question: str
    options: list
    answer: str
    explanation: Optional[str]
    level: str
    lessone_id: int
