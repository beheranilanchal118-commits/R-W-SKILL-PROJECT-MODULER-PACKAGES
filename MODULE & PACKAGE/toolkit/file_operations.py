def save_output(data):

    with open("output.txt", "a") as file:

        file.write(str(data))
        file.write("\n")


def create_file():

    filename = input("Enter file name: ")

    try:

        with open(filename, "x"):
            pass

        print("File created successfully!")

        save_output(
            f"File created successfully: {filename}"
        )

    except FileExistsError:

        print("File already exists!")

        save_output(
            f"File already exists: {filename}"
        )


def write_file():

    filename = input("Enter file name: ")

    data = input("Enter data to write: ")

    try:

        with open(filename, "w") as file:
            file.write(data)

        print("Data written successfully!")

        save_output(
            f"Data written to {filename}: {data}"
        )

    except FileNotFoundError:

        print("File not found!")

        save_output(
            f"File not found: {filename}"
        )


def read_file():

    filename = input("Enter file name: ")

    try:

        with open(filename, "r") as file:
            data = file.read()

        print("File Content:")
        print(data)

        save_output(
            f"File Content from {filename}: {data}"
        )

    except FileNotFoundError:

        print("File not found!")

        save_output(
            f"File not found: {filename}"
        )


def append_file():

    filename = input("Enter file name: ")

    data = input("Enter data to append: ")

    try:

        with open(filename, "a") as file:
            file.write("\n" + data)

        print("Data appended successfully!")

        save_output(
            f"Data appended to {filename}: {data}"
        )

    except FileNotFoundError:

        print("File not found!")

        save_output(
            f"File not found: {filename}"
        )


def file_menu():

    while True:

        print("""
============================
File Operations:
1. Create a new file
2. Write to a file
3. Read from a file
4. Append to a file
5. Back to Main Menu
============================
""")

        choice = int(input("Enter your choice: "))


        if choice == 1:

            create_file()


        elif choice == 2:

            write_file()


        elif choice == 3:

            read_file()


        elif choice == 4:

            append_file()


        elif choice == 5:

            print("Returning to Main Menu")

            save_output(
                "Returned to Main Menu"
            )

            break


        else:

            print("Invalid Input!")

            save_output(
                "Invalid File Operation Choice"
            )