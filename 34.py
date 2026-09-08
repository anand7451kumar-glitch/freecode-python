c = {'a':10, 'b':20, 'c':30}
tmp = list()
for k, v in c.items() :
    tmp.append( (v, k ) )

print(tmp)
[(10, 'a'), (20, 'b'), (30, 'c')]
tmp = sorted(tmp, reverse=True)
print(tmp)
[(30, 'c'), (20, 'b'), (10, 'a')]