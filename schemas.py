from datetime import date
from optparse import Option
from typing import Optional
from pydantic import BaseModel

class Tasks(BaseModel):

    id : Optional[int]
    title : str
    description : str
    isComplete: bool
    deadline: date

    class Config:
        orm_mode = True