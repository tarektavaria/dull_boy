#!/usr/bin/python
# -*- coding: UTF-8 -*-

##################################
# Filename:         dull_boy.py  #
# Author:           Chris Snyder #
# Created:			       18-JUN-2019  #
# Last Modified:	   25-JUN-2019  #
# Python Version:	  2.7.5        #
##################################

import os
import random
import string
import sys
import time

ALPHANUMERIC_CHARS = string.letters + string.digits + string.punctuation

DEFAULT_LANGUAGE = 'english'
MESSAGES = {
 'english'  : 'All work and no play makes Jack a dull boy. ',
  'italian' : 'Il mattino ha l\'oro in bocca. ',
  'german'  : 'Was du heute kannst besorgen, das vershiebe nicht auf morgen. ',
  'spanish' : 'No por mucho madrugar amanece más temprano. ',
  'french'  : 'Un Tiens vaut mieux que deux Tu l\'auras. '
}

SANITY_LOSS		= True
SANITY_LOSS_RATE	= 0.01
SANITY_STARTING		= 100.0

TYPING_ERROR_RATE	= 0.005
TYPING_MODIFIER		= 0.25
TYPING_PAUSE_RATE	= 0.05

sanity = SANITY_STARTING

def typewriter(language):
 for count, character in enumerate(MESSAGES[language]):
  if random.random() < TYPING_ERROR_RATE * SANITY_STARTING / sanity:
   character = random.choice(ALPHANUMERIC_CHARS)
   
  sys.stdout.write(character)
  sys.stdout.flush()
  
  pause_time = random.random() * TYPING_MODIFIER
  
  if character == ' ' and random.random() < TYPING_PAUSE_RATE:
   pause_time += random.random()
   
  time.sleep(pause_time)
  
def sanity_check():
 global sanity
 
 if not SANITY_LOSS:
  return
  
 if sanity > 1 and random.random() < SANITY_LOSS_RATE:
  sanity -= 1
  
def main():
 os.system('clear')
 
 language = DEFAULT_LANGUAGE
 
 if len(sys.argv) == 2:
  language = str(sys.argv[1])
  
 while(True):
  typewriter(language)
  sanity_check()
  
if __name__ == '__main__':
 main()
