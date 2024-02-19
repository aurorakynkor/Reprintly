from pydantic import BaseModel
from typing import List

class CheckReprintModel(BaseModel):
    cards: List[str]
    sets: List[str]