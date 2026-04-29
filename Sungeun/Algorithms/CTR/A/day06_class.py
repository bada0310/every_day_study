n, r, c = map(int, input().split())
a = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    row = list(map(int, input().split()))
    for j in range(1, n + 1):
        a[i][j] = row[j - 1]

def in_range(y, x):
    return 1 <= y <= n and 1 <= x <= n

drs = [-1, 1, 1, 0]
dcs = [0, 0, -1, 1]

print(a[r][c], end=" ")

while True:
    nr, nc = r, c

    # 상 하 좌 우를 탐색
    for dr, dc in zip(drs, dcs):
        tr = r + dr
        tc = c + dc

        # 격자 밖이면 패스
        if not in_range(tr, tc): 
            continue

        # 현재 위치보다 더 작은 경우 패스
        if a[tr][tc] <= a[r][c]:
            continue

        # 아직 값이 바뀌지 않았다면
        if r == nr and c == nc:
            nr = tr
            nc = tc

    if r == nr and c == nc:
        break

    r, c = nr, nc
    print(a[r][c], end=" ")