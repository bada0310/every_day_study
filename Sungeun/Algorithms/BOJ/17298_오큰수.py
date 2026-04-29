N = int(input())
arr  = list(map(int,input().split()))
result = []
for i in range(N):
    static = arr[i]
    flag = False
    for right in range(i+1,N):
        if arr[right] > static:
            result.append(arr[right])
            flag = True
            break
    if not flag:
        result.append(-1)

print(*result)

N = int(input())
arr  = list(map(int,input().split()))
result = [-1]*N
stack = []
for i in range(N):
    while stack and arr[stack[-1]] < arr[i]:
        idx =stack.pop()
        result[idx] = arr[i]
    stack.append(i)
print(*result)