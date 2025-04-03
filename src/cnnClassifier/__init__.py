import os
import sys
import logging

# Define the logging format
logging_str = "[%(asctime)s : %(levelname)s : %(module)s : %(message)s]"

# Define log directory and file path
log_dir = "logs"
log_filepath = os.path.join(log_dir, "running_logs.log")
os.makedirs(log_dir, exist_ok=True)

# Configure logging
logging.basicConfig(
    level=logging.INFO,  # Corrected `Level` to `level`
    format=logging_str,
    handlers=[
        logging.FileHandler(log_filepath),  # Logs to a file
        logging.StreamHandler(sys.stdout)   # Logs to console
    ]
)

# Get the logger
logger = logging.getLogger("cnnClassifierLogger")
logger.setLevel(logging.INFO)  # Ensure logger captures INFO and above

# Test logging
logger.info("Logging setup is successfully configured.")
