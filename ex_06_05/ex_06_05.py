str = 'X-DSPAM-Confidence: 0.8475'

#print(str)
ipos = str.find(':')
#print(ipos)
piece = str[ipos+1:]
#print(piece)
#print(piece+42.0) # will fail
value = float(piece)
print(value)
#print(value+42.0)
