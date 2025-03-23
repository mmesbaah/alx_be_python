from datetime import datetime, timedelta
def display_current_datetime():
    current_date = datetime.now()
    formatted_date = current_date.strftime ["%Y-%m-%d %H:%M:%S"]
    print(f"current date and time: {formatted_date}")
def calculate_future_date():
    try:
        number_of_days = int(input["Enter the number of days to add to the current date:"])
    except valueError:
        print("invalid input. please enter a valid integer. ")
        return
    current_date = datetime.now()
    future_date = current_date + timedelta(days=number_of_days)
    formatted_future_date = future_date.strftime("%y-%m-%d")
    print(f"future date: {formatted_future_date}")

if __name__ == "__main__":
    display_current_datetime()
    calculate_future_date()
    
