def egg_count(display_value):
    total = 0
    n = display_value
    while n > 0:
        if n % 2 == 1:
            total += 1
        n = n // 2
    return total
        
            
        
