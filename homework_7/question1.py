n = int(input("Pick a number between 1-5 and we will call it n: "))

names = []
ages = []

for i in range(n):
    inputs = input("Type your name and age separated by a space: ").split()
    name = inputs[0]
    age = int(inputs[1])
    names.append(name)
    ages.append(age)
    if 20 <= ages[i] <= 25:
        print("homies between the ages of 20 and 25:", names[i])
