def fib(n: int) -> int: 
    if n == 0: 
        return 0
    elif n == 1 or n == 2:
        return 1
    elif n > 2: 
        a = 1 
        b = 1 
        for x in range(3, n + 1):
            c = a + b
            a, b = b, c
        return c

assert fib(1) == 1
assert fib(2) == 1
assert fib(3) == 2
assert fib(100) == 354224848179261915075