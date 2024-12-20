#Submission 1, CSIT101, Shreya Dhanania, 230252

#Rock, Paper, Scissors using Conditional Statements 
print("Hello, we will be playing rock paper scissors today!")
print('\n')

x = input("Player A: Enter either rock, paper or scissors ").lower()
y = input("Player B: Enter either rock, paper or scissors ").lower()

print('\n')

if x == "rock" and y == "scissors":
  print("Player A wins!")
elif x == "rock" and y == "paper":
  print("Player B wins!")
elif x == "paper" and y == "rock":
  print("Player A wins!")
elif x == "paper" and y == "scissors":
  print("Player B wins!")
elif x == "scissors" and y == "paper":
  print("Player A wins!")
elif x == "scissors" and y == "rock":
  print("Player B wins!")
else:
  print("There is a tie!")

print('\n')

#Prime Number n using For Loops and Conditional Statements
print("Now, we will check if a number is prime or not!")
print('\n')

n = int(input('Enter a number: '))
print("\n")

cnt = 0
for i in range(1,n+1):
  if n%i == 0:
    print(i,"is a factor of",n)
    cnt = cnt + 1

print("\n")

print(n, "has a total of", cnt, "factors.")    
if cnt == 2:
  print("Hence,", n,"is a prime number.")
else:
  print("Hence,", n,"is not a prime number.")