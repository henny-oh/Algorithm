import sys
def find_row(candy_list, N, row1, row2):
    max_result = 0
    escape_max = False
    for num in range(row1, row2+1):
        count_max = 1
        for num1 in range(1, N):
            if candy_list[num1][num] == candy_list[num1-1][num]:
                count_max +=1
            else:
                max_result = max(max_result, count_max)
                if max_result == N:
                    escape_max = True
                    break
                count_max = 1
        if escape_max:
            break
    return max_result
    
        
def find_column(candy_list,N, col1, col2):
    max_result = 0
    escape_max = False
    for num in range(col1, col2+1):
        count_max = 1;
        for num1 in range(1, N):
            if candy_list[num][num1] == candy_list[num][num1 -1]:
                count_max +=1
            else:
                max_result = max(max_result,count_max)
                if max_result == N:
                    escape_max = True
                    break
                count_max = 1
        if escape_max:
            break
    return max_result

if __name__ == "__main__":
    N = int(sys.stdin.readline())
    candy_list = [list(map(str, input())) for _ in range(N)]

    max_candy = 0
    for index in range(0, N):
        for num in range(0, N-1):
            candy_list[index][num], candy_list[index][num+1] = candy_list[index][num+1],candy_list[index][num]
            row_count = find_row(candy_list, N, num, num+1)
            column_count = find_column(candy_list, N, index, index)
            candy_list[index][num], candy_list[index][num+1] = candy_list[index][num+1],candy_list[index][num]
            max_candy = max(row_count, column_count, max_candy)
            if index != (N-1):
                candy_list[index][num], candy_list[index+1][num]= candy_list[index+1][num], candy_list[index][num]
                row_count = find_row(candy_list, N, num, num)
                column_count = find_column(candy_list, N, index, index+1)
                candy_list[index][num], candy_list[index+1][num]= candy_list[index+1][num], candy_list[index][num]
                max_candy = max(row_count, column_count, max_candy)
            if max_candy == N:
                break
            print("index : " + str(index) +"num:"+str(num) + "max_candy:"+str(max_candy), end= "\n")
    print(max_candy)
           
    


        
    
