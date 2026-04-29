N, M = map(int,input().split())
arr = list(input().split())
arr.sort()
gather = ['a', 'e', 'i', 'o', 'u']
answer = []
visited = [False]*M

def dfs(depth, result, start):
    if depth == N:
        v_cnt = 0
        c_cnt = 0
        for k in result:
            if k in gather:
                v_cnt += 1
            else:
                c_cnt += 1
        if v_cnt >= 1 and c_cnt >= 2: # 모음 1개 이상 자음 2개 이상 필수!! 
            answer.append("".join(result))
        return
    
    for i in range(start, M):
        if not visited[i]:
            visited[i] = True
            result.append(arr[i]) 
            
            dfs(depth+1, result, i+1)
            visited[i] = False # 백트래킹!
            result.pop() # 백트래킹!
            
dfs(0, [], 0)
for i in range(len(answer)):
    print(answer[i])