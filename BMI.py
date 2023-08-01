# BMI Calculator

height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))


bmi = round(weight / height ** 2)
if bmi < 18.5:
    print("Underweight")
elif bmi < 25:
    print("Ideal Weight")
elif bmi < 30:
    print("Slightly overweight")
elif bmi < 35:
    print("Overweight")
else:
    print("Obese")
