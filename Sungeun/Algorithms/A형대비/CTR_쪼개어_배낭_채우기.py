# CTR_ 쪼개어 배낭 채우기
# 가격 /무게 했을 때 값이 큰 순서대로 채우는게 좋다
N, M = map(int, input().split()) # 보석의 갯수 # 가방의 크기 
arr = []
max_val = 0 
for _ in range(N):
    w, v = map(int,input().split())
    arr.append((v/w,w,v))

arr.sort(reverse=True)

for ratio, weight, value in arr:
    if M >= weight:
        max_val += value
        M -= weight
    else:
        max_val += M * ratio
        break

print(f'{max_val:.3f}')