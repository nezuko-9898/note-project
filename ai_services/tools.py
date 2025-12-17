from sqlalchemy import select
from sqlalchemy.orm import Session
from app.models.note import Note


def note_as_text(db:Session)->str:
    stmt = select(Note)
    note= db.scalars(stmt).all()



    if not note:
        return "No notes available"
    

    return  '\n\n'.join(

         f"Title: {n.title or 'Untitled'} Content: {n.content}"
         for n in note
    )

     