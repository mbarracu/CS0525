inputs = []

print('Enter numbers to calculate the SMA (press Enter without typing anything to stop):')

while True:
    value = input('> ')
    
    if value == '':
        break

    while not value.replace('.', '', 1).isdigit():
        print("Invalid input. Please enter a number.")
        value = input('> ')

        if value == '':
            break

    if value == '':
        break

    inputs.append(float(value))

window = round(len(inputs) / 3)

last_values = inputs[-window:]

sma = sum(last_values) / window

print(f"SMA: {sma}")

