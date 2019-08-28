
if __name__ == '__main__':
    a = []
    n = 4
    for _ in range(n):
        a.append(list(map(int, input().rstrip().split())))

    max = -9 * 7

    for i in range(n):
        for j in range(n):
            if j + 2 < n and i + 2 < n:
                result = a[i][j] + a[i][j + 1] + a[i][j + 2] + a[i + 1][j + 1] + a[i + 2][j] + a[i + 2][
                    j + 1] + a[i + 2][j + 2]
                if result > max:
                    max = result

    print(max)
"""
#take user input
    for r in range(n):
        a_t= []
        for c in range(n):
            a_t.append(int(input()))
        a.append(a_t)
    for r in range(n):
        for c in range(n):
            print(matrix[r][c], end =" ")
        print()
"""
