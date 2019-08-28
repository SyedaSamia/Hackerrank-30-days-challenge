
def func_bitwise(n,k):
    max = 0

    for i in range(1, n+1):
        for j in range(1, i):
            x = i & j
            if x > max and x < k:
                max = x
                if max == k-1:
                    return max

    return max

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        nk = input().split()
        n = int(nk[0])
        k = int(nk[1])

        print(func_bitwise(n,k))