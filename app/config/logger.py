import logging
import os

# Define log directory inside 'app'
BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # 'D:/interview/zimozi_1/app/config'
APP_DIR = os.path.dirname(BASE_DIR)  # 'D:/interview/zimozi_1/app'
LOG_DIR = os.path.join(APP_DIR, "logs")
LOG_FILE = os.path.join(LOG_DIR, "app.log")

# Ensure the "logs" folder exists inside 'app'
os.makedirs(LOG_DIR, exist_ok=True)

# Create logger
logger = logging.getLogger("fastapi")
logger.setLevel(logging.INFO)

# Remove existing handlers (prevents duplicates)
if logger.hasHandlers():
    for handler in logger.handlers:
        handler.close()  # Close the file handler
    logger.handlers.clear()

# Add file handler
file_handler = logging.FileHandler(LOG_FILE)
file_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))
logger.addHandler(file_handler)

logger.propagate = False  # Prevent duplicate logs


