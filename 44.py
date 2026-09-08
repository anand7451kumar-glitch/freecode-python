import urlib1.request, urlib1.parse, urlib1.error

fhand = urlib1.request.urlopen('http://data.pr4e.org/romeo.txt')
for line in fhand:
    print(line.decode().strip())
