from gcsa.event import Event
from gcsa.google_calendar import GoogleCalendar
from gcsa.recurrence import Recurrence, DAILY, SU, SA
from beautiful_date import Jan, Apr, Mar



gc = GoogleCalendar(credentials_path='/Users/mitrev/apps/desky/.credentials/secret.json')

for event in gc:
    print(event)

start_date=(1 / Jan / 2025)[9:00]
end_date=(1 / Jan / 2026)[9:00]



try:
    colors = gc.get_colors()
    color_map = colors.get('event', {})
    print("Available calendar colors:")
    for color_id, color_info in color_map.items():
        print(f"Color ID: {color_id}, Background: {color_info['background']}")
except Exception as e:
    print(f"Error getting colors: {e}")
    color_map = {}

# Get all events
print("\nUpcoming events with colors:")
print("-" * 60)

try:
    events = list(gc.get_events(start_date, end_date))
    
    if not events:
        print("No events found in the next 30 days.")
    else:
        for event in events:
            color_id = event.color_id
            color_hex = color_map.get(color_id, {}).get('background', 'No color') if color_id else 'Default'
            
            # Format dates properly
            start_time = event.start.strftime('%Y-%m-%d %H:%M') if hasattr(event.start, 'strftime') else 'Unknown'
            end_time = event.end.strftime('%Y-%m-%d %H:%M') if hasattr(event.end, 'strftime') else 'Unknown'
            
            print(f"Event: {event.summary}")
            print(f"  Start: {start_time}")
            print(f"  End: {end_time}")
            print(f"  Color ID: {color_id or 'Default'}")
            print(f"  Color Hex: {color_hex}")
            print(f"  Location: {event.location or 'No location'}")
            print (f"  Recurrance {event.recurrence}")
            print("-" * 60)
except Exception as e:
    print(f"Error retrieving events: {e}")



###create event

# event = Event(
#     'Breakfast',
#     start=(1 / Jan / 2025)[9:00],
#     recurrence=[
#         Recurrence.rule(freq=DAILY),
#         Recurrence.exclude_rule(by_week_day=[SU, SA]),
#         Recurrence.exclude_times([
#             (19 / Apr / 2025)[9:00],
#             (22 / Apr / 2025)[9:00]
#         ])
#     ],
#     minutes_before_email_reminder=50
# )

# calendar.add_event(event)

# for event in calendar:
#     print(event)


start_date=(12 / Mar / 2025)[9:00]
end_date=(14 / Mar / 2025)[9:00]

events = list(gc.get_events(start_date, end_date))
  

for event in events:
    print(event, event.color_id)
    print(event.color_id)