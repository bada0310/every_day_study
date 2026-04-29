# 2846
n = int(input()) # 5

lst_road = list(map(int, input().split()))  # 1 2 1 4 6
# [1,2,1,4,6]
max_high = 0
high = 0 
for i in range(n-1):
    if lst_road[i] < lst_road[i+1]:
		    # 오르막 이라면: 차이만큼 +추가 
        high += lst_road[i+1]-lst_road[i]
    else:
		    # 내리막을 만나면, 현재까지의 오르막 중 최댓값 갱신 후 초기화 
        max_high =max(max_high, high)
        high = 0 
# 마지막 구간이 오르막으로 끝났을 경우를 위해 
max_high =max(max_high, high)
print(max_high)