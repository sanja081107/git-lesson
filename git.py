import pickle
gl = ['a', 'e', 'o', 'u', 'y', 'i']
b = []
with open('cities-europe.bin', 'rb') as f:
    a = pickle.load(f)
    print(len(a))
for i in a:
    col = 0
    for j in i:
        if j.isupper():
            col += 1
    if col == 1:
        b.append(i)
a = b
b = []
print(len(a))
for i in a:
    if i[0] == i[-1].upper():
        b.append(i)
a = b
b = []
print(len(a))
for i in a:
    if i[1] == i[-2] and i[1] in gl and i[-2] in gl:
        b.append(i)
a = b
b = []
print(len(a))
for i in a:
    if 'w' in i:
        b.append(i)
a = b
b = []
print(len(a))
for i in a:
    b.append(len(i))
x = b.index(min(b))
print(a[x])
