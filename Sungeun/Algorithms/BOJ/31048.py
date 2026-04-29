n = int(input())

# 단순 for 반복문을 통한구현 
for _ in range(n): # in testcase 
    a = int(input())
    sat = 1
    for i in range(1, a+1):
        sat *=i 
    print(sat%10) # 1의 자리 남은 수만 출력 
    
    
# 재귀 함수를 통한 구현 
# 1
def factorial(n):
    if n == 1: # n 이 1일때
        return 1
    return n * factorial(n-1) # n 과 factorial  함수에 n-1 을 넣어서 반환된 값을 곱합

# 2
def factorial_recursive(n):
    return n * factorial_recursive(n-1) if n > 1 else 1
# 모듈을 활용한 구현
# 1
import math

math.factorial(n)
# 2
from functools import reduce

def factorial_reduce(n):
    return reduce(lambda x, y: x * y, range(1, n+1))
        
# https://dojang.io/mod/page/view.php?id=2353
# https://shoark7.github.io/programming/algorithm/several-ways-to-solve-factorial-in-python