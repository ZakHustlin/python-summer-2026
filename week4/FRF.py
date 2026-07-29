is_positive = lambda x: x > 0
is_even = lambda x: x % 2 == 0


def make_validator(rules):
    
    def check(value):
        for rule in rules:
            if not rule(value):
                return False
        return True
    return check

check = make_validator([is_positive, is_even])


print(check(4))     # → True  (positive and even)
print(check(-2))    # → False (not positive)
print(check(3))     # → False (not even)
print(check(0))     # → False (not positive)