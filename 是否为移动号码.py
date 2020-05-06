x = ['13915556234','13025621456','15325645124','15202362459']
a = '456789'
b = '01289'
for i in x :
    if i[:2]=='13' and i[2] in a:
        print(i,'yes')
    elif i[:2]=='15' and i[2] in b:
         print(i,'yes')
    else:  print(i,'no')
