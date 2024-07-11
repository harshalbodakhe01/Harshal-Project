import time
print()
print()
print("===========WELCOME TO HARSHAL'S BANK OF INDIA============")
print()
print()
print("Please insert your Card")
time.sleep(5)
password=1005
pin=int(input("Enter your ATM pin:"))
balance=5000
if(pin==password):
    while True:
        print("""
          1 == balance
          2 == withdraw balance
          3== deposite balance
          4 == exit
          """
          )
        try:
            option=int(input("Please enter your choice:"))
        except:
            print("Please enter valid option")
        if option==1:
            print(f"Your current balance is {balance}")
    
        try:
            option=int(input("Please enter your choice:"))
        except:
            print("Please enter valid option")
        if option==1:
            print(f"Your current balance is {balance}")

        if option==2:
            withdraw_amount=int(input("Please enter withdraw amount:"))
            balance=balance-withdraw_amount
            print(f"{withdraw_amount} is debited from you account")
            print(f"Your updated balance is {balance}")

        if option==3:
            deposite_amount=int(input("Please enter deposite amount:"))
            balance=balance+deposite_amount
            print(f"{deposite_amount} is credicted yo your account")
            print("Your updated balance is",balance)
    
        if option==4:
            break
    print("=================THANK YOU FOR VISITING====================")
    
        