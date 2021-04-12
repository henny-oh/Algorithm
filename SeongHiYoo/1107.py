import sys

def findMinMove(num, us_list):
    plus_num = 1
    minus_num = 1
    use_plus = 0
    use_minus = 0
    check_en_min = False
    check_en_plus = False
    int_num = int(num)
    for i in range(int_num+1, 10):
        if str(i) in us_list:
            use_plus = i
            check_en_plus = True
            break
        else:
            plus_num +=1
    for j in range(int_num-1, -1, -1):
        if str(j) in us_list:
            use_minus = j
            check_en_min = True
            break
        else:
            minus_num +=1
    if check_en_min and check_en_plus:
        if plus_num > minus_num:
            return use_minus
        else:
            return use_plus
    else:
        if check_en_min:
            return use_minus
        else:
            return use_plus


def UpDown(curr, ch_num):
    cu = int(curr)
    ch = int(ch_num)

    if cu> ch:
        return cu-ch
    else:
        return ch- cu

if __name__ == "__main__":
    curr = '100'
    ch_num = sys.stdin.readline().split("\n")[0]
    unus_num = int(sys.stdin.readline())
    if unus_num != 0:
        unus_list = sys.stdin.readline().split()
    us_list = []
    if unus_num!= 0:
        us_list = [str(num) for num in range(0, 10) if str(num) not in unus_list ] 
    else:
        us_list = [str(num) for num in range(0, 10)]
    makeNum = ''
    move_count = 0
    Up = False
    Down = False
    countUpdown = UpDown(curr, ch_num)

    if len(us_list) == 0:
        print(countUpdown)
    else:
        if len(curr) < countUpdown:
            for num in ch_num:
                if num in us_list:

                    move_count += 1
                    makeNum += num
                else: 
                    minNum= findMinMove(num, us_list)
                    makeNum += str(minNum)
                    move_count +=1
                    if minNum > int(num):
                        Up= True
                        break
                    else:
                        Down = True
                        break
            if not Up or not Down:
                if len(makeNum) != len(ch_num):
                    if Up:
                        for _ in range(len(makeNum)+1, len(ch_num)):
                            makeNum += us_list[0]
                            move_count +=1
                    else:
                        for _ in range(len(makeNum)+1, len(ch_num)):
                            makeNum += us_list[1]
                            move_count +=1 
    
            if makeNum == ch_num:
                print(move_count)
            else:
                restCount = UpDown(makeNum ,ch_num)
                print(move_count + restCount)
        else:
            print(countUpdown)


