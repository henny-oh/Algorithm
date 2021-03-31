import sys

if __name__ == "__main__":
    A,B,C = map(int, sys.stdin.readline().split())
    
    print((A+B)%C, end= "\n")
    print(((A%C) + (B%C))%C, end = "\n")
    print((A*B)%C, end = "\n")
    print(((A%C)*(B%C))%C, end = "\n")