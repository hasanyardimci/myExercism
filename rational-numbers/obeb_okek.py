def f_multiple(nmbr):
    multiple_list = []
    for b in range(2,nmbr+1):
        while nmbr % b == 0 and nmbr >= b:
            nmbr = nmbr / b
            multiple_list.append(b)
    return multiple_list


n1 = 4000
n2 = 1440

m1 = f_multiple(n1)
m2 = f_multiple(n2)

obeb = []
if n1 <= n2:
    while len(m1) > 0:
        if m1[0] in m2:
            obeb.append(m1[0])
        m1.pop(0)
else:
    while len(m2) > 0:
        if m2[0] in m1:
            obeb.append(m2[0])
        m2.pop(0)
gcd = 1
for i in obeb:
    gcd *= i
print(gcd)