#2798
n, m = map(int, input().split())
# m 을 넘지 않으며 합이 최대한 m에 가까운  카드 세장의 합
lst_num = list(map(int,input().split()))
ans = 0
# 재귀를 이용한 백 트래킹으로 가능 ?
lst_min = []
for i in range(n):
    for j in range(i + 1, n):        
        for k in range(j + 1, n):
            total = lst_num[i]+lst_num[j]+lst_num[k]
            if total <= m:
                ans = max(ans, total)

print(ans)

# # 조합 만드는 방법 
# # 가장 빠른 법은 아무래도 모듈이겠죠 

# # 임의의 숫자 조합(작은 데이터 셋) 
# itertools.combinations 활용
# # 임의의 숫자 조합(큰 데이터 셋) 
# DP 또는 Meet-in-the-middle

# 이 문제의 포인트는 2가지다.
# 1. 조합 만들기 
# 2. 가장 가까운 수 찾기 
# 두 가지 함수를 섞어 풀이하는 게 가장 많다. 
# (추가로 합을 활용하기 = 합리스트? )

# + 두 숫자의 합 정렬 후 투 포인터 O(NlogN)
# + 세 숫자의 합 정렬 후 고정 + 투포인ㄴ터 O(N^2)

# 추가 질문 list() 와 [] 의 차이 
# /a = 2 5 4 3 1 7 6 


lst_1 = list(map(int,input().split())) # list()는 map object 덩어리 들이 순차적으로 하나씩 리스트에 넣게 된다. 
lst_2 = [map(int,input().split())] # [map object 덩어리]

print(lst_1)
print(lst_2)