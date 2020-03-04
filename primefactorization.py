import sys


class primeFactorization:

    # Initialize the variables. The initial factor is set to 1, which will be incremented.
    def __init__(self, n):
        self.number = n
        self.multiple = 0
        self.factor = 1
        self.factorization = []

    # Returns true if there is a next prime. Sets the multiplicity to 0, and updates the factor.
    def getnextprime(self):
        for i in range(self.factor, self.number):
            if self.number % (i + 1) == 0:
                self.factor = i + 1
                self.multiple = 0
                return True
        return False

    # Print the prime factors for the CL Args in the selected format. Factors and their multiplicities are pairs of
    # integers appended to the list.
    def printfactors(self, x):
        print('PrimeFactorization(%s): %s' % (x, self.factorization))

    # Set the multiplicity of the current factor.
    def getmultiple(self):
        while self.number % self.factor == 0:
            self.multiple = self.multiple + 1
            self.number = self.number // self.factor

    # Get all the prime factors and their multiples from the CL Args
    def getprimefactors(self):
        while self.getnextprime():
            self.getmultiple()
            self.factorization.append([self.factor, self.multiple])


if __name__ == '__main__':

    # This expects CL arguments of integers without separators. Currently, there is no error handling.
    if len(sys.argv) > 1:
        for x in (1, len(sys.argv) - 1):
            x = int(sys.argv[x])
            pf = primeFactorization(x)
            pf.getprimefactors()
            pf.printfactors(x)

    else:
        print('command line args required!!!')
