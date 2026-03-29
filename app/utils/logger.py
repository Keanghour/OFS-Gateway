# app/utils/logger.py
import logging
import os
from app.config import LOG_FILE

# Ensure folder exists
os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)

logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def log_info(msg: str):
    logging.info(msg)

def log_error(msg: str):
    logging.error(msg)