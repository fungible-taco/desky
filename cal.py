import os
from logger import get_logger
import time
from datetime import datetime, timedelta
from dotenv import load_dotenv
from gcsa.event import Event
from gcsa.google_calendar import GoogleCalendar
import pytz

load_dotenv()

logger = get_logger(__name__)
gcpath = os.getenv("credentials_path")
lookahead_mins = os.getenv("lookahead_mins")
target_color_id = os.getenv("target_color_id")
mins_before_event = os.getenv("mins_before_event")
token_path = os.getenv("token_path")

gc = GoogleCalendar(credentials_path=gcpath, token_path=token_path)

def get_upcoming_events (minutres_ahead = lookahead_mins):
    try:
        now = datetime.now(pytz.FixedOffset(120))
        end_time = now + timedelta(minutes = int(minutres_ahead))

        logger.info(f"Fetching events from now until {end_time}")
        
        events = list(gc.get_events(now, end_time))
        logger.info(f"Found {len(events)} upcoming events")

        return events
    except Exception as e:
        logger.error(f"Error fetching events: {e}")
        return []


def should_raise_desk(event):
    if event.color_id == target_color_id:
        logger.info(f"Found red meeting {event.summary}")
        return True
    return False


def calculate_raise_time(event):

    raise_time = event.start - timedelta(minutes = int(mins_before_event))
    return raise_time


def time_until_raise(raise_time):
   
    now = datetime.now(pytz.FixedOffset(120))
    time_diff = raise_time - now
    return time_diff.total_seconds()