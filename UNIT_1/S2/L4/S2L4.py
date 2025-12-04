import math

def get_float(prompt: str) -> float:
    # Helper function to get a valid float input from the user.
    while True:
        value = input(prompt)
        try:
            return float(value)
        except ValueError:
            print("Invalid input. Please enter a numeric value.")


def calc_square_perimeter() -> float:
    # Calculate the perimeter of a square.
    side = get_float("Enter the length of one side of the square: ")
    return 4 * side


def calc_circle_perimeter() -> float:
    # Calculate the perimeter (circumference) of a circle.
    radius = get_float("Enter the radius of the circle: ")
    return 2 * math.pi * radius


def calc_rectangle_perimeter() -> float:
    # Calculate the perimeter of a rectangle.
    length = get_float("Enter the length of the rectangle: ")
    width = get_float("Enter the width of the rectangle: ")
    return 2 * (length + width)


def main():
    print("Perimeter Calculator")
    print("--------------------")

    usr_input = input(
        "Enter a number to calculate the perimeter of a geometric figure "
        "(1 = Square, 2 = Circle, 3 = Rectangle): "
    )

    while usr_input not in ['1', '2', '3']:
        usr_input = input("Invalid input. Please enter 1, 2, or 3: ")

    if usr_input == '1':
        perimeter = calc_square_perimeter()
        print(f"The perimeter of the square is: {perimeter}")
    elif usr_input == '2':
        perimeter = calc_circle_perimeter()
        print(f"The perimeter of the circle is: {perimeter}")
    else:
        perimeter = calc_rectangle_perimeter()
        print(f"The perimeter of the rectangle is: {perimeter}")


if __name__ == "__main__": # Only executable when run as a script
    main()
