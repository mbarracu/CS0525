cityInp = input('Enter your city of birth: ')
while cityInp.isdigit():
    cityInp = input('Do not enter numbers, please give the name of the city: ')


petInp =  petInp = input('enter your pets name: ')   
while petInp.isdigit():
    petInp = input('Do not enter numbers, please enter the name of your pet: ')

print(f'Band name: {petInp} from {cityInp} ')
