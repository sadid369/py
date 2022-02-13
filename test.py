# name ="sadid1";
# # print(len(input('what is your name')))
# print(name)

# name = "sadid2"
# print(name)

# print("hello"[4])
# print(123+345)
# True
# False
# a = input('Number  : ')
# # b = input('Number 2 : ')
# num1 = int(a[0])
# num2 = int(a[1])
# print(num1+num2)
# score = 0
# height = 1.8
# isWining = True
# print(f"your score is ${score} your height is ${height} your ${isWining}")

# ageStr= input('my age: ')
# age = int(ageStr)

# print(f"${(55-age)*365} ${(55-age)*52} ${(55-age) * 12}")
# print("welocme to rollercoaster!")
# height = int(input("what is your heiht in cm ?"))
# if height>120:
#     print('you can')
# else:
# #     print('you cna\'t')    
# print('enter height')
# height = int(input("your height"))
# if height>120:
#  print('you can')
# else:
#  print('you canot')

# height = int(input("Height: "))
# age =int( input("Age: "))
# if height >= 120:
#     if age >= 18:
#            print('12')
#     else:
#            print("7")
# else: 
#     print("you cant")            

# year = int(input('Enter Year: '))

# if year % 4 == 0:
#        if year%100 == 0:
#               if year%400 == 0:
#                print(f'So the year {year} is a leap year.') 
#               else:
#                print(f"But the year {year} is not a leap year because")        
#        else:
#               print(f'So the year {year} is a leap year.') 
      
# else:
#  print(f'So the year {year} is a leap year.')     
# 

# print("Welcome to the Love Calculator!")
# name1 = input("What is your name? \n")
# name2 = input("What is their name? \n")

# bothName = name1 + name2;
# t = bothName.lower().count("t")
# r = bothName.lower().count("r")
# u = bothName.lower().count("u")
# e = bothName.lower().count("e")

# trueTotal = t+r+u+e
# l = bothName.lower().count("l")
# o = bothName.lower().count("o")
# v = bothName.lower().count("v")
# e = bothName.lower().count("e")

# loveTotal = l+o+v+e

# result= f"{trueTotal}{loveTotal}"
# resultInt = int(result)
# if resultInt<10 or resultInt>90:
#   print(f"Your score is {resultInt}, you go together like coke and mentos.")
# elif resultInt>=40 and resultInt<=50:
#   print(f"Your score is {resultInt}, you are alright together.")
# else:
#   print(f"Your score is {resultInt}.")

# question1 = input('You\'re at a crossroad. Where do you want to go? Type "left" or "right"')
# if (question1 == "left"):
#     question2 = input('You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across.')
#     if(question2 == "wait"):
#        question3 = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?")
#        if(question3 == "red"):
#          print("Game Over")
#        elif (question3 == "blue"):
#          print("Game Over")
#        elif(question3 == "yellow"):
#          print("You Win!")
#     elif question2 == "swim":
#       print("Game Over")
# elif (question1 == "right"):
#  print("Game Over")

# import random
# import my_module

# randonInt =random.randint(0,5)
# print(randonInt)
# import random
# names_string = input("Give me everybody's names, separated by a comma. ")
# names = names_string.split(", ")
# lenth = len(names)
# index = random.randint(0,lenth-1)
# print(names[index])
# row1 = ["A","B","C"]
# row2 = ["D","E","F"]
# row3 = ["G","H","I"]
# # map = [row1, row2, row3]
# map = [row1, row2, row3 ]
# print(f"{row1}\n{row2}\n{row3}")
# position = input("Where do you want to put the treasure? ")
# row = int( position[0])-1
# colum =int( position[1])-1
# map[row][colum] ="x"

# print(f"{row1}\n{row2}\n{row3}")
# import random

# rock = '''
#     _______
# ---'   ____)
#       (_____)
#       (_____)
#       (____)
# ---.__(___)
# '''

# paper = '''
#     _______
# ---'   ____)____
#           ______)
#           _______)
#          _______)
# ---.__________)
# '''

# scissors = '''
#     _______
# ---'   ____)____
#           ______)
#        __________)
#       (____)
# ---.__(___)
# '''

# #Write your code below this line 👇

# humanInput = input("input 0 = rock, 1 = paper, 2 = scissors")
# i = int(humanInput)
# r = random.randint(0,2)
# imoji = [rock, paper, scissors]
# h = ['rock', 'paper','scissors' ]
# c = ['rock', 'paper','scissors' ]

