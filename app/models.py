# app/models.py
from pydantic import BaseModel
from typing import List, Optional

class T24Request(BaseModel):
    txn_ref: str
    req_name: str
    api_sub: str
    agent_id: Optional[str] = ""
    secret_code: Optional[str] = ""
    data: List[str]

class T24Response(BaseModel):
    ofs_message: str
    status: str = "SUCCESS"