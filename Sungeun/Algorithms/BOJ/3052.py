a = [int(input()) for _ in range(10)]
# print(a)
new_lst = []
for i in a:
    remain = i%42
    new_lst.append(remain)
    new_set = set(new_lst)

print(len(new_set))

