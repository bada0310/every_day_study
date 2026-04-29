# import sys
# input = sys.stdin.readline
n = int(input())
if n == 1:
    print(5)
else:
    total_sum = sum(3 * i - 1 for i in range(1, n))
    print((5 * n +total_sum)%45678)

