import logging
import os
from datetime import datetime

# Create logs directory if it doesn't exist
os.makedirs('logs', exist_ok=True)

# Get current date for log file naming
current_date = datetime.now().strftime('%Y-%m-%d')
log_file = f'logs/desk_automation_{current_date}.log'

# Set up logging configuration
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        # File handler with daily rotation
        logging.FileHandler(log_file),
        # Console handler for immediate feedback
        logging.StreamHandler()
    ]
)

# Create named loggers for different modules
def get_logger(name):
    """
    Returns a logger with the specified name.
    
    Args:
        name (str): The name of the logger, typically __name__ from the calling module
        
    Returns:
        logging.Logger: Configured logger instance
    """
    return logging.getLogger(name)