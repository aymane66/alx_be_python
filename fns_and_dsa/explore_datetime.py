from datetime import datetime, timedelta

def display_current_datetime():
    current_date = datetime.now()
    return current_date


current_date = display_current_datetime()
print("Current date and time: ", current_date)


days = int(input("Enter the number of days to add to the current date: "))


future_date = current_date + timedelta(days=days)
print("Future date: ", future_date)
