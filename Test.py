# Simple Hello World program
def main():
    print("Hello, World!")

def test():
    print('Hi')

# Recursive Fibonacci function
def fibonacci(n):
    if n <= 0:
        return "Invalid input, n must be a positive integer."
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Example usage
if __name__ == "__main__":
    main()
    n = 10  # Change this value to generate more terms
    print(f"The {n}th Fibonacci number is: {fibonacci(n)}")