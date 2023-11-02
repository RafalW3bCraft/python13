sh = input('ENter Hours: ')
sr = input('Enter Rate: ')
try:
    fh = float(sh)
    fr = float(sr)
except:
    print('Error, please enter numerical input')
    quit()
    
print(fh, fr)
if fh > 40:
    reg = fr * fh
    otp = (fh - 40.0) * (fr * 0.5)
    xp = reg + otp
else:
    xp = fh * fr
print('Pay:', xp)   