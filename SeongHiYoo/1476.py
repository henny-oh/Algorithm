import sys

if __name__ == '__main__':
    E, S, M = list(map(int, sys.stdin.readline().split()))

    test_e = 1
    test_s = 1
    test_m = 1
    day = 1
    while not ((test_e == E) and  (test_s == S) and (test_m == M)):
        test_e +=1
        test_s +=1
        test_m +=1
        day +=1
        if  test_e == 16:
            test_e = 1
        if test_s == 29:
            test_s = 1
        if test_m == 20:
            test_m = 1
    print(day)

    