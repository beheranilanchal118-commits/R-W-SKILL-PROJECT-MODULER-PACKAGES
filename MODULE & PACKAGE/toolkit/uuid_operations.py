import uuid

from toolkit.file_operations import save_output


def uuid_menu():

    print("""
Generate Unique Identifiers:

1. Generate UUID4
2. Back to Main Menu
""")

    choice = int(input("Enter your choice: "))

    if choice == 1:

        unique_id = uuid.uuid4()

        print("Generated UUID:", unique_id)

        save_output(
            f"Generated UUID: {unique_id}"
        )

    elif choice == 2:

        print("Returning to Main Menu")

    else:

        print("Invalid Input!")