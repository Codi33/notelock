from pydantic import BaseModel, Field
from odmantic.bson import ObjectId


class NoteIdSchema(BaseModel):
    id: ObjectId


class NoteBase(BaseModel):
    content: str = Field(max_length=1000)


class NoteCreateSchema(NoteBase):
    password: str


class NoteReadSchema(NoteBase):
    pass
