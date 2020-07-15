cache = ['#']*10000

def fibonacci(n):
    
    if n in [0, 1]:
        return n
    if cache[n] != '#':
        return cache[n]
    else:
        a = fibonacci(n - 1) + fibonacci(n - 2)
        cache[n] = a
    return a