fname = input('Enter File:')
if len(fname) < 1 : fname = 'python.txt'
hand = open(fname)


di = dict()
for lin in hand:
    lin = lin.rstrip()
    wds = lin.split()
    
    for w in wds:

        di[w] = di.get(w,0) + 1

        print(w, 'new', di[w])

        
print(di)

#most common word
largest = -1
for k,v in di.items():
    print(k,v)
    if v > largest:
        largest = v
        theword = k

print('Done', largest)

