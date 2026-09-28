import random
import string

from toolkit.file_operations import save_output


def random_menu():

    print("""
Random Data Generation:

1. Generate Random Number
2. Generate Random List
3. Create Random Password
4. Generate Random OTP
5. Back to Main Menu
""")

    choice = int(input("Enter your choice: "))


    # 1. Random Number
    if choice == 1:

        number = random.randint(1, 100)

        print("Generated Random Number:", number)

        save_output(
            f"Generated Random Number: {number}"
        )


    # 2. Random List
    elif choice == 2:

        numbers = []

        for i in range(5):

            numbers.append(
                random.randint(1, 100)
            )

        print("Generated Random List:", numbers)

        save_output(
            f"Generated Random List: {numbers}"
        )


    # 3. Random Password
    elif choice == 3:

        length = int(
            input("Enter password length: ")
        )

        characters = (
            string.ascii_letters
            + string.digits
            + string.punctuation
        )

        password = ""

        for i in range(length):

            password += random.choice(
                characters
            )

        print("Generated Password:", password)

        save_output(
            f"Generated Password: {password}"
        )


    # 4. Random OTP
    elif choice == 4:

        otp = random.randint(
            100000,
            999999
        )

        print("Generated OTP:", otp)

        save_output(
            f"Generated OTP: {otp}"
        )


    # 5. Back
    elif choice == 5:

        print("Returning to Main Menu")


    else:

        print("Invalid Input!")