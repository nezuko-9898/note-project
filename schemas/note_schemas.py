from pydantic import BaseModel
from datetime import datetime

class NoteCreate(BaseModel):
    title:str 
    content : str


class NoteResponse(BaseModel):
    id : int
    title : str | None = None
    content :str
    created_at : datetime 

    model_config ={
        'from_attributes' : True
    }   