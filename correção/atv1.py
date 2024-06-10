a = 6
b = 10
mmc = 0
if a > b:
    maior = a
else:
    maior = b
    
while mmc == 0:
    resto_a = maior % a
    resto_b = maior % b
    if resto_a + resto_b == 0:
        mmc = maior
    maior += 1
print(mmc)
        
