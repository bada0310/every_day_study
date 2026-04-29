def comb(idx, sum_val):
    global min_val
    if sum_val >= S:
        val = sum_val - S # 무조건 S 보다 높다
        if val < min_val:
            min_val = val
            return
    if idx == N:
        return
    comb(idx+1,sum_val+arr[idx])
    comb(idx+1, sum_val)
T = int(input())

for tc in range(1,T+1):
    N, S = map(int,input().split())
    arr = list(map(int,input().split()))
    min_val = float('inf')
    comb(0,0)
    print(f'#{tc}',min_val)
