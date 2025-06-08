from datetime import datetime, timedelta

def display_current_datetime():
    return datetime.now()

def calculate_future_date(current_date, days):
    return current_date + timedelta(days=days)

current_date = display_current_datetime()
formatted_current = current_date.strftime("%Y-%m-%d %H:%M:%S")
print("Current date and time:", formatted_current)


days = int(input("Enter the number of days to add to the current date: "))


future_date = calculate_future_date(current_date, days)
formatted_future = future_date.strftime("%Y-%m-%d %H:%M:%S")
print("Future date:", formatted_future)
