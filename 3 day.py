# 🧑‍💻Example 1: Age Checker

age = int(input("Enter your age: "))

if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")


#🖥️ Output (if age = 20):
# Enter your age: 20
# You are eligible to vote.

# 🧑‍💻 Example 2: Number is Positive, Negative or Zero

num = int(input("Enter a number: "))

if num > 0:
    print("Number is positive")
elif num < 0:
    print("Number is negative")
else:
    print("Number is zero")
    
# 🖥️ Output (if num = -5):
# enter a number: -5
# Number is negative


# 🧑‍💻 Example 3: Print even numbers from 2 to 10

for i in range(2, 11, 2):
          print(i)
    
# 🖥️ Outpu      
# 2
# 4
# 6
# 8
# 10


# 🧑‍💻 Example 4: Print reverse from 5 to 1 using while loop
num = 5
while num >= 1:
    print(num)
    num -= 1

# 🖥️ Output:
# 5
# 4
# 3
# 2
# 1






