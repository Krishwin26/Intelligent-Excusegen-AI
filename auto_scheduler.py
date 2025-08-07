import json
from datetime import datetime, timedelta

def suggest_next_excuse_time():
    try:
        with open("history.json", "r") as f:
            lines = f.readlines()
            if not lines:
                return "Tomorrow at 9 AM"
            last_entry = json.loads(lines[-1])
            last_time = datetime.strptime(last_entry["timestamp"], "%Y-%m-%d %H:%M:%S.%f")
            next_time = last_time + timedelta(days=1)
            return next_time.strftime("%A at %I:%M %p")
    except:
        return "Monday at 9 AM"