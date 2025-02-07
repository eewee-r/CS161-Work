#Div5
num=input("Give me a number:")
math=(int(num)//5)


#State Capitals
valid_states=("Oregon","Washington","California","Idaho","Maine","Florida")
pairs={"Oregon":"Salem", "Washington":"Olympia", "California":"Sacramento","Idaho":"Boise","Maine":"Augusta","Florida":"Tallahassee"}
print (valid_states)
state_choice=input("Pick one of the above listed states, and don't forget to capitalise: ")
def state_capitals(state_capitals):
    print(state_choice+", "+pairs[state_choice])

state_capitals(state_choice)

#Pool Pricing
#<2 free, 2-11 $3, 11-60 $6, >60 $4
guest_age=int(input(print("Hello, welcome to the public pool! How old are you?")))
def pool_price_calc(guest_age):
    if guest_age<2:
        return 0
    elif guest_age<11:
        return 3
    elif guest_age<60:
        return 6
    elif guest_age>60:
        return 4
    print(f"Based on your age, you will pay {pool_price_calc}.")
pool_price_calc(guest_age)

#160
