#def average(num1, num2, num3)->int:
 #   return (average)/3

#print (average( 4, 6, 9))
#print (average( 1, 2, 3))


#Dog Age
#dog age = 24+(dog_age-2)x4 OR 24+(dog_age/2)-8. Reminding myself of the math so I don't have to alt+tab
dog_age=int(input("Give me a dog age, please:"))
def my_function(dog_age):
    print (f"{dog_age} years is actually {24+(dog_age-2)*4} years in human years.")
my_function(dog_age)



#Car Math
#Ger: -5%/year
#Japanese: -7%/year
#Italian: -5%/year
car_brands = ["German", "Italian", "Japanese"]
Car_Manfct=input("Do you own a Japanese, Italian, or German car? Make sure you capitalise, please:")
if Car_Manfct not in car_brands:
    print("I'm sorry, please choose one of the listed options.")
Car_Money = int(input("How much did you pay for it?:"))
Car_Age = int(input("And lastly, how many years ago did you buy it?:"))
if Car_Age>2025:
    print("Nice try, pal.")#just in case anyone tries to be funny
if Car_Manfct=="German":
    print(f"Your Benz is curently worth ${Car_Money-((2025-Car_Age)*0.05)}, {Car_Age} year(s) after you bought it.")
if Car_Manfct=="Japanese":
    print(f"Your Subaru is currently worth ${Car_Money-((2025-Car_Age)*0.07)}, {Car_Age} year(s) after you bought it.")
if Car_Manfct=="Italian":
    print(f"Your Ferrari (showoff) is worth ${Car_Money-((2025-Car_Age)*0.05)}, {Car_Age} year(s) after you bought it.")


#Dog Age Calc
#dog age = 24+(dog_age-2)x4 OR 24+(dog_age/2)-8. Reminding myself of the math so I don't have to alt+tab
dog_name=input("What's your dog's name?:")
dog_age2=input(f"How old is {dog_name}?:")
def dog_math(dog_age2):
    print (f"{dog_name} is {dog_age2}, which is actually {24+(dog_age2-2)*4} years in human years.")

dog_math(int(dog_age2))

#Ice Cream Math
#Price = scoop(s)*1.15+2.25
scoop_count = input("One last thing before you go! How many scoops of ice cream do you usually like?:")
def icecreammath(scoop_count):
    print (f"Your {scoop_count} scoop cone will cost you ${scoop_count*1.5+2.25}.")
icecreammath(int(scoop_count))