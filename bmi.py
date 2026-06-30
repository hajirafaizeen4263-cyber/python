#bmi calculator
bmi=lambda weight,height:weight/(height**2)
def main():
    print("WELCOME TO BMI CALCULATOR.......")
    weight=float(input("enter your weight in kg:"))
    height_cm =float(input("enter your height in cm:"))
    height_m=height_cm/100
    bmi_value=bmi(weight,height_m)
    print("your bmi",bmi_value)
    if bmi_value <=16:
            print("severe thinness")
    elif  bmi_value<=17:
            print("moderate thinness")
    elif bmi_value<=18.5:
            print("mild thinness")
    elif bmi_value<=25:
            print("normal")
    elif bmi_value<=30:
            print("overweight")
    elif bmi_value<=35:
            print("obese class 1")
    elif bmi_value<=40:
            print("obese class 2")
    else:
            print("obese class 3")
main()