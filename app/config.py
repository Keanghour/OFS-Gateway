import os

T24_ENDPOINT = "http://internal-t24-server:8080"  # replace with actual port
ATM_ID = "CFC.ATM/123456/KH0010001"

# Logging
LOG_FOLDER = "app/logs"
os.makedirs(LOG_FOLDER, exist_ok=True)
LOG_FILE = os.path.join(LOG_FOLDER, "t24_api.log")