#importing library that will allo wto randomly choose number
from random import randint
#asking the user for input
player = input('rock (r), paper (p) or scissors (s)?')

#setting the computer choices based on the random number
chosen = randint(1,3)
if chosen == 1:
    computer = 'r'
elif chosen ==2:
    computer = 'p'
elif chosen ==3:
    computer ='s'
#printing the outcome
print (player,'vs', computer)

#printing who won and who lost (result of outcome)
if computer == player:
    print ('its a tie')
    
elif (computer == 'r' and player =='p'):
    print ('you win!')
elif (computer == 'p' and player =='r'):
    print ('computer wins')
    
elif (computer == 's' and player =='p'):
    print ('computer wins')
elif (computer == 'p' and player =='s'):
    print ('you win!')
    
elif (computer == 'r' and player =='s'):
    print ('computer wins')
elif (computer == 's' and player =='r'):
    print ('you win!')   
