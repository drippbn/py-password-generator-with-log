import random 
import logging

logging.basicConfig(filename='password.log', encoding='utf-8', level=logging.DEBUG,
format='%(asctime)s - %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

print('Alpha-numeric password generator by Bn')

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ`!"£$%^&*()-_=+[{]};:@#~,<.>/?'

number = input('No of passwords to generate (Restricted to 1 for logging): ')
number = int(number)

length = input('Length: ')
length = int(length)

print('Passwords listed below: ')

for pwd in range(number):
    passwords = ''
    for c in range(length):
        passwords += random.choice(chars)
    print('Your password: '+ passwords)

logging.info(password)
