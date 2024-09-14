# # START
# # a
height: float = float(input("Enter your height: "))
while height < 0.4  or height > 2.5:
        print(f"wrong input")
        height: float = float(input("Enter your height: "))
print(f"your height is {height}")

#  b
num: int = int(input("Enter a number: "))
num2: int = int(input("Enter another number: "))
for i in range(num, num2+1):
    print(i)
for i in range(num2, num+1):
    print(i, end=" ")
#
# # c
counter: int = 1
pi = 3.14
pi_input: float = float(input("What is the value of pi?: "))
while pi != pi_input and counter < 3:
    counter += 1
    pi_input: float = float(input("What is the value of pi?: "))
if counter == 3:
    print("The value of pie is 3.14")
else: print("You are correct")

# d
# input 3 numbers until:
# first number: 0-10
# second number: 10-60 and the average of the three numbers
# # third number: 60-100
while True:
    x: int = int(input("Enter a number between 0-10: "))
    y: int = int(input("Enter a number between 10-60: "))
    z: int = int(input("Enter a number between 60-100: "))
    if (0 <= x <= 10) and (10 <= y <= 60) and (60 <= z <= 100) and (y == (x + y + z) / 3):
        print("all conditions are met")
        break
    else: print("try again")
# # EXTRA
# BEER = 10
# ONLY 18+ CAN GET BEER
#INPUT AGE FROM USER, ONLY IF 18+ GIVE BEER, DO UNTIL ALL BEER IS GONE
beers = 10
while beers > 0:
    age: int = int(input("How old are you?: "))
    if age >= 18:
        beers -=1
        print("you get a beer")
    else:
        print("you're not legal")
# STOP
