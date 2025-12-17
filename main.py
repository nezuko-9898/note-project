from fastapi import FastAPI
from app.core.database import engine, BASE
from app.routes.note_routes import router


BASE.metadata.create_all(bind=engine)
app = FastAPI()

app.include_router(router)
