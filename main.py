# ADD COMMENT REQUIREMENTS HERE
from Festival import *

# Print welcome statement
print('Welcome to "My Line-Up", an application for setting your\n own personal line-up for music festival set lists.\n');

# Print festival options 
print('Here are the upcoming festivals:\n')

print(' 1. Coachella\n 2. Stagecoach\n 3. Rolling Loud\n 4. Aftershock\n 5. Lollapalooza');

# Declare class for festival names (create new objects for each festival)

# Class for festival info

# Create objects for festivals
fest1 = Festival('Coachella', '4/26/2023', '. Awesome!', [
      ['9:00AM - 10:00AM', 'BAND'],
      ['10:00AM - 11:00AM', 'BAND'],
      ['12:00PM - 1:00PM', 'BAND'],
      ['1:00PM - 2:00PM', 'BAND'],
      ['2:00PM - 3:00PM', 'BAND'],
      ['3:00PM - 4:00PM', 'BAND'],
      ['5:00PM - 6:00PM', 'BAND'],
      ['6:00PM - 7:00PM', 'BAND'],
      ['7:00PM - 8:00PM', 'BAND'],
      ['8:00PM - 9:00PM', 'BAND'],
      ['9:00PM - 10:00PM', 'BAND']
    ])
fest2 = Festival('Stagecoach', '4/26/2023', '. Yee Haw!', [
      ['9:00AM - 10:00AM', 'BAND'],
      ['10:00AM - 11:00AM', 'BAND'],
      ['12:00PM - 1:00PM', 'BAND'],
      ['1:00PM - 2:00PM', 'BAND'],
      ['2:00PM - 3:00PM', 'BAND'],
      ['3:00PM - 4:00PM', 'BAND'],
      ['5:00PM - 6:00PM', 'BAND'],
      ['6:00PM - 7:00PM', 'BAND'],
      ['7:00PM - 8:00PM', 'BAND'],
      ['8:00PM - 9:00PM', 'BAND'],
      ['9:00PM - 10:00PM', 'BAND']
    ])
fest3 = Festival('Rolling Loud', '4/26/2023','. Rad!', [
      ['9:00AM - 10:00AM', 'BAND'],
      ['10:00AM - 11:00AM', 'BAND'],
      ['12:00PM - 1:00PM', 'BAND'],
      ['1:00PM - 2:00PM', 'BAND'],
      ['2:00PM - 3:00PM', 'BAND'],
      ['3:00PM - 4:00PM', 'BAND'],
      ['5:00PM - 6:00PM', 'BAND'],
      ['6:00PM - 7:00PM', 'BAND'],
      ['7:00PM - 8:00PM', 'BAND'],
      ['8:00PM - 9:00PM', 'BAND'],
      ['9:00PM - 10:00PM', 'BAND']
    ])
fest4 = Festival('Aftershock', '4/26/2023', '. Rock On!', [
      ['9:00AM - 10:00AM', 'BAND'],
      ['10:00AM - 11:00AM', 'BAND'],
      ['12:00PM - 1:00PM', 'BAND'],
      ['1:00PM - 2:00PM', 'BAND'],
      ['2:00PM - 3:00PM', 'BAND'],
      ['3:00PM - 4:00PM', 'BAND'],
      ['5:00PM - 6:00PM', 'BAND'],
      ['6:00PM - 7:00PM', 'BAND'],
      ['7:00PM - 8:00PM', 'BAND'],
      ['8:00PM - 9:00PM', 'BAND'],
      ['9:00PM - 10:00PM', 'BAND']
    ])
fest5 = Festival('Lollapalooza', '4/26/2023', '. Sweet!', [
      ['9:00AM - 10:00AM', 'BAND'],
      ['10:00AM - 11:00AM', 'BAND'],
      ['12:00PM - 1:00PM', 'BAND'],
      ['1:00PM - 2:00PM', 'BAND'],
      ['2:00PM - 3:00PM', 'BAND'],
      ['3:00PM - 4:00PM', 'BAND'],
      ['5:00PM - 6:00PM', 'BAND'],
      ['6:00PM - 7:00PM', 'BAND'],
      ['7:00PM - 8:00PM', 'BAND'],
      ['8:00PM - 9:00PM', 'BAND'],
      ['9:00PM - 10:00PM', 'BAND']
    ])

# Function to select appropriate festival
def festivalSelection(userFestival):
  if  userFestival == '1':
    name = fest1.name
    print('You have selected ' + fest1.name + fest1.greeting)
    print('Here is the lineup: ')
    print (fest1.lineup)

  elif (userFestival == '2'):
    name = fest2.name
    print('You have selected ' + fest2.name + fest2.greeting)
    print('Here is the lineup: ')
    print (*fest2.lineup, sep = "\n")

  elif (userFestival == '3'):
    name = fest3.name
    print('You have selected ' + fest3.name + fest3.greeting)
    print('Here is the lineup: ' + fest3.lineup)
  elif (userFestival == '4'):
    name = fest4.name
    print('You have selected ' + fest4.name + fest4.greeting)
    print('Here is the lineup: ')
    print (*fest.lineup, sep = "\n")
  elif (userFestival == '5'):
    name = fest5.name
    print('You have selected ' + fest5.name + fest5.greeting)
    print('Here is the lineup: ' + fest5.lineup)
  else: 
    print('Please enter a valid option number.')

# User input for festival choice
userFestival = input('\nWhich festival are you attending? (enter number only)\n')

festivalSelection(userFestival) 

# Function for option to return to main menu (add loop later)





# Here is the lineup for the festival
# Select 



    