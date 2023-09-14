import random
def main():
    #start a guessing genre game
    print ("Guess the genre! everytime you guess it right,You'll get scores and everytime you don't,you'll get chances >_<!")
    print("what's your name? let me us know!")
    name=input()
    print("we hope you'll enjoy this game")
    genre = [
        "jazz",
        "pop",
        "rock",
        "hiphop",
        "country",
        "folk",
        "r&b",
        "metal",
        "funk",
        "classical"
        ]
    x=random.choice(genre)
    max_trials=5
    trials=0
    score=100
    guess=None
    
    while trials<max_trials:
        guess= str(input("Guess which is our favourite one? :3 :     "))
        if x == guess:
            print(f"FUYOOO you so pro dooo,you get it in only {max_trials} attempts and your score is {score}! >_<".format(guess))
            score +=20
            break
        
        else:
            print("unfortunately, You got it wrong. try again la bro!".format(guess))
            print(f"you have {max_trials} chances remaining.")
            print(f"the genre has {len (x)} words")
            max_trials-=1
            score-=20
            if max_trials == 0:
                print(f"out of attempts.bapak noob pi balik la takyah main dh. the word was {x}.")
        
main()