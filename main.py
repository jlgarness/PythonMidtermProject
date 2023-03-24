# ADD COMMENT REQUIREMENTS HERE
from festivalClass import *
from festivalObjects import *



# festInfo function to call within festivalSelection
def festInfo(obj):
  print('\nYou have selected ' + obj.name + obj.greeting)
  print('\nHere is the lineup for ' + obj.name + ':\n')
  for i in obj.lineup :
      print( i, "-------------", obj.lineup[i], sep = '\t') 


# Function to select appropriate festival
def festivalSelection(userFestival):
  if  userFestival == '1':
    festInfo(fest1)
    
  elif (userFestival == '2'):
    festInfo(fest2)

  elif (userFestival == '3'):
    festInfo(fest3)
      
  elif (userFestival == '4'):
    festInfo(fest4)

  elif (userFestival == '5'):
    festInfo(fest5)

# Function to check valid entry
def isValidEntry(input):
  if (input) == 1 or 2 or 3 or 4 or 5:
    return True
      
  
      
  
# User input for festival choice
run = True

while run == True:

  # Print welcome statement
  print('\nWelcome to "My Line-Up", an application for setting your\n own personal line-up for music festival set lists.\n');

  # Print festival options 
  print('Here are the upcoming festivals:\n')
  print(' 1. ' + fest1.name + '\n 2. ' + fest2.name + '\n 3. ' + fest3.name + '\n 4. '   + fest4.name + '\n 5. ' + fest5.name);

  # Get user input
  userFestival = input('\nWhich festival are you attending? (enter valid number only)\n')

  # Check if valid entry  
  while isValidEntry(userFestival):
    festivalSelection(userFestival)
    break
    #continue
    
  restart = input('\nWould you like to try again? If so, type "Yes".\n\n')
  if restart == "yes" or "Yes":
    print('\nOk, restarting...')
    run == True
  else:
    print('Ok. See you soon! Enjoy your show.')
    run == False
    break
      
       
  
  






# Try again do-while loop for option to return to main menu (add loop later)
# Loop for error message
# Function for selecting and printing only desired sets


    