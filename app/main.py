from fastapi import FastAPI, HTTPException, status

from app.core.db import engine
from app.schemas.note import (
    NoteCreateSchema,
    NoteIdSchema,
    NoteReadSchema
)
from app.models.note import NoteOrm

from app.helpers.crypto import encrypt_and_compress, decrypt_and_decompress

from bson import ObjectId
from bson.errors import InvalidId

app = FastAPI()


@app.post("/create", response_model=NoteIdSchema)
async def create_note(note_input: NoteCreateSchema):
    encrypted_content = encrypt_and_compress(note_input.content, note_input.password)
    new_note = NoteOrm(content=encrypted_content)
    return await engine.save(new_note)


@app.get("/get/{note_id}", response_model=NoteReadSchema)
async def get_note(note_id: str, password: str):
    try:
        note = await engine.find_one(NoteOrm, {"_id": ObjectId(note_id)})
        if note is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"note {note_id} not found")
    
        content = decrypt_and_decompress(note.content, password)
        return {"content": content}
    except InvalidId:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="bad id")


@app.get("/count", response_model=int)
async def get_count():
    return await engine.count(NoteOrm)
