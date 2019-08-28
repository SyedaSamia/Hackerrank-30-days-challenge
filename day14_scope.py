import itertools
class Difference:
    def __init__(self, a):
        self.__elements = a
        self. maximumDifference = 0


    def computeDifference(self):

        for i in range(len(a)):
            for j in range(i+1,len(a)):
                if (abs(a[i] - a[j]) > self.maximumDifference):
                    self.maximumDifference = abs(a[i] - a[j])

        return self.maximumDifference

    """
        def computeDifference(self):

        for i,j in itertools.combinations(a,2):
            if (abs(i-j) > self.maximumDifference):
                self.maximumDifference = abs(i-j)
        return self.maximumDifference

    """

if __name__ == '__main__':
    _ = input()
    a = [int(e) for e in input().split(' ')]

    d = Difference(a)
    d.computeDifference()

    print(d.maximumDifference)