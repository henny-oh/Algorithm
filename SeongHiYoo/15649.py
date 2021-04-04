import sys
from itertools import permutations
if __name__ == '__main__':
    N, M = list(map(int, sys.stdin.readline().split()))
    num_list = [num for num in range(1, N+1)]
    results = list(permutations(num_list, M))
    for result in results:
        for cos in result:
            print(cos, end=" ")
        print('')
    
    