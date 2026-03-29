from fastapi import FastAPI, HTTPException
from app.models import T24Request, T24Response
from app.services.ofs_generator import generate_ofs
from app.utils.txn_cache import is_duplicate

app = FastAPI(title="T24 OFS API")

@app.post("/send-to-t24", response_model=T24Response)
async def send_to_t24_api(req: T24Request):
    # Prevent duplicates
    if is_duplicate(req.txn_ref):
        raise HTTPException(
            status_code=400,
            detail=f"TXNREF {req.txn_ref} already used. Try a new txn_ref."
        )

    # Generate OFS message
    ofs_msg = generate_ofs(req.dict())

    # Return OFS
    return T24Response(ofs_message=ofs_msg, status="SUCCESS")