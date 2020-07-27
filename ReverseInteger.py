


x = -123
newInt = 0
retInt = 0
if(x>0):
    new = (str(x)[::-1])
    newInt = int(new.strip())
else:
    new = str(str(abs(x))[::-1])
    newInt = (-1*int(new.strip()))
if 2 ** 31 > newInt and newInt >= (-2 ** 31):
    retInt = newInt
print(newInt)
