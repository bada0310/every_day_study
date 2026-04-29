# 1차원 젠가

n = int(input())
blocks = [int(input()) for _ in range(n)]
s1, e1 = map(int, input().split())
s2, e2 = map(int, input().split())

# Please write your code here.
s1 -= 1
s2 -= 1
e1 -= 1
e2 -= 1

blocks = blocks[0:s1] + blocks[e1+1:]
blocks = blocks[0:s2] + blocks[e2+1:]

print(len(blocks))
print("\n".join(map(str, blocks)))