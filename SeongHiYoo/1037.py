import sys

if __name__ == "__main__":
    measure_num = int(sys.stdin.readline())
    measures = list(map(int, sys.stdin.readline().split()))
    measures.sort()
    if len(measures) < 2:
        print(measures[0]*measures[0])
    else:
        print(measures[0]*measures[-1])