from fastapi import FastAPI


app = FastAPI(
    title="FastAPI",
    description="This is a fantastic app",
    version="0.1",
    docs_url="/"
)

# @app.get("/")
# async def root():
#     return {"message": "Hello World"}

@app.get("/notes")
async def get_all_notes():
    return {"message": "This is a list of notes"}

@app.post("/notes")
async def create_note():
    return {"message": "This is a list of notes"}

@app.get("/notes/{note_id}")
async def get_note_by_id(note_id: int):
    return {"message": "This is a list of notes"}

@app.patch("/notes/{note_id}")
async def update_note(note_id: int):
    return {"message": "This is a list of notes"}

@app.delete("/notes/{note_id}")
async def delete_note(note_id: int):
    return {"message": "This is a list of notes"}