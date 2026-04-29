#2005 
T = int(input())

for t in range(1, T+1):
    N = int(input())
    numbers =[]
    temp = []
    print(f"#{t}")
    for i in range(N):
        numbers.append(1)
        temp.append(1)
        if i < 2:
            pass
        else:
            for j in range(1, len(numbers)-1):
                temp[j] = numbers[j-1] + numbers[j]
        for j in range(len(numbers)):
            numbers[j] = temp[j]
            print(str(numbers[j]) + " ", end="")
        print("")
# 파스칼의 삼각형 (top-down = DP , bottom-up = for문 )
# 흔히 Top-Down과 Bottom-Up이 방식과 장단점에서 차이 점이 있는데,
# 위의 코드를 보고 알아 챌 수 있듯이
# - Memoization(Top-Down)의 경우 재귀의 호출 스택이 Recursion Error를 발생시킬 수 있다.
# - Bottom-Up의 경우 어떤 입력이 들어와도 처음부터 계산하기 때문에 불필요한 연산이 생긴다.
# https://kill-xxx.tistory.com/18
# https://zzong2.tistory.com/12