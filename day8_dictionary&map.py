
if __name__ == '__main__':
    n = int(input())
    phone_book = dict()
    for i in range(0,n):
        data = input().split()
        name = str(data[0])
        phone_no = int(data[1])
        phone_book[name] = phone_no
    while True:
        try:
            search_name = str(input())
                #search_name = input()
            if search_name in phone_book:
                search_number = phone_book[search_name]
                print(search_name + "=" + str(search_number))
            else:
                print("Not found")


        except EOFError:
            break

