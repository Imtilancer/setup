def generate_fibonacci_by_terms(n):
    """Generate the Fibonacci series up to a specific number of terms."""
    if n <= 0:
        return []
    series = [0, 1]
    for _ in range(2, n):
        series.append(series[-1] + series[-2])
    return series[:n]

def generate_fibonacci_by_value(max_value):
    """Generate the Fibonacci series up to a specific maximum value."""
    if max_value < 0:
        return []
    series = [0, 1]
    while series[-1] + series[-2] <= max_value:
        series.append(series[-1] + series[-2])
    return series[:-1] if series[-1] > max_value else series

def validate_input(prompt):
    """Validate user input to ensure it is a non-negative integer."""
    while True:
        user_input = input(prompt).strip()
        if user_input.isdigit():
            return int(user_input)
        else:
            print("Invalid input. Please enter a non-negative integer.")

def display_menu():
    """Display the menu and handle user choices."""
    while True:
        print("\nFibonacci Series Generator")
        print("1. Generate Fibonacci series up to a specific number of terms.")
        print("2. Generate Fibonacci series up to a specific maximum value.")
        print("3. Exit")

        choice = input("Enter your choice (1-3): ").strip()

        if choice == "1":
            n_terms = validate_input("Enter the number of terms: ")
            series = generate_fibonacci_by_terms(n_terms)
            print(f"Fibonacci series with {n_terms} terms: {series}")

        elif choice == "2":
            max_value = validate_input("Enter the maximum value: ")
            series = generate_fibonacci_by_value(max_value)
            print(f"Fibonacci series up to {max_value}: {series}")

        elif choice == "3":
            print("Have a good luck for your Exam")
            break

        else:
            print("Your Choice is Invalid")

if __name__ == "__main__":
    display_menu()
