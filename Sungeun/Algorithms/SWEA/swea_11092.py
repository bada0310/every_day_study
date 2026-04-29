T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = list(map(int,input().split()))
    max_val = max(arr)
    min_val = min(arr)
    answer_max = []
    answer_min = []
    for i in range(N):
        if arr[i] == max_val:
            answer_max.append(i)
        if arr[i] == min_val:
            answer_min.append(i)
    
    answer = abs(max(answer_max) - min(answer_min))
    print(f"#{t} {answer}")
    