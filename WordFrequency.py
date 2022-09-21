
infile=open('sometext.txt','r')
words={}
i=0
text=infile.read()
text=text.rstrip('\n'+','+'.')
list=text.split(" ")
print(list)
for name in list:
    if name in list and name not in words:
        a=list.count(name)
        words[name]={'count': a}

print(words)
