#2
f = open('24-233.txt').read()

k = 0
mma = 0
ma = 0
s =''

for i in f:
    if i.isdigit():
        k += 1
        s += str(i)
        s1 = int(s)
        mma = max(s1, mma)
        ma = max(k, ma)
    else:
        s = ''
        k = 0
print(mma, ma)













