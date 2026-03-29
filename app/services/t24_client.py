# app/services/t24_client.py
import httpx
from app.config import T24_ENDPOINT
from app.utils.logger import log_info, log_error

async def send_to_t24(ofs_message: str) -> str:
    """
    Send OFS message to T24 using HTTPX.
    """
    try:
        async with httpx.AsyncClient(timeout=10.0) as client:
            payload = {"ofs_message": ofs_message}
            response = await client.post(T24_ENDPOINT, json=payload)
            response.raise_for_status()
            log_info(f"Sent to T24: {ofs_message}")
            return response.text
    except Exception as e:
        log_error(f"Error sending to T24: {str(e)}")
        return f"ERROR: {str(e)}"