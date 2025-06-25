import logging
import sys
import os
from datetime import datetime


log_path = os.path.join(os.getcwd(),"logs")
os.makedirs(log_path, exist_ok=True)

LOG_FILE = f"{datetime.now().strftime('%Y-%m-%d_%H_%M_%S')}.log"
LOG_FILE_PATH = os.path.join(log_path, LOG_FILE)

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO,
        handlers=[
        logging.FileHandler(LOG_FILE_PATH),
        logging.StreamHandler(sys.stdout)
    ]
)



logger=logging.getLogger(__name__)