# if(h[i] == c[r]):
#     print(f"Human :\n {imoji[i]}")
#     print(f"Computer: \n {imoji[r]}")
#     print("Game Tie")
# elif (h[i] == "rock" and c[r] == "paper"):
#     print(f"Human :\n {imoji[i]}")
#     print(f"Computer: \n {imoji[r]}")
#     print("Computer Win")
# elif (h[i] == "paper" and c[r] == 'rock'):
#     print(f"Human :\n {imoji[i]}")
#     print(f"Computer: \n {imoji[r]}")
#     print('Human Win')
# elif (h[i] == 'scissors' and c[r] == 'paper'):
#     print(f"Human :\n {imoji[i]}")
#     print(f"Computer: \n {imoji[r]}")
#     print('Human Win')
# elif (h[i] == 'paper' and c[r] == 'scissors'):
#     print(f"Human :\n {imoji[i]}")
#     print(f"Computer: \n {imoji[r]}")
#     print("Computer Win")
# elif (h[i] == 'rock' and c[r] == 'scissors'):
#     print(f"Human :\n {imoji[i]}")
#     print(f"Computer: \n {imoji[r]}")
#     print("Human Win")
# elif (h[i] == 'scissors' and c[r] == 'rock'):
#     print(f"Human :\n {imoji[i]}")
#     print(f"Computer: \n {imoji[r]}")
#     print("Computer Win")

# # 🚨 Don't change the code below 👇
# student_heights = input("Input a list of student heights ").split()
# for n in range(0, len(student_heights)):
#   student_heights[n] = int(student_heights[n])
# # 🚨 Don't change the code above 👆
  

#Write your code below this row 👇for 
# total_heght = 0
# num = 0;
# for stu in student_heights:
#     total_heght = total_heght+stu
#     num = num + 1
# print(total_heght/num)
# max_value = 0
# for x in student_heights:
#     if x> max_value:
#         max_value = x
# print(max_value)

# min_value = student_heights[0]
# for x in student_heights:
    
#     if min_value>x:
#         min_value = x
# print(min_value)
# total = 0
# for num in range(1,10,2):
#   total +=num
# print(total)
# 🚨 Don't change the code below 👇
# student_heights = input("Input a list of student heights ").split()
# for n in range(0, len(student_heights)):
#   student_heights[n] = int(student_heights[n])
# # 🚨 Don't change the code above 
# total = 0
# for num in range(1, 101):
#    if(num%3 == 0 and num%5 == 0):
#      print('Fizz Buzz')  
#    elif(num%3 == 0):
#      print("Fizz")
#    elif(num%5 ==0):
#      print("Buzz")
#    else:
#      print(num)

#Password Generator Project
# import random
# letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# print("Welcome to the PyPassword Generator!")
# nr_letters= int(input("How many letters would you like in your password?\n")) 
# nr_symbols = int(input(f"How many symbols would you like?\n"))
# nr_numbers = int(input(f"How many numbers would you like?\n"))

# #Eazy Level - Order not randomised:
# #e.g. 4 letter, 2 symbol, 2 number = JduE&!91
# password = ""
# for char in range(1, nr_letters +1):
#   random_letter = random.choice(letters)
#   password += random_letter
#   # print(password)
# for char in range(1, nr_symbols +1):
#   random_symbols = random.choice(symbols)
#   password += random_symbols
#   # print(password)
# for char in range(1, nr_numbers +1):
#   random_number = random.choice(numbers)
#   password += random_number
#   # print(password)
# random_password = []
# for char in range(0, (nr_letters+nr_symbols+nr_numbers)):
#   random_password.append(password[char])
# print(random_password)
# shuffleList = random.shuffle(random_password)
# finalPass = ""
# for char in random_password:
#   finalPass += char
# print(finalPass)
 

# #Hard Level - Order of characters randomised:
# #e.g. 4 letter, 2 symbol, 2 number4 = g^2jk8&P2

#Step 1 
# import random

# word_list = ["aardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
# chosen_word = random.choice(word_list)

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
# guess = input("Guess a word ").lower()

# #TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
# # chosenWordList = []
# # for char in range(0, len(chosen_word)):
# #     chosenWordList.append(chosen_word[char])
# for letter in chosen_word:
#   if guess == letter:
#     print("Right")
#   else:
#     print("wrong")
# print(chosen_word)
import random 
from hangman_words import word_list
from hangman_art import logo , stages


# word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

print(f'Pssst, the solution is {logo}.')
print(f'Pssst, the solution is {chosen_word}.')
#Testing code

#TODO-1: - Create an empty List called display.
#For each letter in the chosen_word, add a "_" to 'display'.
#So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.
display = []
word_length = len(chosen_word)
for _ in range(word_length):
  display += "_"

lives = 6
end_of_game = True 
while end_of_game:
   guess = input("Guess a letter: ").lower()

   

   for position in range(word_length):
         letter = chosen_word[position]
         if letter == guess:
          display[position] = letter
   print(display)
   if "_" not in display:
            end_of_game = False
            print("you won")
   elif guess not in display:
     print(stages[lives])
     lives -= 1
     if lives <0 :
       end_of_game = False
       print("you lose")
    #TODO-3: - Print 'display' and you should see the guessed letter in the correct position and every other letter replace with "_".
#Hint - Don't worry about getting the user to guess the next letter. We'll tackle that in step 3.