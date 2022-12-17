# Banking Management System Using Python
class Bank:
    nAcc = {}
    nEnq={}
    c=0

    def NewAcc(self):
        print("Please enter the Account holder id of 3 digits only")
        AccHolId = int(input("Enter the new account holder id:"))
        AccHolNm = input('Enter the new account holder name:')
        AccHolAge = int(input('Enter the new account holder age:'))
        AccHolAmt = int(input('Enter the amount deposited by the account holder:'))
        Bank.nAcc[AccHolId]=[[AccHolNm],[AccHolAge],[AccHolAmt]]
        Bank.c=AccHolAmt


    def DelIAcc(self):
        delAcc=int(input('Enter the Account no. you want to delete:'))
        if(delAcc in Bank.nAcc):
                del Bank.nAcc[delAcc]
        else:
            print("Customer not found")

    def DispTAcc(self):
        if(len(Bank.nAcc)==0):
            print('Empty List')
        print(Bank.nAcc)

    def DispIAcc(self):
        dispAcc = int(input('Enter the Account no. you want to show their details:'))
        for j in Bank.nAcc:
            if (dispAcc ==j):
                 print(Bank.nAcc[j])
            else:
                print('User Not found')

    def EdAmt(self):
        print('press 1. for Addition')
        print('press 2. for Subtraction')
        ch1=int(input('Enter the mathematical operation you want to do with this account holder amount:'))
        if(ch1==1):
            AmtAdd=int(input('Enter the amount you want to add into the account holder amount:'))
            AccHolid1=int(input('Enter the account no. on which you want to do this operation:'))
            for j in Bank.nAcc:
                if(AccHolid1 == j):
                    for y in Bank.nAcc[AccHolid1]:
                        if(y==[Bank.c]):
                            z=Bank.c+AmtAdd
                            Bank.nAcc[AccHolid1][2]=[z]

        elif(ch1==2):
            AmtSub = int(input('Enter the amount you want to add into the account holder amount:'))
            AccHolid2 = int(input('Enter the account no. of a customer on which you want to do this operation:'))
            for k in Bank.nAcc:
                if (AccHolid2 == k):
                        for x in Bank.nAcc[AccHolid2]:
                            if(x==[Bank.c]):
                                p=Bank.c-AmtSub
                                Bank.nAcc[AccHolid2][2]=[p]

        else:
            print('No Operation')

    def NewEnq(self):
        EnqNm = input('Enter the name of the person who want to know everything about this bank:')
        EnqEml = input('Enter the Email of that person:')
        Bank.nEnq[EnqNm]=EnqEml

    def DispEnq(self):
        print(Bank.nEnq)

obj=Bank()

while(True):
    print('press 1. for Creating Account')
    print('press 2. for Deleting Account')
    print('press 3. to Display Total Accounts')
    print('press 4. to Display Particular Account Holder Details')
    print('press 5. For New Enquiry')
    print('press 6. For Disp Enquiry List')
    print('press 7. to add amount or deduct amount from the account holder account')
    print('press 8. to exit')
    ch=int(input('Enter your choice:'))

    if ch==1:
        obj.NewAcc()

    elif ch==2:
        obj.DelIAcc()

    elif ch==3:
        obj.DispTAcc()

    elif ch==4:
        obj.DispIAcc()

    elif ch==5:
        obj.NewEnq()

    elif ch==6:
        obj.DispEnq()

    elif ch==7:
        obj.EdAmt()

    else:
        print('Wrong Choice')
        break
