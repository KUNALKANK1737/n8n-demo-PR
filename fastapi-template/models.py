from typing import Optional
from pydantic import BaseModel


class MsgPayload(BaseModel):
    msg_id: Optional[int]
    msg_name: str
print("Hello World")
print("Hello World")



