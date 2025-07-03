def format_converter(current_format: str):
    current_time, *current_meridiem = current_format.split()
    if "AM" in current_meridiem:
        return f"00:{current_time.split(":")[-1]}" if current_format.startswith("12:") else current_time
    elif "PM" in current_meridiem:
        return current_time if current_time.startswith("12:") else f"{int(current_time.split(":")[0]) + 12}:{current_time.split(":")[-1]}"
    else:
        hours, minutes = current_format.split(":")
        if int(hours) < 24:
            if int(hours) > 12:
                return f"{int(hours) - 12}:{minutes.rjust(2, "0")} PM"
            elif int(hours) == 12:
                return f"{hours}:{minutes.rjust(2, "0")} PM"
            else:
                return f"{hours}:{minutes.rjust(2, "0")} AM"
        else:
            hours_12 = int(hours) % 24
            if hours_12 > 12:
                return f"{hours_12 - 12}:{minutes.rjust(2, "0")} PM"
            else:
                return f"12:{minutes.rjust(2, "0")} AM" if hours_12 == 0 else f"{hours_12}:{minutes.rjust(2, "0")} AM"


def add_time(start: str, duration: str, start_day: str = ""):
    start_time_24: str = format_converter(start)
    structured_start_time = start_time_24.split(":")
    structured_duration = duration.split(":")
    new_minutes = int(structured_start_time[-1]) + int(structured_duration[-1])
    carry_over: int = 0
    next_day: str = start_day
    week = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
    if new_minutes > 59:
        carry_over += 1
        new_minutes -= 60
    new_hours = int(structured_start_time[0]) + int(structured_duration[0]) + carry_over
    days_elapsed = new_hours // 24
    if days_elapsed:
        if start_day:
            if days_elapsed == 1:
                next_day = f"{week[week.index(start_day.capitalize()) + days_elapsed]} (next day)"
            else:
                next_day = f"{week[(week.index(start_day.capitalize()) + days_elapsed) % 7]} ({days_elapsed} days later)"
        elif days_elapsed == 1:
            next_day = "(next day)"
        else:
            next_day = f"({days_elapsed} days later)"
    new_time = format_converter(f"{new_hours}:{new_minutes}")
    return (f"{new_time}" if not start_day else f"{new_time}, {next_day}") if not days_elapsed else (f"{new_time} {next_day}" if not start_day else f"{new_time}, {next_day}")
    
inputs = (("3:00 PM", "3:10"), ("11:30 AM", "2:32", "Monday"), ("11:43 AM", "00:20"), ("10:10 PM", "3:30"), ("11:43 PM", "24:20", "tueSday"), ("2:59 AM", "24:00", "saturDay"), ("11:59 PM", "24:05", "Wednesday"), ("8:16 PM", "466:02", "tuesday"))

for input in inputs:
    print(add_time(*input))
