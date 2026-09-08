fhand = open('notes.py')
for line in fhand:
    if line.startswith('from:') :
        print(line)

