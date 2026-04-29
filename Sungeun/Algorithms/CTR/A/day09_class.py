K, N = map(int, input().split())

# Please write your code here.

arr = [i for i in range(1, K+1)]
path= []
def perm():
    if len(path) == N:
        print(*path)
        return
    for i in range(K):
        if len(path) >= 2 and path[-1] == arr[i] and path[-2] == arr[i]:
            continue
        path.append(arr[i])
        perm()
        path.pop()

perm()