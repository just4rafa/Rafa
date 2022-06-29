
def fibonacci(n):
    """Return the `n` th
    Fibonacci number, for
    positive `n`."""
    if 0 <= n <= 1:
        return n
    
    n_minus1, n_minus2  = 1, 0
    
    result = None
    for f in range(n - 1):
        result = n_minus1 + n_minus2
        n_minus2 = n_minus1
        n_minus1 = result
        
    return result
   
f = int(input("Enter fibonancci number: "))
for i in range(f + 1):
    if i == f:
        print("-" * 6)
    print(i, fibonacci(i))
    if i == f:
        print("-" * 6)
        
