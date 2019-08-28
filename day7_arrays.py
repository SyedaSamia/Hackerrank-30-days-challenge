if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().rstrip().split()))
    arr2 =map(str,arr[::-1])
    print(" ".join(arr2))

'''strip() removes whitespace and newlines from the ends of that string and returns the result.

split() splits that string into a list of parts. If you don't give any arguments, it splits on any whitespace.

map() takes two arguments: A function and a list. In this case the function is int, and the list is the one from above.
 It executes the function once on each thing in the list, and returns the result. In this casse the function is int,
 which converts its argument to an
 integer (a whole number).

 arr[::-1] Negative values also work to make a copy of the same list in reverse order:
 '''

