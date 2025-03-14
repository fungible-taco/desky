import logging

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='desk_automation.log'
)
logger = logging.getLogger('desk_automation')