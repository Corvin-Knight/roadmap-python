print("Simple Weight Converter")

Weight = input("Weight: ")
Unit = input("k(g) or l(bs): ")
 
if Unit.upper() == "L":
    print("Here is you Weight in Kilos!")
    print(float(Weight) * 0.453592) 
elif Unit.upper() == "K":
    print("Here is your Weight in Pounds!")
    print(float(Weight) / 0.453592)