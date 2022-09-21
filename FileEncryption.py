infile=open('info_security.txt','r')
outfile=open('encrypted.txt','w')

code={'A':'!','a':'1','B':'@','b':'2','C':'$','c':'3','D':'%','d':'4',
'E':'^','e':'5','F':'&','f':'6','G':'*','g':'7','H':'(','h':'8','I':')','i':'9',
'J':'-','j':'Q',
'K':'_','k':'E','L':'+','l':'O','M':'=','m':'P','N':'{','O':'}','n':'L','O':'`','o':'a',
'P':'[','p':'A','Q':']','q':'D','R':'|','r':'G','S':':','s':'H',
'T':';','t':'W','U':'<','u':'Z'
,'V':'>','v':'B','W':',','w':'F','X':'.','x':'I','Y':'?','y':'C','Z':'/','z':'~'}

text=infile.read()
text=text.rstrip('\n'+','+'.')
list=text.split(" ")

encrypt=""
for x in range(len(text)):
    if text[x] in code.keys():
        encrypt+=code[text[x]]
    else:
        encrypt+=text[x]
print(encrypt)


outfile.write(encrypt+'\n')

outfile.close()