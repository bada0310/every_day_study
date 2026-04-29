import sys
n, m = map(int, sys.stdin.readline().split()) # 1. 첫 번째 줄 읽기 (N, M)
score = list(map(int, sys.stdin.readline().split())) # 2. 두 번째 줄 읽기 (배점)
result = [] 

for _ in range(m):
    line =sys.stdin.readline().split()
    stu_id = int(line[0]) # 이름은 일단 그대로 두고, 결과는 O/X만 추출
    answer = line[1:]

    total_score = 0
    for i in range(n):
        if answer[i] == 'O':
            total_score += score[i]
    result.append((stu_id, total_score)) # 첫 번째 학생이거나, 점수가 더 높을 때 갱신
 # 최종 결과 출력
result.sort(key=lambda x: (-x[1], x[0]))
print(result[0][0], result[0][1])