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

# 처음에 생각하지 못했던 오류? 
# start 인자의 필요성 
#  우리가 이미 정렬을 했기 떄문에 순서대로 뽑을 거 같지만 
# 만약  K (0이 아닌)번쨰의 문자부터 시작하게 된다면 visited 를 check 할때 
# 0 번째 부터하기 때문에, 정렬되지 않은 순서로 K 번째 -> 0번째 -> 1번째 이렇게 순서대로 나열된다.
# 이때 사실은 우리는 k 번쨰 이후의 원소들만 check 해서 넣어야 상관이 없다. 
# start 를 통해서 '무조건 오른쪽에서만 뽑아'를 통해 따로 정렬할 필요도 set 으로 묶을 필요도 없앤다. 
# 