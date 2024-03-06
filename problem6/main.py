def is_prima(N):
    # your code here
    if N <= 1:
        return False
    for i in range (2, N):
        if N % i == 0:
            return False
    return True

def full_prima(N):
    if N <= 0:
        return False
    
    while N > 0:
        digit = N % 10
        if not is_prima(digit):
            return False
        N //= 10
    return True


if __name__ == '__main__':
    print(full_prima(2)) # True
    print(full_prima(3)) # True
    print(full_prima(11)) # False
    print(full_prima(13)) # False
    print(full_prima(23)) # True
    print(full_prima(29)) # False
    print(full_prima(37)) # True
    print(full_prima(41)) # False
    print(full_prima(43)) # False
    print(full_prima(53)) # True