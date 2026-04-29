T = int(input())
for t in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    min_val = 10000
    best_idx = 0
    for i in range(1, N):
        a = sum(arr[0:i])
        b = sum(arr[i:])
        diff = abs(a - b)
        if diff < min_val:
            min_val = diff
            best_idx = i
    print(f"#{t} {best_idx} {min_val}")


               
