score_list = []
for _ in range(5):
    lst_cook = list(map(int, input().split()))
    score_list.append(sum(lst_cook))

first = max(score_list)
print(score_list.index(first)+1, first)