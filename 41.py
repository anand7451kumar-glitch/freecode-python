import re
hand = open('clown.txt')
for line in hand:
    line = line.rstrip()
    stuff = re.findall('^X-DSPAM-Confidence: ([0-9.]+0', line)
    if len(stuff) != 1 : continue
    num = float(stuff[0])
    numlist.append(num)
print('Maximum:', max(numlist))


wikipedia.org/wiki/Internet socket 
wikipedia.org/wiki/TCP and UDP port

www.ietf.org

telnet www.dr-chuck.com 80