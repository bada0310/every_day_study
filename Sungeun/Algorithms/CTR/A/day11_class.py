https://www.codetree.ai/ko/external-connection/classes/177/lectures/1769/curated-cards/intro-n-choose-m/description

N, M = map(int, input().split())
arr = [i for i in range(1,N+1)]
visited = [False]*(N+1)
result = []
# Please write your code here.
def comb(depth,start):
    if depth == M:
 
        print(*result)
        return

    for i in range(start,N):
        if  not visited[i]:
            visited[i] = True
            result.append(arr[i])

            comb(depth+1, i+1)
            result.pop()
            visited[i] = False

comb(0,0)



# N = int(input())
# a1, b1, c1 = map(int, input().split())
# a2, b2, c2 = map(int, input().split())

# # n1과 n2 사이의 거리가 2 이내인지 확인하는 함수
# def is_near(n1, n2):
#            # 시계방향                # 반시계방향
#     return (abs(n1 - n2) <= 2) or (abs(n1 - n2) >= N - 2)

# open_cnt = 0
# for i in range(1, N+1):
#     for j in range(1, N+1):
#         for k in range(1, N+1):
#             # 모든 자리에 대해 첫 번째 조합과 거리가 2 이내이거나
#             lock1 = is_near(i, a1) and is_near(j, b1) and is_near(k, c1)

#             # 모든 자리에 대해 두 번째 조합과 거리가 2 이내에 있으면
#             lock2 = is_near(i, a2) and is_near(j, b2) and is_near(k, c2)
            
#             if lock1 or lock2:
#                 open_cnt += 1

# print(open_cnt)