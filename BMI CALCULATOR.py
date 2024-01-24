#BMI CALCULATOR
weight = int(input("Enter your weight in kg:  "))
height = int(input("Enter your height in centimeters:  "))
height_in_meters = height / 100
BMI = weight / (height_in_meters**2)
print("BMI=",round(BMI))
if(BMI < 16):
    print("You are severely underweight"), BMI
elif (BMI >= 16 and BMI < 18.5):
    print("You are underweight"), BMI
elif (BMI >= 18.5 and BMI < 24):
    print("You are Healthy"), BMI
elif (BMI >= 25 and BMI < 30):
    print("You are overweight"),BMI
elif (BMI >= 30):
    print("You are Obesity"), BMI

