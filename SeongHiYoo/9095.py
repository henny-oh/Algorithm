import sys

def make_num():
    num_list = [0 for _ in range(0, 11)] 
    num_list[0] = 0
    num_list[1] = 1
    num_list[2] = 2
    num_list[3] = 4
    for num in range(4, 11):
        num_list[num] = num_list[num-1] + num_list[num-2]  + num_list[num-3]
    return num_list

if __name__ == '__main__':
    T = int(sys.stdin.readline())
    num_list = make_num()

    for _ in range(0, T):
        num = int(sys.stdin.readline())
        print(num_list[num])    
        