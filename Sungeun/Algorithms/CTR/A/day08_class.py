# 중복 순열 만들기 
K, N = map(int, input().split())

# Please write your code here.
arr = [i for i in range(1,K+1)]

path = [0]*N

def perm(depth):
    if depth == N:
        print(*path)
        return
    
    for i in range(K):
        path[depth]=arr[i]

        perm(depth+1)
perm(0)

# K, N = map(int, input().split())

# def choose(picked):
#     # "len(picked)번째를 골라야 하는 상황"

#     if len(picked) == N:
#         print(" ".join(map(str, picked)))
#         return

#     for i in range(1, K + 1):
#         picked.append(i)
#         choose(picked)
#         picked.pop()

# choose([])

