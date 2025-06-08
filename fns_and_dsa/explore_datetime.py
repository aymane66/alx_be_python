import datetime

def display_current_datetime():
    current_date = datetime.datetime.now()
    return current_date

print("Current date and time: ", display_current_datetime())
days = int(input("Enter the number of days to add to the current date: "))
current_date = display_current_datetime()
future_date = current_date + datetime.timedelta(days=days)
print("Future date: ", future_date)