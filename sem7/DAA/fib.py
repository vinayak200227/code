def fibonacci_recursive(n, steps):
    if n <= 1:
        return n, steps + 1
    else:
        fib1, steps = fibonacci_recursive(n - 1, steps)
        fib2, steps = fibonacci_recursive(n - 2, steps)
        return fib1 + fib2, steps + 1

def fibonacci_iterative(n):
    if n <= 1:
        return n
    fib = [0, 1]
    steps = 0
    for i in range(2, n + 1):
        fib.append(fib[i - 1] + fib[i - 2])
        steps += 1
    return fib[n], steps

def main():
    n = int(input("Enter the value of n: "))
    recursive_result, recursive_steps = fibonacci_recursive(n, 0)
    iterative_result, iterative_steps = fibonacci_iterative(n)

    print(f"Fibonacci number using recursion for n = {n}: {recursive_result}")
    print(f"Steps required for recursion: {recursive_steps}")
    print(f"Fibonacci number using iteration for n = {n}: {iterative_result}")
    print(f"Steps required for iteration: {iterative_steps}")

if __name__ == "__main__":
    main()
