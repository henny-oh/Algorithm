import sys

if __name__ == '__main__':
    N = int(sys.stdin.readline())
    cost = N
    num_list = [num for num in range(2, N+1)]
    for num in num_list:
        val = N//num
        cost += (num)*val
    print(cost)