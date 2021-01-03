# Nth Fibonacci number

# Solution one
# Running time O(n) space 0(1)

def getNthFib1(n):
    a = 0
    b = 1
    while n:
        nth = a
        a, b = b, a + b
        n -= 1

    return nth


# Solution two
# Running time O(2^n) space 0(n)
def getNthFib2(n):
    if n == 2:
        return 1
    elif n == 1:
        return 0
    else:
        return getNthFib2(n - 1) + getNthFib2(n - 2)
