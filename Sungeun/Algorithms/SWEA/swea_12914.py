# 전제 조전: 이진 트리 
# 노드 위치들 list 형식으로 주어짐
# sub_tree count  = 나를 기준으로 한! 왼쪽 + 오른쪽 + 나(1)
def count_node(node, left, right):
    if node == 0:
        return 0
    return count_node(left[node], left, right)+ count_node(right[node], left,right) + 1

T = int(input())
for t in range(1, T+1):
    E, N  = map(int,input().split())
    data = list(map(int, input().split()))
    left = [0]*(E+2) # E +2 인 이유 node = edge + 1 and 0 idx (+1)
    right = [0]*(E+2)

    for i in range(0, len(data), 2):
        parent, child = data[i], data[i+1]
        if left[parent] == 0:
            left[parent] = child
        else:
            right[parent] = child
    result = count_node(N, left, right)
    print(f'#{t}',result)