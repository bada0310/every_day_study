# 11573
T =int(input())
for t in range(1, T+1):
    N =int(input()) # 정수의 갯수
    arr= list(map(int,input().split()))
    stack = []
    for i in range(N):
        if arr[i] != 0:
            stack.append(arr[i])
        if arr[i] == 0:
            stack.pop()
        
    print(f"#{t} {sum(stack)}")