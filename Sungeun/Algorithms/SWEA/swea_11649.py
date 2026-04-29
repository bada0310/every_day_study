T = int(input())

for t in range(1, T+1):
    N, M = map(int,input().split())
    arr = list(input().split())
    target = M%N
    # for i in range(M):
    #     last_one = arr[0]
    #     arr.append(last_one)
    print(f"#{t}",arr[target])