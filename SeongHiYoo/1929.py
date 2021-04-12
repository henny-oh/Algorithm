import sys


def checkPrime(min_num, max_num):
    prime_matrix = [False, False] +[True]*(max_num-1)
    
    for num in range(2, max_num+1):
        if prime_matrix[num]:
            if (num >= min_num) and (num <= max_num):
                print(num)
            for num2 in range(num*2, max_num+1, num):
                prime_matrix[num2] = False
if __name__ == "__main__":
    min_num, max_num = list(map(int, sys.stdin.readline().split()))
    checkPrime(min_num, max_num)
