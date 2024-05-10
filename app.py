#Banking system 
bank_user = {'sakib': 1234, 'robin': 4321, 'sami': 50000, 'billgets': 90000}
print('Wellcome to our virtual banking system..');
while True:
    print('What do you like to do')
    print(' ' + '1.VIEW BALANCE')
    print(' ' + '2.VIEW ALL BANK INFO')
    print(' ' + '3.UPDATE BALANCE')
    print(' ' + '4.EXIT')
    desc = input('please enter a key 1 to 4  ')
    if desc == '1':
        print('Please Enter Your Name:')
        userName = input()
        if userName in bank_user.keys():
            print(userName + ' Your Bank Blance Is ' + str(bank_user[userName]))
        else:
            print('The is not found..! Would you like to add the user account?')
            desc =input('Please Press Yes or No ...')
            if desc == 'Yes':
                userName = input('Plese Enter Your Name: ')
                balance = int(input('Plese Enter Your Balance: '))
                bank_user.update({userName: balance})
            else:
                print('Would You Like To Exit?')
                desc = input('Please Enter Yes')
                if desc == 'Yes':
                    break
    elif desc == '2':
        for userName, balance in bank_user.items():
            print('UserName: ' + str(userName) + 'Balance: ' + str(balance))
    elif desc == '3':
        print('Enter Your Name Please:')
        userName = input()
        if userName in bank_user.keys():
            print('Do You Went To Add or Subtract from Your Savings?')
            desc = input()
            if desc == 'Yes':
                temBalance =bank_user[userName]
                extra = int(input('Enter Your Add Amount:'))
                bank_user[userName] = temBalance + extra
                print('Balance Updated. Your Balance is: ' +bank_user[userName])
            else:
                print('There is no Account in This Bank')
    elif desc == '4':
        break
    

