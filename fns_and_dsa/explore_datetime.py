from datetime import datetime, timedelta

def display_current_datetime():
    return datetime.now()

def calculate_future_date(current_date, days):
    return current_date + timedelta(days=days)


current_date = display_current_datetime()
print("Current date and time:", current_date)


days = int(input("Enter the number of days to add to the current date: "))

future_date = calculate_future_date(current_date, days)
print("Future date:", future_date)
