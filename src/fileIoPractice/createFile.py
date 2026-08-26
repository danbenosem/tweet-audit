import os

print(os.getcwd())

with open ('accounts.txt', mode ='w') as accounts:
    accounts.write('100 jones 2.345\n')
    accounts.write('200 jasd 2.345\n')
    accounts.write('300 jones 21.2\n')
    accounts.write('400 joad 21.2\n')


with open ('accounts.txt', mode ='r') as accounts:
    print(f'{"Accounts":<10} {"Name":<10} {"Balance":>10}')
    for record in accounts:
        account,name,balance= record.split()
        print(f'{account}:<10 {name}:10 {balance}:>10')


