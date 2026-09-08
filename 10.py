

data='Fromstephen.marquard@uct.ac.zaSatJan509:14:162008'
atpos=data.find('@')
print(atpos)
21
sppos=data.find('',atpos)
print(sppos)
31
host=data[atpos+1:sppos]
print(host)