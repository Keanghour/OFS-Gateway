
# T24 OFS API

A FastAPI service to generate and send **OFS messages** to a T24 core banking system. This API also prevents duplicate transactions using an in-memory cache.

## Features

* Generate OFS messages from structured JSON requests.
* Auto-create **MSG.ID** using API.SUB, TXNREF, and timestamp.
* Prevent duplicate transactions using `txn_ref`.
* Optional fields: `agent_id`, `secret_code`.
* Can be integrated with T24 via HTTP POST requests.

## Installation

1. Clone the repository:

```bash
git clone <repo-url>
cd <repo-folder>
```

2. Create a Python virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```

3. Install dependencies:

```bash
pip install fastapi uvicorn httpx pydantic
```

## Configuration

Edit `app/config.py` to configure:

```python
T24_ENDPOINT = "xxxx.xxx.xx.xx:xxxx/xxxx"  
ATM_ID = "xxxx"  
LOG_FOLDER = "xxxx"  
```

Logs will be saved in `app/logs/t24_api.log`.

## Running the API

Start the FastAPI server:

```bash
uvicorn app.main:app --reload
```

The API will be available at:

```
POST http://localhost:8000/send-to-t24
```

## Request Format

Send JSON data:

```json
{
  "txn_ref": "TX12345",
  "req_name": "cash_withdrawal",
  "api_sub": "atm.withdraw",
  "agent_id": "AG123",
  "secret_code": "XYZ123",
  "data": [
	"account_no=12345678,amount=500","currency=USD"
  ]
}
```

## Response Format

```json
{
  "ofs_message": "CND.MIDWARE.REQ,/I/PROCESS,CFC.ATM/123456/KH0010001,,REQ.NAME:1:1=CASH_WITHDRAWAL,API.SUB:1:1=ATM.WITHDRAW,AGENT_ID:1:1=AG123,SECRET_CODE:1:1=XYZ123,TXNREF:1:1=TX12345,MSG.ID:1:1=AW-TX12345-260329101530,ACCOUNT_NO:1:1=12345678,AMOUNT:1:1=500,CURRENCY:1:1=USD",
  "status": "SUCCESS"
}
```

## Duplicate Prevention

* `txn_ref` is used to detect duplicates.
* Duplicates within **60 seconds** are rejected.

## Sending to T24

Use `send_to_t24(ofs_message)` function to POST messages to the configured `T24_ENDPOINT`.

---


## ☕ Support / Buy Me a Coffee

If you like this project and want to support me, you can:

| Option                  | Link / QR                                         |
| ----------------------- | ------------------------------------------------- |
| 🏦**ABA Bank QR** | [ABA Bank QR](https://pay.ababank.com/oRF8/fe6dcb9h) |
| 💬**Telegram**    | [@phokeanghour](https://t.me/phokeanghour)           |

> 🙏 Your support helps me keep building and improving this project!
>
