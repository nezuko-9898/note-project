from fastapi import HTTPException , Depends, APIRouter
from sqlalchemy.orm  import  Session
from app.db.session import get_db
from app.schemas.note_schemas import NoteCreate,NoteResponse
from app.services.note_service import create_note, get_all_notes,get_note_by_id
from app.ai_services.agent import ask_note_agent
from app.ai_services.tools import note_as_text


router = APIRouter(
    prefix="/notes",
    tags=["Notes"]
)

#Add note
@router.post("/add",response_model=NoteResponse)
def add_note(
    payload: NoteCreate,
    db:Session = Depends(get_db)
):
   return create_note( db, payload.content,payload.title)

# List all note
@router.get("/", response_model= list[NoteResponse])
def list_note(db:Session = Depends(get_db)):
   return get_all_notes(db)

#Get Single 
@router.get("/{note_id}",response_model=NoteResponse)
def get_single_note(
    note_id:int,
    db:Session=Depends(get_db)
):
    note= get_note_by_id(db,note_id)

    if not note:
        raise HTTPException(status_code=404,detail="Note Not Found")
    return note




@router.post("/ask")
def ask_ai(
      question : str,
      db : Session = Depends(get_db)

):
     note_text = note_as_text(db)
     answer = ask_note_agent(question,note_text)
     return {"Answer":answer}