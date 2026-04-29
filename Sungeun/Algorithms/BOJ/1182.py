N, M = map(int,input().split())
arr = list(map(int,input().split()))

def get_subsequence(arr):
    # sub = []
    count = 0
    def backtracking(idx, curr):
        nonlocal count 
        if idx == len(arr):
            if curr and sum(curr) == M:
                count += 1
            # sub.append(curr[:])
            return
        curr.append(arr[idx])
        backtracking(idx+1, curr)
        
        curr.pop()
        backtracking(idx+1, curr)
    backtracking(0, [])
    return count

print(get_subsequence(arr))