acn = 'Hello row'
try:
	ast = int(acn)
except:
	ast = -1
print('First', ast)

acn = '123'
try:
	ast = int(acn)
except:
	ast = -1
print('Second', ast)
