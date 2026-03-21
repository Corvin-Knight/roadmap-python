print("Simple Weight Converter")

Weight = input("Weight: ")
Unit = input("k(g) or l(bs): ")
 
if Unit == "l":
    print(float(Weight) * 0.453592) 
elif Unit == "k":
    print(float(Weight) / 0.453592)     
