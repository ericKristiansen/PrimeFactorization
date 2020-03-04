import sys


class primeFactorization:

    def __init__(self, n):
        self.number = n
        self.multiple = 0
        self.factor = 1
        self.factorization = []

    def getnextprime(self):
        for i in range(self.factor, self.number):
            if self.number % (i + 1) == 0:
                self.factor = i + 1
                self.multiple = 0
                return True
        return False

    def printfactors(self, x):
        print('PrimeFactorization(%s): %s' % (x, self.factorization))

    def getmultiple(self):
        while self.number % self.factor == 0:
            self.multiple = self.multiple + 1
            self.number = self.number // self.factor

    # A function to print all prime factors of
    # a given number n
    def getprimefactors(self):
        while self.getnextprime():
            self.getmultiple()
            self.factorization.append([self.factor, self.multiple])


if __name__ == '__main__':

    if len(sys.argv) > 1:
        for x in (1, len(sys.argv) - 1):
            x = int(sys.argv[x])
            pf = primeFactorization(x)
            pf.getprimefactors()
            pf.printfactors(x)

    else:
        print('command line args required!!!')
