from pydantic import BaseModel


# BUG (old code): class Item:
# CHANGES: Added BaseModel inheritance to Item
class Item(BaseModel):
    # BUG (old code): name: int
    # CHANGES: Changed type of name from int to str
    name: str
    description: str


class User(BaseModel):
    username: str
    bio: str

    # You can raise your hands and give the answer to the chocolate question
