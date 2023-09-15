h1 = int(input ("digite a hora da primeira entrada"))
min1 = int(input ("digite os minutos da primeira entrada"))
h2 = int(input ("digite a hora do segundo horário"))
min2 = int(input ("digite os minutos do segundo horário"))
htemp =0
if h1 > 12:
    h1 -= 12

if h2 > 12:
    h2 -= 12

totalmin = min1 + min2

if totalmin >=60:
    totalmin -= 60
    htemp = 1

htotal = h1 + h2 + htemp

if htotal > 12:
   htotal -= 12

print(f"o resultado da soma é {htotal}hs e {totalmin}min")

