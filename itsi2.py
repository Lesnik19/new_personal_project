file = open('data.txt', 'r', encoding='utf8')
data = file.readlines()
new_list = []
names = []
answer = 0
num = {}


def get_key(d, value):
    for k, v in d.items():
        if v == value:
            return k


for i in data[1:]:
    if i.find('/m') != -1:
        new_list.append(i)

for a in new_list:
    if a in names:
        pass
    else:
        names.append(a)

for u in names:
    num[u] = new_list.count(u)

print(num)
print(max(num.values()))
print(get_key(num, max(num.values())))
