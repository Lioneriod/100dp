#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

total = float(input('What was the bill total value?\n'))
totalDisplay = "{:.2f}".format(total)
people = int(input('How many people are splitting this bill?\n'))
tip = input('How much percentage of tip are you guys giving?\n')
tipPercentage = float('1.'+f'{tip}')
formula = (total/people) * tipPercentage
roundedFormula = round(formula,2)
roundedFormula = "{:.2f}".format(formula)
print(f'For a bill of $ {totalDisplay}, split between {people} people with a tip percentage of {tip}%, each person will be paying ${roundedFormula}')
