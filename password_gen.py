# Random password generator
import random

Letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N',
        'O','P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c'
        ,'d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

symbols = ['!','@','#','$','%','^','&','*']
numbers = ['0','1','2','3','4','5','6','7','8','9']
generated_password = []

print('************* Welcome to random password generator ! *************')
print("Please provide some details for the length of your required password.")
no_of_letters = int(input("How many letters you want in your password ? :  "))
digits_required= int(input("How many digits you want ? : "))
symbols_choice = int(input("How many symbols you want ? : "))

for l in range(1,no_of_letters+1):
    generated_password+= random.choice(Letters)
    
for n in range(1,digits_required+1):
    generated_password+= random.choice(numbers)

for s in range(1,symbols_choice+1):
    generated_password+= random.choice(symbols)

final_password = ''
random.shuffle(generated_password)

for i in generated_password:
    final_password = final_password + i

print(final_password)