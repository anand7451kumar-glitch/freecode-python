import re
x = 'From: Using the : character'
y = re.findall('^F.+?:', x)
print(y)
['From:']

y = re.findall('\S+@\S+',x)
print(y)