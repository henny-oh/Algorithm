import sys
import itertools

def find_dup(cos_list):
    return len(cos_list) != len(set(cos_list))
if __name__ == '__main__':
    N, M = list(map(int, sys.stdin.readline().split()))
    num_list = [num for num in range(1, N+1)]
    results = list(itertools.combinations(num_list, M))
    for result in results:
        if not find_dup(result):
            for cos in result:
                print(cos, end=' ')
        print('')
    
    