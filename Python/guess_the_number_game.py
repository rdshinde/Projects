# Guess The Number Game.
# Importing buit in modules to access inbuilt functions. 
import threading
from threading import Thread
import random
class numberGuessgame():
# Initialization of intro function.
    def intro(self):
        print("                                 WELCOME TO GUESS THE NUMBER GAME!")
        #print("\n                             Set the level of difficulty as you want.")
        global playerName
        playerName=input("\n\n What's your name?\n ")
        print('\n                             WELCOME',playerName.upper(),'TO GUESS THE NUMBER GAME!')
        print('\n\n #  This is Guess the number game. First choose the range of numbers.Enter your guess and try to guess the number. When you are done enter "quit" to EXIT the game.')
        print('\n\n                                      Best of luck!!!')

# Initialization of main function which contains main part of game to be executed.
    def main(self):
            global counting,winCount
            counting = 0 # Number of attempts initialized.
            winCount=0 # Number of wincounts initialized.

            global a,b
            print("\n #Set the difficulty level with range of numbers.\n ")
            try:                                                           # Try and except error used.
                 a=int(input('* Enter starting point Number: '))
                 b=int(input('* Enter end point Number: '))
            except:
                print("* ERROR! You have entered unexpected input.\n\n")
                print(" # TRY AGAIN.")
                numberGuessgame.main(self) # Recursion of main function.
            while True:                                              # Loop is used to create random integer again and again. 
                #try:
                    global randNum,userNum
                    randNum = (random.randint(a,b))

                    userNum=int(input('* Guess the number: '))


                    if userNum<a and userNum>b:
                        print('* Please enter number in range of: ',a, '-', b)
                        continue
                    elif userNum == randNum:
                        print('Congratulations! You win!!!', 'YourNum = ',userNum,'= Random Num = ',randNum )
                        winCount=winCount+1
                        counting=counting+1
                        print('Your total attemts: ',counting)
                        print('You won',winCount,'times!!!')
                        playOrno=input('Do you want to play more? y/n ')
                        if playOrno.lower() == 'y':
                            numberGuessgame.main(self)
                        elif playOrno.lower() == 'n':
                            print('Thanks for participating. Have a nive day',playerName.upper())
                            break
                        else:
                            print('Invalid input!!!')
                    elif userNum != randNum:
                        print('You lose!, Try again.', 'YourNum = ',userNum,'!= Random Num != ',randNum )
                        counting=counting+1

                    else:
                        break
                        print('Game Over!!!')
                #except:
                #    print('Something went wrong!!!')
                #    break
    def ending(self):
        print('Your total attemts: ',counting)
        print('You won',winCount,'times!!!')

    def runall(self): # Running all the functions defined in class with defining function 'runall'.
        if __name__ == '__main__':
            Thread(target = self.intro()).start()
            Thread(target = self.main()).start()
            Thread(target = self.ending()).start()
run = numberGuessgame() # Calling last function defined in class.
run.runall() # running function using function runall.
