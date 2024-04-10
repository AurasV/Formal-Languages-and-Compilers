def fibonacci(n):
    fib_series = [0, 1]
    any(map(lambda _: fib_series.append(sum(fib_series[-2:])), range(2, n)))
    return fib_series[:n]

def main():
    n = int(input("Enter the number of Fibonacci numbers to generate: "))
    print("The Fibonacci series is:", fibonacci(n))

if __name__ == "__main__":
    main()

