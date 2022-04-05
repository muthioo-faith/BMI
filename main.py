height=float(input('Enter height in m\n'))
weight=int(input('Enter weight in kg:\n'))


bmi=float(weight/(height**2))
print(f"your BMI is {bmi}")

if bmi <=19.5:
   print("you are underweight.")
elif bmi <=22.6:
    print("you are health.")
elif bmi <=29.9:
    print("you are over weight.")
elif bmi <=35.7:
    print("you are severally over weight.")
elif bmi <=39.9:
    print("you are obese.") 
else:
    print("you are severely obese.")           













