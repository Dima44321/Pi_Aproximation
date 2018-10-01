import random, math

#check if numbers are coprime
def isCoprime(a,b):
    if math.gcd(a,b) == 1:
        return 1
    else:
        return 0

#gather inputs
cycles = int(input("Cycles: "))
upperBound = int(input("Upper Bound: "))
counter = 0

#count the number of coprime and non-coprime pairs
for i in range(cycles):
    a = random.randint(1, upperBound)
    b = random.randint(1, upperBound)
    counter = counter + isCoprime(a,b)

#calculate pi
x = counter/cycles
pi = math.sqrt(6/x)
print("Pi: " + str(pi))
