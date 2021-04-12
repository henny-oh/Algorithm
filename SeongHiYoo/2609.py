from math import gcd
import sys
if __name__ == "__main__":
    num1, num2 = list(map(int, sys.stdin.readline().split()))

    re1 = gcd(num1,num2)
    print(re1)
    print((num1*num2)//re1)