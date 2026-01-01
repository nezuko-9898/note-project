from sqlalchemy import select
from sqlalchemy.orm import Session
from app.models.note import Note

#Create a Note-----------------------------
def create_note(
    db: Session,
    content: str,
    title: str 
):
    note = Note(
        title=title,
        content=content
    )
    db.add(note)
    db.commit()
    db.refresh(note)
    return note

#Get all Notes---------------------------------------------
def get_all_notes(db: Session) -> list[Note]:
   stmt = select(Note).order_by(Note.created_at.desc())
   return db.scalars(stmt).all()



#Get Note By id----------------------------------------
def get_note_by_id(db:Session,note_id:int)-> Note | None:
    stmt = select(Note).where(Note.id == note_id)
    result= db.execute(stmt).scalar_one_or_none()
    return result


