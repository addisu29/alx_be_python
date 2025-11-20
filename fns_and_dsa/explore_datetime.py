from datetime import datetime, timedelta

def display_current_datetime():
    current_date = datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted_date}")
    return current_date

def calculate_future_date(days):
    current_date = datetime.now()
    future_date = current_date + timedelta(days=days)
    formatted_future = future_date.strftime("%Y-%m-%d")
    print(f"Future date: {formatted_future}")
    return future_date

def main():
    display_current_datetime()

    days_input = input("Enter the number of days to add to the current date: ")

    try:
        days = int(days_input)
        calculate_future_date(days)
    except ValueError:
        print("Please enter a valid integer.")

if __name__ == "__main__":
    main()
