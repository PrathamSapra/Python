def generate_fibonacci(n):
    fibonacci_series = [0, 1]  # Initialize the series with the first two Fibonacci numbers

    while len(fibonacci_series) < n:
        next_number = fibonacci_series[-1] + fibonacci_series[-2]
        fibonacci_series.append(next_number)

    return fibonacci_series

# Get user input for the number of terms in the series
terms = int(input("Enter the number of Fibonacci terms to generate: "))

# Call the function to generate the Fibonacci series
result = generate_fibonacci(terms)

# Display the generated Fibonacci series
print("Fibonacci Series:")
print(result)
