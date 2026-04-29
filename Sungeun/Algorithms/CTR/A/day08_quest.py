

N = int(input())
lines = [tuple(map(int,input().split())) for _ in range(N)]
lines.sort()
# Please write your code here.
picked = []
max_cnt = 0

def choose(start):
    global max_cnt
    # 기저 조건
    if len(picked) > max_cnt:
        max_cnt = len(picked)

    for i in range(start,N):
        if len(picked) > 0:
            prev_idx=picked[-1]
            if lines[prev_idx][1] >= lines[i][0]:
                continue
        picked.append(i)
        choose(i+1)
        picked.pop()
choose(0)
print(max_cnt)


# n = int(input())
# lines = [tuple(map(int, input().split()))]

# def is_valid(picked):
#     tmp = [0 for _ in range(n + 1)]

#     for l, r in picked:
#         for i in range(l, r + 1):
#             tmp[i] += 1

#     for i in range(n + 1):
#         if tmp[i] >= 2:
#             return False

#     return True

# def choose(picked, idx):
#     # idx번째를 고를 차례

#     # 종료조건
#     if idx == n:
#         if is_valid(picked):
#             return len(picked)
#         return 0

#     cnt = 0

#     # 고르거나
#     picked.append(lines[idx])
#     cnt = max(cnt, choose(picked, idx + 1))
#     picked.pop()

#     # 안고르거나
#     cnt = max(cnt, choose(picked, idx + 1))
#     picked.pop() 

#     return cnt

# print(choose([], 0))