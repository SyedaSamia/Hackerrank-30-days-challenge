if __name__ == '__main__':
    N = int(input())

    for N_itr in range(N):
        firstNameEmailID = input().split()

        firstName = firstNameEmailID[0]

        emailID = firstNameEmailID[1]
        if "@gmail" in emailID:
            list.append(firstName)

    list.sort()
    for i in list:
        print(i)
