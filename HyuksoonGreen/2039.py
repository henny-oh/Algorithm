
lst = []
summ = 0
nine = 9
for i in range(nine):
    N = int(input())
    lst.append(N)
summ = sum(lst)
for i in range (8):
    for j in range(i+1, nine):
        if (summ - lst[i]-lst[j] == 100):
            one = lst[i]
            two = lst[j]
lst.remove(one)
lst.remove(two)
lst.sort()
for i in lst:
  print(i)