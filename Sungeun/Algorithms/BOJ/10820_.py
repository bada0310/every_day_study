N, K = map(int, input().split())
medals = []
for n in range(N) :
    medal = list(map(int, input().split()))
    medals.append(medal)

medals.sort(key = lambda x: (x[1], x[2], x[3]), reverse=True)

for i in range(N) :
    if medals[i][0] == K :
        answer = i + 1
        break

# 앞에 국가가 동점이면 등수 하나씩 올리기
# answer : 등수
while  answer > 1 :
    if medals[answer - 2][1:] == medals[answer - 1][1:] :
        answer -= 1
    else :
        break

print(answer)