import random
import os

#MESSAGE TO THE USER
print("WELCOME TO THE WORD PUZZLE GAME")
print("Game Rules:")
print("1. Five Suffled Words Were Given")
print("2. Arrange All The Words To Form A Meaningfull Word")
print("3. For Each Correct Answer You will Get +1 Score")
print("4. For Each Wrong Answer You will Get -1 Score")
input("Hit Enter To Start The Game")
os.system("cls")
print("Game Started...")
print()

#LOGIC PART
list_Of_Words=["CONTINUE","KEYWORD","ARGUMENT","BREAK","FATHER","GREEN","AEROPLANE","DEADLOCK"]
random.shuffle(list_Of_Words)
score=0
count=0
for word in list_Of_Words:
    word_into_list=list(word)
    random.shuffle(word_into_list)
    for e in word_into_list:
        print(e,end="")
    print()
    answer=(str(input())).upper()
    if word==answer:
        print("Correct")
        score+=1
        print()
    else:
        print("Wrong")
        score-=1
        print()
    count+=1
    if count==5:
        break
print("Gave Over")
print("Net Score =",score)
