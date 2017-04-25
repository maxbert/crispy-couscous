upper = [x for x in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"]
lower = [x for x in "abcdefghijklmnopqrstuvwxyz"]
number =[str(x) for x in range(10)]
char = [x for x in ".?!&#,;:-_*"]
    
def checker(passw):
    uppers = [x for x in passw if x in upper]
    lowers = [x for x in passw if x in lower]
    numbers =[x for x in passw if x in number] 
    return False if uppers == [] or lowers == [] or numbers == [] else True

def rater(passw):    
    uppers = [x for x in passw if x in upper]
    lowers = [x for x in passw if x in lower]
    numbers =[x for x in passw if x in number]
    chars = [x for x in passw if x in char]

    # The proportion of uppercase to lower case accounts for half the point value, and each number  and each symbol adds 0.5 points. the perfecrt password would be the same number of upper and lowercase letters, 5 symbols and 5 numbers, a password of only uppercase or only lowercase will get a zero
    
    a =  10 * ( ((len(uppers) * 1.0) / len(lowers)) * 0.5 + ((len(chars) * 1.0) / 5) * 0.25 + ((len(numbers) * 1.0) / 5) * 0.25 ) if len(uppers) <= len(lowers) else 10 * ( ((len(uppers) * 1.0) / len(lowers)) * 0.5  + ((len(chars) * 1.0) / 5) * 0.25 + ((len(numbers) * 1.0) / 5) * 0.25)
    return a if a <= 10 else 10.0

print checker("Max1&")
print rater("Max1&")
print checker("ziYan")
print rater("ziYan")
print rater("max")
print rater("MaXzIyAn12345?!&#,")
