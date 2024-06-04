class VSLA:
    name = input( "Enter your name: ")
    print( "Welcome to the VSLA Banking system: " + name)

    Membership_number = int(input( " Enter your four digit membership number : "))
    if  Membership_number >= 10000:
        print( " Invalid Membership Number")
        quit()
    elif Membership_number < 1000:
        print ( " Invalid Membership Number")
        quit()
    else:
        print( f" Your membership Number :  {Membership_number} has been verified")



    def __init__(self):
        self.balance = 0
        self.subscription = 10
        print( f"Your account is created with {self.subscription} Euros subscription ")

    def deposit(self):
        amount = float(input(" Enter the amount to be deposited ; "))
        self.balance = amount + self.balance
        print(" Deposit is successful and the balance in the account is %f" % self.balance)

    def withdraw(self):
        amount = float(input("Enter the amount to withdraw : "))
        if (self.balance >=amount):
            self.balance = self.balance -amount
            print( "The withdraw is successful and the balance is %f" % self.balance)
        else:
            print( " Insufficient Balance")

    def enquiry(self):
        print(" Thank you for using our VSLA system ")
        print (" Your Balance on the account is %f" % self.balance)


acc = VSLA()
acc.deposit()
acc.withdraw()
acc.enquiry()


















