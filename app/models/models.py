
from pydantic import BaseModel


class InputModel(BaseModel):
    department: str
    surface: int
    max_rent: int


class OutputModel(BaseModel):
    city: str
    avg_rent: int
    postal_code: list[str]
    score: float
    population: int

