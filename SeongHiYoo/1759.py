import sys
from itertools import combinations
def find_coll(string_list):
    coll = ['a', 'e', 'i', 'o', 'u']
    str_coll = []
    for st in string_list:
        if st in coll:
            str_coll.append(st)
    return sorted(str_coll)

def make_string(str_coll, cons, L):
    con_list = {}
    coll_list = {}
    for num in range(2, L):
        con_list[num] = list(combinations(cons, num))
    
    for num in range(1, L-1):
        coll_list[num] = list(combinations(str_coll, num))
    result = []
    for key in coll_list.keys():
        con_num = L- key
        if con_num in con_list.keys():
            for coll in coll_list[key]:
                for con in con_list[con_num]:
                    result.append(list(con+coll))
    sort_result = []
   
    for res in result:
        sort_res = sorted(res)
        sort_result.append(''.join(sort_res))
    sort_res = sorted(sort_result)
    for re in sort_res:
        print(re) 



if __name__ == "__main__":
    coll = ['a', 'e', 'i', 'o', 'u']
    L, C = list(map(int, sys.stdin.readline().split()))
    string_list = list(sys.stdin.readline().split())
    str_coll = find_coll(string_list)
    cons = list(set(string_list) - set(str_coll))
    cons.sort()
    make_string(str_coll, cons, L)
    