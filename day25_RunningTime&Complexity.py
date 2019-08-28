def is_prime(x):
    if x == 0 or x == 1:
        return False
    else:
        for j in range(2, int(x**0.5)+1):
            if x % j == 0:
                return False
        return True


if __name__ == '__main__':

    n = int(input())
    for i in range(n):
        x = int(input())
        if is_prime(x):
            print("Prime")
        else:
            print("Not prime")

