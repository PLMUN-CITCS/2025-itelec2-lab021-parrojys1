"""Takes a non-negative integer from user and calculates the factorial of the input."""
def git_non_negative_integer():
    """Prompts user for a non-negative integer and returns the value.

    Returns:
        integer: The non-negative integer entered by the user.
    """
    while True:
        try:
            x = int(input("Enter a non-negative integer: "))
            if x < 0:
                print("Sorry, your response must not be negative.")
                continue
            return x
        except ValueError:
            print("Sorry, your response must be an integer.")

def calculate_factorial(n):
    """Calculates the factorial of a non-negative integer.

    Args:
        n (integer): The non-negative integer for which the factorial will be calculated.

    Returns:
        integer: The factorial of the input integer.
    """
    if n == 0:
        y = 1
    else:
        y = n * calculate_factorial(n - 1)
    return y

if __name__ == "__main__":
    print(calculate_factorial(git_non_negative_integer()))
