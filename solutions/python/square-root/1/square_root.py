def square_root(number):
    n = int(number)
    x = True
    low = 1
    high = n
    while x is True:
        mid = (low + high) // 2
        if mid * mid == n:
            x = False
            return mid
        elif mid * mid < n:
            low = mid
        else:
            high = mid
