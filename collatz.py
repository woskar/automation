#Collatz sequence, the simplest impossible math problem

def collatz(number):
    if number % 2 == 0:
        number = number // 2
        return number
    else:
        number = 3*number+1
        return number

print('Hello, my friend! Give me an integer and I will show you the collatz sequence:')
print('Where do you want to start?')
try:
    number = int(input())
    while(number > 1):
        number = collatz(number)
        print(number)

except:
    print('Please insert a number, not something else')
