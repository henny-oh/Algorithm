import sys


def isPrime():
    max_num = 1000
    a = [False,False] + [True] * (max_num-1)

    for num in range(2, max_num+1):
        if a[num]:
            for j in range(2*num, max_num+1, num):
                a[j] = False
    return a        
if __name__ == "__main__":
    result = 0
    N = int(sys.stdin.readline())
    num_list = list(map(int, sys.stdin.readline().split()))
    prim_matrix = isPrime()

    for num in num_list:
        if prim_matrix[num]:
            result += 1
    print(result)
