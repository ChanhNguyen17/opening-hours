def convert_unix_to_string(unix_time):
    if 0 <= unix_time <= 86399:
        hours = unix_time // 3600
        minutes = (unix_time % 3600) // 60
        seconds = (unix_time % 3600) % 60
        am_pm = "AM" if hours < 12 else "PM"
        if hours == 0:
            hours = 12
        elif hours > 12:
            hours -= 12
        if seconds > 0:
            formatted_time = "{}:{:02d}:{:02d} {}".format(hours, minutes, seconds, am_pm)
        elif minutes > 0:
            formatted_time = "{}:{:02d} {}".format(hours, minutes, am_pm)
        else:
            formatted_time = "{} {}".format(hours, am_pm)
        return formatted_time
    else:
        return "Invalid UNIX time"


def safe_parse_int(value, default=None):
    try:
        return int(value)
    except (ValueError, TypeError):
        return default
