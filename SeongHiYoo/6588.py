import sys

def makePrime():
    max_num = 1000000
    prime_matrix = [False, False] + [True]*(max_num-1)

    for num in range(2, max_num+1):
        if prime_matrix[num]:
            for num2 in range(num*2, max_num+1, num):
                prime_matrix[num2] = False
    return prime_matrix

def findNum(prime_matrix,find_num): 
    for num in range(3,len(prime_matrix)):
        if prime_matrix[num] and ((prime_matrix[num]%2) != 0):
            check_num = find_num - num
            if prime_matrix[check_num] and (check_num %2 != 0):
                print("{} = {} + {}".format(find_num,num,check_num))
                break
        
if __name__ == "__main__":
    matrix_pr = makePrime()
    while True:
        N = int(sys.stdin.readline())
        if N == 0:
            break
        else:
            findNum(matrix_pr, N)
