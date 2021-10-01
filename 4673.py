no_self = []
self =set(i for i in range(1,10001))
for i in range(1,100001):
    for j in str(i):
        i+=int(j)
    no_self.append(i)

no_self = set(no_self)
self = sorted(self-no_self)

for i in self:
    print(i)