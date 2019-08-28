
if __name__ == '__main__':
    x = list()
    t = int(input())
    for i in range(t):
        x.append(input())
    x.sort(key=lambda i: (len(i), i))

    for i in x:
        print(i)

