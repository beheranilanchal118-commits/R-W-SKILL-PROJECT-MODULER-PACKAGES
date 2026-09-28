import datetime
import time

from toolkit.file_operations import save_output


def datetime_menu():

    print("""
Datetime and Time Operations:

1. Display current date and time
2. Calculate difference between two dates/times
3. Format date into custom format
4. Stopwatch
5. Countdown Timer
6. Back to Main Menu
""")

    choice = int(input("Enter your choice: "))


    # 1. Current Date and Time
    if choice == 1:

        current = datetime.datetime.now()

        result = f"Current Date and Time: {current}"

        print(result)

        save_output(result)


    # 2. Difference Between Two Dates
    elif choice == 2:

        first_date = input(
            "Enter the first date (YYYY-MM-DD): "
        )

        second_date = input(
            "Enter the second date (YYYY-MM-DD): "
        )

        first_date = datetime.datetime.strptime(
            first_date,
            "%Y-%m-%d"
        )

        second_date = datetime.datetime.strptime(
            second_date,
            "%Y-%m-%d"
        )

        difference = second_date - first_date

        result = f"Difference: {difference.days} days"

        print(result)

        save_output(result)


    # 3. Custom Date Format
    elif choice == 3:

        current = datetime.datetime.now()

        print("Current Date:", current.date())

        date_format = input(
            "Enter your date format (Example: %d-%m-%Y): "
        )

        formatted_date = current.strftime(
            date_format
        )

        result = f"Formatted Date: {formatted_date}"

        print(result)

        save_output(result)


    # 4. Stopwatch
    elif choice == 4:

        input(
            "Press Enter to start stopwatch..."
        )

        start_time = datetime.datetime.now()

        input(
            "Press Enter to stop stopwatch..."
        )

        end_time = datetime.datetime.now()

        difference = end_time - start_time

        result = f"Stopwatch Time: {difference}"

        print(result)

        save_output(result)


    # 5. Countdown Timer
    elif choice == 5:

        seconds = int(
            input("Enter seconds: ")
        )

        while seconds > 0:

            print("Time:", seconds)

            time.sleep(1)

            seconds -= 1

        result = "Time's Up!"

        print(result)

        save_output(result)


    # 6. Back
    elif choice == 6:

        print("Returning to Main Menu...")


    else:

        print("Invalid Input!")