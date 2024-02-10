# fuck hangman

import random

li_food = ["chicken", "banana", "fish", "pizza", "lemon", "bread", "jam", "cheese", "butter", "onion"]

a = random.choice(li_food)
print(a)

li_1 = ""

nobat = 9



while True:
    qustion = input("enter the word: ")
    li_1 += qustion
    if qustion not in a:
        nobat -= 1
        print(f"your chance is {nobat}")
        print("you chose wrong!")
    if nobat == 8 :
        print("""
             ++++++++++++++++++                  
             ||               |             
             ||                  
             ||                
             ||              
             ||               
             ||              
             ||     
        _____||_____""")
    if nobat == 7 :
        print("""
             ++++++++++++++++++                  
             ||               |             
             ||               |   
             ||                
             ||              
             ||               
             ||              
             ||     
        _____||_____""")
    if nobat == 6 :
        print("""
             ++++++++++++++++++                  
             ||               |             
             ||               |   
             ||               0 
             ||                   
             ||                   
             ||              
             ||     
        _____||_____""")
    if nobat == 5 :
        print("""
             ++++++++++++++++++                  
             ||               |             
             ||               |   
             ||               0 
             ||               |
             ||               
             ||                
             ||     
        _____||_____""")
    if nobat == 4 :
        print("""
             ++++++++++++++++++                  
             ||               |             
             ||               |   
             ||               0 
             ||              /|
             ||               
             ||              
             ||     
        _____||_____""")
    if nobat == 3 :
        print("""
             ++++++++++++++++++                  
             ||               |             
             ||               |   
             ||               0 
             ||              /|\\
             ||               
             ||             
             ||     
        _____||_____""")
    if nobat == 2 :
        print("""
             ++++++++++++++++++                  
             ||               |             
             ||               |   
             ||               0 
             ||              /|\\
             ||               |
             ||              
             ||     
        _____||_____""")
    if nobat == 1 :
        print("""
             ++++++++++++++++++                  
             ||               |             
             ||               |   
             ||               0 
             ||              /|\\
             ||               |
             ||              /
             ||     
        _____||_____""")
    if nobat == 0:
        print("""
             ++++++++++++++++++                  
             ||               |             
             ||               |   
             ||               0 
             ||              /|\\
             ||               |
             ||              / \\
             ||     
        _____||_____""")
        print("you lose")
        break
    counter = 0
    for i in a:
        if i in li_1:
            print(i, end=" ")
        else:
            print("_", end=" ")
            counter += 1
    if counter == 0:
        print("you win")
        break

