from toolkit import datetime_operations
from toolkit import math_operations
from toolkit import random_operations
from toolkit import uuid_operations
from toolkit import file_operations
from toolkit import module_explorer


def main():

    while True:

        print("\n==================================")
        print("Welcome To Multi-Utility Toolkit")
        print("==================================")

        print("""
1. Datetime And Time Operations
2. Mathematical Operations
3. Random Data Generation
4. Generate Unique Identifiers (UUID)
5. File Operations (Custom Module)
6. Explore Module Attributes (dir())
7. Exit
""")

        try:
            choice = int(input("Enter Your Choice Here: "))

        except ValueError:
            print("Please enter a number!")
            continue


        if choice == 1:

            datetime_operations.datetime_menu()


        elif choice == 2:

            math_operations.math_menu()


        elif choice == 3:

            random_operations.random_menu()


        elif choice == 4:

            uuid_operations.uuid_menu()


        elif choice == 5:

            file_operations.file_menu()


        elif choice == 6:

            module_explorer.explorer_menu()


        elif choice == 7:

            print("Thank You For Using Multi-Utility Toolkit!")

            file_operations.save_output(
                "Program closed by user."
            )

            break


        else:

            print("Invalid Input!")


if __name__ == "__main__":
    main()