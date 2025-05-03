class Bank_system:
     __balance=0
     def deposit(self,value):
         if value>0:
             self.__balance += value
             print("deposit successful")
         else:
             print("invalid balance")
     def withdraw(self,value):
         if value>0 and value<= self.__balance :
             self.__balance -=value
             print(f"{value} tk withdraw successful")
         else:
             print("insufficient balance")
     def check_banalce(self):
         print(f"{self.__balance} TK" )
obj=Bank_system()
while(1):
    print(" Chose 1 for Deposit")
    print(" Chose 2 for Withdraw")
    print(" Chose 3 for Check Balance")
    print(" Chose 4 for Exit")
    n=int(input("Enter 1-3 "))
    if(n==1):
        value=int(input("Enter the value you want to deposit "))
        obj.deposit(value)
    elif(n==2):
        value = int(input("Enter the value you want to withdraw "))
        obj.withdraw(value)
    elif(n==3):
        obj.check_banalce()
    elif(n==4):
        break
    else:
       print("Please chose between 1 to 4")

