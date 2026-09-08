import re
x = 'My 2 favorite numbers are 7 and 13'
y = re.findall('[0-9]+', x)
print(y)    
['2', '7', '13']
y = re.findall('[AEIOU]+', x)
print(y)
[]
