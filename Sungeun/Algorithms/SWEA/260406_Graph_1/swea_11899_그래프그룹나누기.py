def union_find(pairs):
    parent = {i: i for i in range(1,N+1)} # 대표자를 저장할 dict  # dict 로 만들어서 넣고 val 이없는 key 들중에 다른 

    for u, v in pairs:
        if u not in parent: parent[u] = u
        if v not in parent: parent[v] = v
    # 주장 찾기 
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]
    
    def union(a,b):
        rootA = find(a)
        rootB = find(b)

        if rootA != rootB: # 이미 같은 집합이면 pass, 아닐 경우에만 시도 
            if rootA < rootB:
                parent[rootB] =rootA
            else:
                parent[rootA] = rootB

    for u, v in pairs:
        union(u,v)

    # group 하기 
    groups = {}
    for node in parent:
        root = find(node)

        if root not in groups:
            groups[root] = []
        groups[root].append(node)
    return len(groups)

T = int(input())
for tc in range(1,T+1):
    N, M = map(int,input().split())
    nums= list(map(int,input().split()))
    pairs = [[nums[i], nums[i+1]] for i in range(0,M*2,2)]
    ans = union_find(pairs)
    print(f'#{tc}',ans)




