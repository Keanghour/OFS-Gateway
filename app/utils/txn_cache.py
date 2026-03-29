import time

TXNREF_CACHE = {}
EXPIRY_SECONDS = 60

def is_duplicate(txn_ref: str) -> bool:
    now = time.time()
    # Remove old entries
    for ref in list(TXNREF_CACHE.keys()):
        if now - TXNREF_CACHE[ref] > EXPIRY_SECONDS:
            del TXNREF_CACHE[ref]

    if txn_ref in TXNREF_CACHE:
        return True

    TXNREF_CACHE[txn_ref] = now
    return False