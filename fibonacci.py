



def generate_fibonacci(n):
    fibonacci_sequence = [0, 1]

    for i in range(2, n):
        next_term = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_term)

    return fibonacci_sequence

# Prompt the user for the number of terms
num_terms = int(input("Enter the number of terms in the Fibonacci sequence: "))

# Generate and display the Fibonacci sequence
fib_sequence = generate_fibonacci(num_terms)
print("Fibonacci Sequence:")
print(fib_sequence)