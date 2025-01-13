from turtledemo.minimal_hanoi import hanoi

print("Welcome to my program!")
pet = "cat"
petname = "blackjack"
petgender = "his"
print(f"I have a {pet} and {petgender} name is {petname}")


myname = "Eirwyn"
myage = "25"
annualsavings = "$1000"
print(f"Hello {myname}! I am currently {myname} years old. In 10 years, I will be 35 years old! \nIf I save {annualsavings} each year, in 5 years I will have $5000.")


Januarydays = 31
hoursday = 24
secondshour = 360
print("There are "+str(Januarydays)+" days in January. There are "+str(hoursday)+" hours in a day. \nThere are "+str(secondshour)+" seconds in an hour.")
print(f"There are {Januarydays * hoursday * secondshour} seconds in a month.")


egg_input = input("How many eggs are you using?: ")
carton_math=(int(egg_input)//(12))
remainder=(int(egg_input)%12)
print(f"You can make {carton_math} carton(s) with {remainder} remaining egg(s).")