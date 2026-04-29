# https://www.acmicpc.net/problem/2851
mushrooms = [int(input()) for _ in range(10)]
total = 0
answer = 0
for sum_mushroom in mushrooms:
    total += sum_mushroom
    if abs(100-total) <= abs(100-answer):
        answer = total
    print(answer)
    
# 이전 포인트까지의 합 # 그 후포인트 까지의 합
mushrooms = [int(input().strip())for _ in range(10)]
point = 0
for m in mushrooms:
    prepoint = point
    point += m

    if point >= 100:
        gapov = point - 100
        gapud = 100 - prepoint

        if gapov <= gapud:
            print(point)
        else:
            print(prepoint)
        break

else:
    print(point)