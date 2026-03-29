from app.config import ATM_ID
from datetime import datetime

def generate_ofs(req: dict) -> str:
    ofs_message = f"CND.MIDWARE.REQ,/I/PROCESS,{ATM_ID},,"

    # Fixed fields
    ofs_message += f"REQ.NAME:1:1={req['req_name'].upper()},"
    ofs_message += f"API.SUB:1:1={req['api_sub'].upper()},"
    if req.get("agent_id"):
        ofs_message += f"AGENT_ID:1:1={req['agent_id'].upper()},"
    if req.get("secret_code"):
        ofs_message += f"SECRET_CODE:1:1={req['secret_code'].upper()},"

    txn_ref = req['txn_ref'].upper()
    ofs_message += f"TXNREF:1:1={txn_ref},"

    # MSG.ID = prefix from API.SUB + TXNREF + timestamp
    prefix = "".join([p[0].upper() for p in req['api_sub'].split(".")])
    timestamp = datetime.now().strftime("%y%m%d%H%M%S")
    msg_id = f"{prefix}-{txn_ref}-{timestamp}"
    ofs_message += f"MSG.ID:1:1={msg_id},"

    # Dynamic data
    for row in req.get("data", []):
        fields = row.split(",")
        for field in fields:
            if "=" in field:
                key, value = field.split("=", 1)
                ofs_message += f"{key.upper()}:1:1={value.upper()},"

    return ofs_message.rstrip(",")