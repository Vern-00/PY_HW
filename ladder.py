def my_steps(n):
    if n < 1 or n > 25:
        raise ValueError("input out of range (1-25)")
    if (n == 1):
        return 1
     if (n == 2):
        return 2
    return my_steps(n-2) + my_steps(n-1)