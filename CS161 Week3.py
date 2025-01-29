name=input("What is your name?:")
print (f"Hello {name}. Welcome to my program")


age=input("How old are you?:")
#print(age + 5)
#The above command will not work because the user input needs to be turned into an integer.
#As is, it is a string, and thus cannot be acted upon by an integer like 5.
#The solution is to say print (int(age)+5). This converts user input 'age' into an integer.
print(f"In 5 years, you will be {int(age)+5} years old.")


hrs_worked=int(input("How many hours do you work a week?:"))
hrly_wage=int(input("How much do you make an hour without tips?:"))
print(f"Your gross pay this week will be ${(hrs_worked)*(hrly_wage)}.")
annual_income=(hrs_worked*hrly_wage*52)
print(f"Your gross pay in a year, assuing no changes in employment status, will be ${annual_income}.")

#Taxes
if(0<annual_income<11600):
    print(f"And you will pay ${annual_income*0.1} in annual taxes, leaving you with ${annual_income-(annual_income*0.1)}.")
elif(11600<annual_income<47150):
    print(f"And you will pay ${annual_income*0.12} in annual taxes, leaving you with ${annual_income-(annual_income*0.12)}.")
elif(47150<annual_income<100525):
    print(f"And you will pay ${annual_income*0.22} in annual taxes, leaving you with ${annual_income-(annual_income*0.22)}.")
elif(100525<annual_income<191950):
    print(f"And you will pay ${annual_income*0.24} in annual taxes, leaving you with ${annual_income-(annual_income*0.24)}.")
elif(191950<annual_income<243725):
    print(f"And you will pay ${annual_income*0.32} in annual taxes, leaving you with ${annual_income-(annual_income*0.32)}.")
elif(243725<annual_income<609350):
    print(f"And you will pay ${annual_income*0.35} in annual taxes, leaving you with ${annual_income-(annual_income*0.35)}.")
elif(609350.01<annual_income<999999999999999):
    print(f"And you will pay ${annual_income*0.37} in annual taxes, leaving you with ${annual_income-(annual_income*0.37)}.")