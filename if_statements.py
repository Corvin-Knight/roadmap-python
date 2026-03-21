temperature = 25

if temperature > 30: #{ in most other languages, including C#, Java, and JavaScript, blocks of code are put braces, here in python we use these indentations
    print("It's a hot day")
    print("Drink plenty of water")
elif temperature > 20: # (20, 30]
    print("It's a nice day")
elif temperature > 10:
    print("It's a bit cold")
else:
    print ("It's cold")
   
#}
print("Done") #Even if temperature is not met, this print is outside of the if temperature code block, so it will be done no matter what