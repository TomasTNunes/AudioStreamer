import os
import logging
from logging.handlers import RotatingFileHandler

# Define the log file path
log_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'audiostreamer.log')

# Configure logging
logger = logging.getLogger('AudioStreamerLogger')
logger.setLevel(logging.INFO)

# Create handlers
console_handler = logging.StreamHandler()
file_handler = RotatingFileHandler(log_file_path, maxBytes=1*1024*1024*1024, backupCount=1)

# Create formatters and add them to the handlers
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
console_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

# Add handlers to the logger
logger.addHandler(console_handler)
logger.addHandler(file_handler)