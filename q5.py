def polyinomial(cofficents,number):
    result = 0
    power = len(cofficents) - 1
    
    for i in range(len(cofficents)):
        result += cofficents[i] * pow(number, power)
        power -= 1

    return result

n = int(input("Enter Value of (n): "))
coff = []

for i in range(0,3):
    i = int(input("Enter Coefficients and a constant from left to right: "))
    coff.append(i)

print(polyinomial(coff,n))