import logging
import time
from datetime import datetime, timedelta
from cal import get_upcoming_events, should_raise_desk, calculate_raise_time, time_until_raise
from logger import get_logger
from desk_control import raise_desk


logger = get_logger(__name__)

# # Set up logging
# logging.basicConfig(
#     level=logging.INFO,
#     format='%(asctime)s - %(levelname)s - %(message)s',
#     filename='desk_automation.log'
# )
logger = logging.getLogger('desk_automation')


def main():
    """
    Main function to check for upcoming meetings and raise the desk if needed.
    """
    logger.info(f"Starting desk automation check at {datetime.now()}")
    
    # Get upcoming events
    events = get_upcoming_events()
    
    # Find the next red meeting (if any)
    next_red_meeting = None
    next_raise_time = None
    
    for event in events:
        if should_raise_desk(event):
            raise_time = calculate_raise_time(event)
            seconds_until_raise = time_until_raise(raise_time)
            
            # If we need to raise within the next 15 minutes (typical cron interval)
            # and the meeting hasn't started yet
            if 0 <= seconds_until_raise <= 15 * 60 and time_until_raise(event.start) > 0:
                next_red_meeting = event
                next_raise_time = raise_time
                break
    
    # Raise desk if it's time
    if next_red_meeting:
        seconds_until_raise = time_until_raise(next_raise_time)
        
        if 0 <= seconds_until_raise <= 60:  # If we're within 1 minute of target raise time
            logger.info(f"It's time to raise desk for meeting: {next_red_meeting.summary}")
            raise_desk()
        elif seconds_until_raise <= 15 * 60:  # If it's within 15 minutes
            logger.info(f"Waiting {seconds_until_raise:.1f} seconds to raise desk for: {next_red_meeting.summary}")
            time.sleep(seconds_until_raise)
            logger.info(f"It's time to raise desk for meeting: {next_red_meeting.summary}")
            raise_desk()
        else:
            logger.info(f"Next desk raise scheduled in {seconds_until_raise:.1f} seconds for: {next_red_meeting.summary}")
    else:
        logger.info("No upcoming red meetings requiring desk adjustment")

if __name__ == "__main__":
    main()