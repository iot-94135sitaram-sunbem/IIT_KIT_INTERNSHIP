conversions = [
    lambda tons: tons * 1000,                
    lambda kg: kg * 1000,                      
    lambda g: g * 1000,                        
    lambda mg: mg / 453592.37                  
]

tons = float(input("Enter weight in tons: "))

kg = conversions[0](tons)
gm = conversions[1](kg)
mg = conversions[2](gm)
lbs = conversions[3](mg)

print("Weight in kilograms:", kg)
print("Weight in grams:", gm)
print("Weight in milligrams:", mg)
print("Weight in pounds:", lbs)
