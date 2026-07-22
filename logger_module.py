import logging
import os
from datetime import datetime

PROJECT_NAME = "coforge_healthcare_project"

# Current Date
current_date = datetime.now().strftime("%Y-%m-%d")

# Create Daily Log Folder
daily_log_folder = os.path.join(
    "logs",
    current_date
)

os.makedirs(
    daily_log_folder,
    exist_ok=True
)

# Log File Names
log_file_name = (
    f"{PROJECT_NAME}-log-{current_date}.log"
)

exception_file_name = (
    f"{PROJECT_NAME}-exception-{current_date}.log"
)

# Log File Paths
log_file_path = os.path.join(
    daily_log_folder,
    log_file_name
)

exception_file_path = os.path.join(
    daily_log_folder,
    exception_file_name
)

# Application Logger
application_logger = logging.getLogger(
    "application_logger"
)
application_logger.setLevel(logging.INFO)

# Exception Logger
exception_logger = logging.getLogger(
    "exception_logger"
)
exception_logger.setLevel(logging.ERROR)

# Log Format
formatter = logging.Formatter(
    "%(asctime)s | %(levelname)s | %(message)s"
)

# Application File Handler
application_file_handler = logging.FileHandler(
    log_file_path,
    mode="a",
    encoding="utf-8"
)

application_file_handler.setLevel(logging.INFO)
application_file_handler.setFormatter(formatter)

# Exception File Handler
exception_file_handler = logging.FileHandler(
    exception_file_path,
    mode="a",
    encoding="utf-8"
)

exception_file_handler.setLevel(logging.ERROR)
exception_file_handler.setFormatter(formatter)

# Add Handlers
if not application_logger.handlers:
    application_logger.addHandler(application_file_handler)

if not exception_logger.handlers:
    exception_logger.addHandler(exception_file_handler)