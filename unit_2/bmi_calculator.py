bmi_categories = f""" 
Formula: weight (lb) / [height (in)]2 x 703

BMI Categories:
---------------
underweight = <18.5
normal_weight = 18.5–24.9
overweight = 25–29.9
obesity = BMI of 30 or greater
 """
print(bmi_categories)

weight = input('enter weight(lbs): ')
height = input('enter height(in): ')
calculated_BMI = float(weight) / (float(height) * float(height)) * 703

result = round(calculated_BMI)
sentence = f'Your Body Mass index is:  {result}'
print(sentence)