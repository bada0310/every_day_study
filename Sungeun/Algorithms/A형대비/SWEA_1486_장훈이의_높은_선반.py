# +) 1486_장훈이의 높은 선반 
def comb(idx, sum_val):
    global min_val
    if sum_val >= S:
        val = sum_val - S
        if val < min_val:
            min_val = val
        return
    if idx == N:
        return
    comb(idx+1, sum_val+arr[idx]) # 선택했을때? 
    comb(idx+1, sum_val) # 선택 안했을때 
T = int(input())
for tc in range(1,T+1):
    N, B = map(int,input().split())
    arr = list(map(int,input().split()))
    S = sum(arr)
    min_val = float('inf')
    comb(0,0)
    print(f'#{tc}',min_val)
