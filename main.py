from datetime import datetime, timedelta


def calculate_work_hours_per_day():
    # Calculate daily work hours for a 38-hour week over 5 days
    weekly_hours = 38
    work_days = 5
    daily_hours = weekly_hours / work_days
    daily_minutes = daily_hours * 60
    hours = int(daily_minutes // 60)
    minutes = int(daily_minutes % 60)
    return hours, minutes


def calculate_work_end_time():
    hours, minutes = calculate_work_hours_per_day()
    print(f"Daily work time: {hours} hours and {minutes} minutes")

    # Input the start time
    start_time_str = input("Please enter your start time (format HH:MM): ")

    try:
        # Convert input to datetime object
        start_time = datetime.strptime(start_time_str, "%H:%M")

        # Define work duration and break time
        work_duration = timedelta(hours=hours, minutes=minutes)
        break_time = timedelta(minutes=45)

        # Calculate end time
        end_time = start_time + work_duration + break_time

        # Format and display the end time
        print(f"Your workday ends at: {end_time.strftime('%H:%M')}")

    except ValueError:
        print("Invalid time input. Please use the format HH:MM.")


if __name__ == "__main__":
    calculate_work_end_time()
