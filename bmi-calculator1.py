# BMI Calculator
# BMI = Weight(kg) / Height * Height(m)

# input
weight = int(input("INPUT YOUR WEIGHT (Kg) : "))
height = int(input("INPUT YOUR HEIGHT (M) : "))

# process
# cm => m
height /= 100
# calculate BMI
bmi = weight / (height * height)

# output
print("YOUR WEIGHT IS : " + str(weight))
print("YOUR HEIGHT IS : " + str(height))
print("-------------------")
print("YOUR BMI IS : " + str(bmi))

# --------------- OR --------------- #

# input
weight = int(input("INPUT YOUR WEIGHT (Kg) : "))
height = int(input("INPUT YOUR HEIGHT (M) : "))/100

# output
print("YOUR WEIGHT IS : " + str(weight))
print("YOUR HEIGHT IS : " + str(height))
print("-------------------")
print("YOUR BMI IS : " + str(weight / (height * height)))
