import random
counter = 0
print("Welcome to hangman")
secretwords = ('world', 'letter', 'desperate', 'computer', 'human', 'capital', 'lowercase', 'laptop', 'tree', 'problem', 'lol', 'weather')
word = random.choice(secretwords)
guessed = " "
output = " "
again = " "
saveG = " "


def Drawhang():
    global counter
    global word
    global again
    global saveG
    global output
    if counter == 1:
        print('''
        ----
        |
        |
        |
        |
        |
        |\\
        ------
        ''')
        print("You have made " + str(counter) + " mistakes.")
    elif counter == 2:
        print('''
        ----
        |  |
        |
        |
        |
        |
        |\\
        ------
        ''')
        print("You have already made " + str(counter) + " mistakes.")
    elif counter == 3:
        print('''
        ----
        |  |
        |  0
        |
        |
        |
        |\\
        ------
        ''')
        print("You have already made " + str(counter) + " mistakes.")
    elif counter == 4:
        print('''
        ----
        |  |
        |  0
        |  |
        |
        |
        |\\
        ------
        ''')
        print("You have already made " + str(counter) + " mistakes.")
    elif counter == 5:
        print('''
        ----
        |  |
        |  0
        | \\|
        |
        |
        |\\
        ------
        ''')
        print("You have already made " + str(counter) + " mistakes.")
    elif counter == 6:
        print('''
        ----
        |  |
        |  0
        | \\|/
        |
        |
        |\\
        ------
        ''')
        print("You have already made " + str(counter) + " mistakes.")
    elif counter == 7:
        print('''
        ----
        |  |
        |  0
        | \\|/
        | /
        |
        |\\
        ------
        ''')
    elif counter == 8:
        print('''
        ----
        |  |
        |  0
        | \\|/
        | / \\
        |
        |\\
        ------
        ''')
        print("The word was " + word)
        again = input("Do you wanna play again? \n")
        again.lower()
        if again == "yes" or again == "y":
            word = random.choice(secretwords)
            saveG = " "
            output = " "
            counter = 0
        elif again == "no" or again == "No" or again == "n" or again == "N":
            print("Okay byeee")
            counter += 1
while True:
    guessedw = True
    length = len(word)
    for l in word:
        if l in output:
            continue
        else:
            guessedw = False
    if guessedw == False:    
        for l in word:
            if l in output:
                print(l, end = "")
            elif l not in output:
                print("_ ", end = "")
        
        guessed = input("\nType a letter \n")
        guessed = guessed.lower()
        if guessed.isalpha():
            for l in guessed:
                if guessed in saveG:
                    print("You have already used this letter")
                elif guessed not in saveG:
                    saveG += guessed
                    if guessed in word:
                        output += guessed
                        print("[" + saveG + "]" + " this are all the letters you have tried.")
                        print("[" + output + "]" + " this are all your right guessed letters.")
                    elif guessed not in word:
                        print("[" + saveG + "]" + " this are all the letters you have tried.")
                        print("[" + output + "]" + " this are all your right guessed letters.")
                        counter += 1
                        Drawhang()
        else:
            print("A letter please")
    elif guessedw == True:
        print("Well done! \n You guessed the word.")
        again = input("Do you wanna play again?\n")
        again.lower()
        if again == "yes" or again == "y":
            word = random.choice(secretwords)
            saveG = " "
            output = " "
            counter = 0
        elif again == "no" or again == "n":
            print("Okay byeee")
            break
        else:
            print("Yes or no")
    if counter == 9:
        break
