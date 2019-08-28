if __name__ == "__main__":
    t=int(input())
    for i in range(0,t):
        s = input()
        for j in range(0, len(s)):
            if j%2==0:
                print(s[j], end='')
        print(" ", end='')
        for j in range(0, len(s)):
            if j%2 !=0:
                print(s[j], end='')
        print(" ")