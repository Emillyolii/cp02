def fibonacci(n):
    fib_sequence = [0, 1]

    while len(fib_sequence) < n:
        next_term = fib_sequence[-1] + fib_sequence[-2]

        print(next_term)

        fib_sequence.append(next_term)

    return fib_sequence


print("Fibonacci:")
fibonacci(20)
