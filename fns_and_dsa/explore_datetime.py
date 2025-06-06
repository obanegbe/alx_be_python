from datetime import datetime, date, time, timedelta



def display_current_datetime():
    return datetime.now()


current_date = display_current_datetime()
print(f"Current date and time: {current_date}")


def calculate_future_date():
    number_of_days = int(input("Enter the number of days to add to the current date:: "))
    
    today = date.today()
    delta = timedelta(days=number_of_days)
    return today + delta


future_date = calculate_future_date()
print(f"Future date: {future_date}")
