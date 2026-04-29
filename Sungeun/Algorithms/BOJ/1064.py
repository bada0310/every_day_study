def distance(a, b):
    return ((a[0]-b[0])**2 + (a[1]-b[1])**2)**0.5 
# 점들간의 거리를 구하는 내용은 함수로 구현해도 될거 같아서 함수로 구현 

# 입력 받기
try:
    nodes = list(map(int, input().split()))
    graph = [[nodes[i], nodes[i+1]] for i in range(0, 6, 2)]
    # 점들이 한직선상에 존재하면 평행사변형을 만들지 못함 -> 그래서 -1 을 프린트 
    dx1, dy1 = graph[1][0] - graph[0][0], graph[1][1] - graph[0][1] 
    dx2, dy2 = graph[2][0] - graph[1][0], graph[2][1] - graph[1][1]

    if dy1 * dx2 == dy2 * dx1:
        print(-1.0) 
    else:
        len_12 = distance(graph[0], graph[1])
        len_23 = distance(graph[1], graph[2])
        len_13 = distance(graph[0], graph[2])

    # 둘레 구하기 
        cirs = [
            2 * (len_12 + len_23),
            2 * (len_23 + len_13),
            2 * (len_12 + len_13)
        ]
        # 둘레의 차이 구하기 
        print(max(cirs) - min(cirs))

except ZeroDivisionError: # 예외처리 분모가 0 이 되는 경우 
    print(-1.0)
except Exception:
    pass