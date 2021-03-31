if __name__ == "__main__":
    while True:
        try:
            n = int(input())
            if ((n%2) == 0) and ((n%5) == 0):
                break
            one_str = '1'
            min_count = 1
            while (int(one_str) % n) != 0:
                one_str += '1'
                min_count +=1
            print(min_count)
        except EOFError:
            break