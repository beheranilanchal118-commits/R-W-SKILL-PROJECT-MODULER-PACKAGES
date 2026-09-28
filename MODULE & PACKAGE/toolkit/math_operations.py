import math

from toolkit.file_operations import save_output


def math_menu():

    print("""
Mathematical Operations:

1. Calculate Factorial
2. Solve Compound Interest
3. Trigonometric Calculations
4. Area of Geometric Shapes
5. Back to Main Menu
""")

    choice = int(input("Enter your choice: "))


    # 1. Factorial
    if choice == 1:

        num = int(input("Enter a number: "))

        result = math.factorial(num)

        print("Factorial:", result)

        save_output(
            f"Factorial of {num}: {result}"
        )


    # 2. Compound Interest
    elif choice == 2:

        principal = float(
            input("Enter principal amount: ")
        )

        rate = float(
            input("Enter rate of interest (in %): ")
        )

        time = float(
            input("Enter time (in years): ")
        )

        amount = principal * math.pow(
            1 + rate / 100,
            time
        )

        result = round(amount, 2)

        print("Compound Interest:", result)

        save_output(
            f"Compound Interest: {result}"
        )


    # 3. Trigonometric Calculations
    elif choice == 3:

        angle = float(
            input("Enter angle in degrees: ")
        )

        sin_value = round(
            math.sin(math.radians(angle)),
            2
        )

        cos_value = round(
            math.cos(math.radians(angle)),
            2
        )

        tan_value = round(
            math.tan(math.radians(angle)),
            2
        )

        print("Sin:", sin_value)
        print("Cos:", cos_value)
        print("Tan:", tan_value)

        save_output(
            f"Trigonometric Calculation - "
            f"Angle: {angle}, "
            f"Sin: {sin_value}, "
            f"Cos: {cos_value}, "
            f"Tan: {tan_value}"
        )


    # 4. Area of Geometric Shapes
    elif choice == 4:

        print("""
Area of Geometric Shapes:

1. Circle
2. Rectangle
3. Square
4. Triangle
""")

        shape = int(
            input("Enter your choice: ")
        )


        if shape == 1:

            radius = float(
                input("Enter radius: ")
            )

            area = math.pi * math.pow(
                radius,
                2
            )

            result = round(area, 2)

            print("Area of Circle:", result)

            save_output(
                f"Area of Circle: {result}"
            )


        elif shape == 2:

            length = float(
                input("Enter length: ")
            )

            breadth = float(
                input("Enter breadth: ")
            )

            area = length * breadth

            result = round(area, 2)

            print("Area of Rectangle:", result)

            save_output(
                f"Area of Rectangle: {result}"
            )


        elif shape == 3:

            side = float(
                input("Enter side: ")
            )

            area = math.pow(
                side,
                2
            )

            result = round(area, 2)

            print("Area of Square:", result)

            save_output(
                f"Area of Square: {result}"
            )


        elif shape == 4:

            base = float(
                input("Enter base: ")
            )

            height = float(
                input("Enter height: ")
            )

            area = 0.5 * base * height

            result = round(area, 2)

            print("Area of Triangle:", result)

            save_output(
                f"Area of Triangle: {result}"
            )


        else:

            print("Invalid Input!")


    # 5. Back
    elif choice == 5:

        print("Returning to Main Menu")


    else:

        print("Invalid Input!")