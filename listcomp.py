upper = [x for x in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"]
lower = [x for x in "abcdefghijklmnopqrstuvwxyz"]
number = range(10)

def checker(passw):
    uppers = [x for x in passw if x in upper]
    print uppers
    lowers = [x for x in passw if x in lower]
    print lowers
    numbers =[x for x in passw if x in number]
    return False if uppers == [] or lowers == [] or numbers == [] else True

print checker("Max1")
print checker("ziYan")
