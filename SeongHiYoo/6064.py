import sys

if __name__ == "__main__":
    N = int(sys.stdin.readline())
    for _ in range(0, N):
        day_count = 1
        M,N,x,y = list(map(int,sys.stdin.readline().split()))
        answer = 0
        x_days = 0
        y_days = 0
        check_true = True
        if x> y:
            x_days = x -y
            while x_days % N != 0:
                x_days += M
                if x_days > (M*N):
                
                    check_true = False
                    break
            answer = x_days+y
        else:
            y_days =  y -x
            while y_days % M != 0:
                y_days += N
                if y_days > (M*N):
                    check_true = False
                    break
            answer = y_days+x
        if check_true:
            print(answer)
        else:
            print(-1)
        
       