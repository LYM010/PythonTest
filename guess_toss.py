#!/usr/bin/env python3
# -*-UTF-8-*-
import logging
logging.basicConfig(level=logging.DEBUG,format='%(asctime)s - %(levelname)s - %(message)s')

import random
logging.debug('Start of Program')
guess = ''
while guess not in('heads','tails'):
    print('Guess the coin toss! Enter heads or tails:')
    guess = input()
    toss = random.randint(0,1) # 0 is tails, 1 is heads
    logging.debug(f'guess is {guess}, toss is {toss}') 
    if toss == guess:
        print ('You got it!')
    else:
        print('Nope! Guess again!')
        guess = input()
        logging.debug(f'guess is {guess}, toss is {toss}') 
        if toss == guess:
            print('You got it!')
        else:
            print('Nope.You are really bad at this game.')
logging.debug('End of program')
                
              
