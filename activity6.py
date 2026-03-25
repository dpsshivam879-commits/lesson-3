weight=float(input("enter your weight in kg:"))
height=float(input("enter your weight in cm:"))
BMI=weight/(height/100)**2
if BMI<= 18.5:
    print("you are undernourished")
elif BMI<=24.9:
    print("you are over nourished")
elif BMI<=30.9:
    print("you are healthy")
else:
    print("you are obese")