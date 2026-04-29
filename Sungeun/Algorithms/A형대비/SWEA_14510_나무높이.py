# swea_14510_나무 높이 
# 홀수날 +1 짝수날 +2 (물을 안주는 날도 존재 O )
# 모든 나무의  키가 가장 큰 나무의 키와 같아지는 순간 
# greedy

T = int(input())
for tc in range(1,T+1):
    N  = int(input())
    arr = list(map(int,input().split()))
     
    top_tree = max(arr)
    odd = 0
    even = 0 
     
    for i in range(N):
        diff = top_tree - arr[i]
        if diff > 0: 
            odd += diff%2
            even += diff//2
    while even > odd+1:
        even -= 1
        odd += 2
    if odd > even:
        time = odd * 2 - 1
    else:
        time = even * 2
         
    print(f'#{tc}',time)
