from itertools import combinations
if __name__ == "__main__":
    num_list = []
    result = []
    for _ in range(0, 9):
        num_list.append(int(input()))
    
    combin_list = list(combinations(num_list,7))
    for num in combin_list:
        if sum(num) == 100:
            result = num
            break

    sort_result = sorted(result)
    for res in sort_result:
        print(res, end="\n")
    

    