from odmantic import Model, Field
from odmantic.bson import Binary


AES_BLOCK_SIZE = 16
MAX_SIZE = 1000 + AES_BLOCK_SIZE


class NoteOrm(Model):
    content: bytes = Field(Binary, max_length=MAX_SIZE)
