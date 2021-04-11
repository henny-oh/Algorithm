a, b, c = map(int, input().split())
print((a+b)%c)
print((a%c+b%c)%c)
print((a*b)%c)
print((a%c*b%c)%c) //세 수 A, B, C가 주어졌을 때, 위의 네 가지 값을 구하는 프로그램