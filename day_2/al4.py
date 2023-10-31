temp = "5 degrees"
cel = 0
try:
	fahr = float(temp)
except:
	print('error, input numerical value')
	quit()
cel = (fahr - 32.0) * 5.0 / 9.0
print(cel)
