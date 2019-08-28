if __name__ == '__main__':

    S = input().strip()
    try:
        S2 = int(S)
        print(S2)
    except ValueError:
        print("Bad String")