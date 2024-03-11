from fastapi import FastAPI
from sqlalchemy.ext.asyncio import async_sessionmaker
from crud import CRUD
from db import engine
from schemas import NoteModel, NoteCreateModel
from http import HTTPStatus
from typing import List
from models import Note
import uuid
app = FastAPI(
    title="FastAPI",
    description="This is a fantastic app",
    # version="0.1",
    docs_url="/"
)

db=CRUD()

session=async_sessionmaker(
    bind=engine,
    expire_on_commit=False,
)
# @app.get("/")
# async def root():
#     return {"message": "Hello World"}

@app.get("/notes",response_model=List[NoteModel])
async def get_all_notes():
    notes=await db.get_all(session)
    return notes

@app.post("/notes",status_code=HTTPStatus.CREATED.value,response_model=NoteModel)
#  API endpoint for creating a note resource

#     7890

#     Args:
#         note_data (NoteCreateModel): data for creating a note using the note schema

#     Returns:
#         dict: note that has been created
async def create_note(note_data:NoteCreateModel)->dict:
    new_note = Note(
        id=str(uuid.uuid4()), title=note_data.title, content=note_data.content
    )

    note = await db.create(session, new_note)

    return note

@app.get("/notes/{note_id}")
async def get_note_by_id(note_id: str):
    note = await db.get_by_id(session, note_id)

    return note

@app.patch("/notes/{note_id}")
async def update_note(note_id: str, data: NoteCreateModel):
    note = await db.update(
        session, note_id, data={"title": data.title, "content": data.content}
    )

    return note

@app.delete("/notes/{note_id}")
async def delete_note(note_id: str):
    note = await db.get_by_id(session, note_id)

    result = await db.delete(session, note)

    return result