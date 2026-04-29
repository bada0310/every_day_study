N= int(input())

# Please write your code here.
arr = [4, 5, 6]
path = []
is_finished = False

def is_good(path):
    if len(path) <= 1:
        return True
    for l in range(1, len(path)//2 +1): # 부분 수열을 비교하는 것 /반 나눈 것을 기준으로 전과 후를 비교
        if path[-l:] == path[-(2*l):-l]:
            return False
    return True
def perm():
    global is_finished
    if is_finished:
        return
    if len(path) == N:
            print("".join(map(str,path)))
            is_finished =True
            return
    for i in range(len(arr)):
        path.append(arr[i])
        if is_good(path):
            perm()
    
        path.pop()
perm()
        