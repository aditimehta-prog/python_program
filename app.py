import streamlit as st


st.set_page_config(page_title = "My Webpage",page_icon =":tada:",layout = "wide")
st.subheader("Hi, I am Aditi :wave:")
st.title("Python and C++ Developer")
st.write("I am passionate about finding the solution of problem, building projects and working with code.")
st.code("""print("\n\n\n--------------------------------------- Welcome To Our ATM -----------------------------------------")
print("\nWhat you want to do?","\n1.Deposit money\n2.Withdraw money\n3.Check your balance\n4.Nothing")
balance = 40000
pin = 1234
option = int(input("Please enter your option number that you want to choice."))
if option == 1:
    print("you want to deposit your money.")
    pin1 =int(input("Please enter your PIN code."))
    if pin == pin1:
         print("PIN is correct.Now, you can do your work.")
    else:
         print("PIN is incorrect.")
    money=int(input("Please enter your amount that you want to deposit."))
    balance=balance+money
    print("The money is deposit successfully.")
    checkbal=input("Do you want to check your balance.(yes/no)").lower()
    if checkbal=='yes':
        print(f"Now, your balance is {balance}.")
elif option == 2:
    print("you want to withdraw your money.")
    pin1 =int(input("Please enter your PIN code."))
    if pin == pin1:
         print("PIN is correct.Now, you can do your work.")
    else:
         print("PIN is incorrect.")
    money=int(input("Please enter your amount that you want to withdraw."))
    if balance > 1000:
            balance=balance-money
            print("The money is withdrawal successfully.")
    elif money >=20000:
         print("Your amount of money to withdrawal is t0o much than your limit of withdrawal.")
    else :
         print("The balance is insufficent so you can not withdraw your money.")      
    checkbal=input("Do you want to check your balance.(yes/no)")
    if checkbal=='yes':
        print(f"Now, your balance is {balance}.")
elif option == 3:
    pin1 =int(input("Please enter your PIN code."))
    if pin == pin1:
         print("PIN is correct.Now, you can do your work.")
    else:
         print("PIN is incorrect.")
    print(f"your balance is {balance}.")
elif option == 4:
     print("you want to do nothing")
print("Thank you.visit again")     
         
    
""")