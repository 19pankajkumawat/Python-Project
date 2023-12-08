# import random
# n = random.randrange(5,20)
# guess = int(input("Enter any number: "))
# while guess: # n!= guess:
#     if guess < n:
#         print("Too low")
#         guess = int(input("Enter number again: "))
#     elif guess > n:
#         print("Too high!")
#         guess = int(input("Enter number again: "))
#     else:
#       break
# print(f"You WON  you guessed it right!!")

list1 = [12, 16, 20, 20, 12, 30, 25, 23, 24, 20]

m1 = list1[len(list1)//2]
m2 = list1[len(list1)//2 - 1]

median = (m1 + m2)/2
median = list1[len(list1)//2]
print(median)