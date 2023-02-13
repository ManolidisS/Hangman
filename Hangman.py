version = "1.0.1 (ASCII update)"
from random import choice

words = ['books', 'verse', 'bird', 'advise', 'wandering', 'contain', 'oven', 'economic', 'deserve', 'food', 'defective', 'high', 'moan', 'flag', 'doll', 'wash', 'burn', 'thrill', 'exclusive', 'bells', 'nervous', 'faithful', 'settle', 'zipper', 'plan', 'desert', 'instrument', 'fallacious', 'distance', 'pot', 'car', 'respect', 'minute', 'used', 'reminiscent', 'slave', 'ink', 'stale', 'shallow', 'thinkable', 'reading', 'spade', 'veil', 'fireman', 'abounding', 'rhetorical', 'believe', 'heal', 'tip', 'cloth', 'delay', 'clumsy', 'wave', 'neat', 'shrill', 'wish', 'flippant', 'silly', 'dramatic', 'upset', 'prick', 'crowded', 'sidewalk', 'tug', 'fantastic', 'wonder', 'join', 'pastoral', 'pop', 'complain', 'wacky', 'aware', 'visitor', 'dispensable', 'judicious', 'laborer', 'concerned', 'cabbage', 'wink', 'argument', 'remind', 'trust', 'test', 'side', 'glib', 'surround', 'start', 'slip', 'ajar', 'alike', 'example', 'voiceless', 'bewildered', 'scandalous', 'classy', 'friends', 'direful', 'lopsided', 'raspy', 'cat']
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def hangman_ascii(lifes):
    if lifes == 0:
        ascii_art = '''______________
|            |
|            O
|           /|\\
|           | |
|
|_____________'''
        return ascii_art
    elif lifes == 1:
        ascii_art = '''______________
|            |
|            O
|           /|\
|           | 
|
|_____________'''
        return ascii_art
    elif lifes == 2:
        ascii_art = '''______________
|            |
|            O
|           /|\
|  
|
|_____________'''
        return ascii_art
    elif lifes == 3:
        ascii_art = '''______________
|            |
|            O
|           /|
|           
|
|_____________'''
        return ascii_art
    elif lifes == 4:
        ascii_art = '''______________
|            |
|            O
|            |
|           
|
|_____________'''
        return ascii_art
    elif lifes == 5:
        ascii_art = '''______________
|            |
|            O
|
|           
|
|_____________'''
        return ascii_art
    elif lifes == 6:
        ascii_art = '''______________
|            |
|            
|          
|           
|
|_____________'''
        return ascii_art
    elif lifes == 7:
        ascii_art = '''______________
|            
|            
|         
|           
|
|_____________'''
        return ascii_art
    elif lifes == 8:
        ascii_art = '''_______
|            
|            
|         
|           
|
|_____________'''
        return ascii_art
    elif lifes == 9:
        ascii_art = '''
|            
|            
|         
|           
|
|_____________'''
        return ascii_art
    elif lifes >= 10:
        ascii_art = '''_____________'''
        return ascii_art

def hangman(lifesParameter):
    lifes = lifesParameter
    word = choice(words)
    wordLetters = [*word]
    correctLetters = []
    for i in range(len(wordLetters)):
        correctLetters.append("")
    incorrectLetters = []
    while correctLetters != wordLetters:
        print(f"Lifes left: {lifes}")
        print(f"{hangman_ascii(lifes)}")
        for i in range(len(wordLetters)):
            if correctLetters[i] == wordLetters[i]:
                print(wordLetters[i],end=" ")
            else:
                print("_",end=" ")
        letterGuessed = input("\nGuess a letter: ").lower()
        if letterGuessed in wordLetters:
            print(f"Well done! Your guess: {letterGuessed} was in the word!")
            for i in range(len(wordLetters)):
                if letterGuessed == wordLetters[i]:
                    correctLetters[i] = letterGuessed
        elif letterGuessed not in wordLetters:
            print("Incorrect, sorry. You lost a life!")
            lifes = lifes - 1
        if lifes <= 0:
            break
    if lifes <= 0:
        print(f"{hangman_ascii(lifes)}")
        print(f"You lost, sorry!, the word was {word}.")
    else:
        print(f"Lifes: {lifes}\n{hangman_ascii(lifes)}")
        print(f"You won, the word was {word}. Yay!")
    print("--------------------")



print(f"Hello! This is a simple hangman game made by Spyridon Manolidis. Version {version}.")
print("Update: 1 day after the original was made, I added ascii, you're welcome!")
print("Don't judge I made this when 12. (13 in a month woooooo)!")

while True:
    option = input("Do you want to play hangman (yes/no)?\n").lower()
    if option in ["yes", "y", "true"]:
        option = input("What mode (Easy, Medium, Hard, DEVTEST)?\n")
        if option.lower() in ["easy", "e", "ez"]:
            hangman(10)
        elif option.lower() in ["medium", "m", "med"]:
            hangman(7)
        elif option.lower() in ["hard", "h", "ha"]:
            hangman(10)
        elif option.lower() == "devtest":
            hangman(10**10)
        else:
            print("Invalid Option.")
    elif option in ["no", "n", "false"]:
        break
    else:
        print("Sorry you entered something invalid.\nThe options are: (Yes, Y, True) or (No, N, False).\nPlease try again.\n")
    

exit()