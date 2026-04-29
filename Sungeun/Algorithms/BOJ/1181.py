arr = set()
N = int(input())
for _ in range(N):
    word = input()
    arr.add((len(word), word))
arr = sorted(arr)
for i, j in arr:
    print(j)

# 이어서 질문할 내용
# 왜 set() 자료 구조는 sort() 함수가 적용되지 않는가?
# 꼭 sorted() 해야 하는가? 
