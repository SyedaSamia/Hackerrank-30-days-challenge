if __name__ == '__main__':
    n = int(input())
    one = 0
    max_one = 0


    while(n> 0):
        r = int(n/2)
        c = n - (2 * r)
        n = r
        if c == 1:
            one = one +1
            if(one>max_one):
                max_one = max_one +1
        else:
            one = 0



    print(max_one)