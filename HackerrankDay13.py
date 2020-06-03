class Difference:
    def __init__(self, a):
        self.__elements = a

    maximumDifference = 0

    # Add your code here
    def computeDifference(self):
        for i in range(len(self.__elements)):
            for j in range(i, len(self.__elements)):
                temp = abs(self.__elements[j] - self.__elements[i])
                if temp > self.maximumDifference:
                    self.maximumDifference = temp

            # End of Difference class


_ = input()
a = [int(e) for e in input().split(' ')]
d = Difference(a)
d.computeDifference()
print(d.maximumDifference)
