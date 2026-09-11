code = input()
word = ''
digits = '0123456789'
checker1 = True
checker2 = True

for i in range(len(code)):
    now = code[i]
    if now.isupper() and checker1:
        checker1 = False
        word+= str(now)
        first = i

    if now in digits and checker2:
        checker2 = False
        word += code[i+1]
        second = i+1
        dlina = second-first

full = second
while full+ dlina <= len(code):
    full += dlina
    word+= code[full]

print(word)


    


        
