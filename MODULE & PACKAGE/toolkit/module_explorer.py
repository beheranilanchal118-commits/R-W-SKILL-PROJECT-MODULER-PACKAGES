import importlib

from toolkit.file_operations import save_output


def explorer_menu():

    print("""
Explore Module Attributes:

1. Explore Module
2. Back to Main Menu
""")

    choice = int(input("Enter your choice: "))

    if choice == 1:

        module_name = input(
            "Enter module name to explore: "
        )

        try:

            module = importlib.import_module(
                module_name
            )

            attributes = dir(module)

            print(
                f"Available Attributes in {module_name} module:"
            )

            print(attributes)

            save_output(
                f"Available Attributes in {module_name} module:\n"
                f"{attributes}"
            )

        except ModuleNotFoundError:

            print("Module not found!")

            save_output(
                f"Module not found: {module_name}"
            )


    elif choice == 2:

        print("Returning to Main Menu")


    else:

        print("Invalid Input!")