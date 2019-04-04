import curses, os
screen = curses.initscr() #initializes a new window for capturing key presses
curses.noecho() # Disables automatic echoing of key presses (prevents program from input each key twice)
curses.cbreak() # Disables line buffering (runs each key as it is pressed rather than waiting for the return key to pressed)
curses.start_color() # Lets you use colors when highlighting selected menu option
screen.keypad(1) 


curses.init_pair(1,curses.COLOR_BLACK, curses.COLOR_WHITE) # Sets up color pair #1, it does black text with white background 

getin = None #user input on top menu
sub1get = None #user input on sub menu 1
sub2get = None #user input on sub menu 2, I don't use a second submenu, but I've left this here as an example for anyone who wants to use it

# This function controls what is displayed on the top menu (the menu first loaded when script is run)
def topmenu():

#Not sure if the following two lines are needed since I declare it at beginning of program, but here for safety
  screen.keypad(1)
  curses.init_pair(1,curses.COLOR_BLACK, curses.COLOR_WHITE)

  pos=1 #pos is the position of the hightlighted menu option.  Every time topmenu is called, position retuns to 1, when topmenu ends the position is returned and tells the program what option has been selected
  x = None #control for while loop, let's you scroll through options until return key is pressed then returns pos to program
  h = curses.color_pair(1) #h is the coloring for a highlighted menu option
  n = curses.A_NORMAL #n is the coloring for a non highlighted menu option
  
  # Loop until return key is pressed
  while x !=ord('\n'):
    screen.clear() #clears previous screen on key press and updates display based on pos
    screen.border(0)
    screen.addstr(2,2, "Program Launcher", curses.A_STANDOUT) # Title for this menu
    screen.addstr(4,2, "Please selection an option...", curses.A_BOLD) #Subtitle for this menu

    # Detects what is higlighted, every entry will have two lines, a condition if the menu is highlighted and a condition for if the menu is not highlighted
	# to add additional menu options, just add a new if pos==(next available number) and a correspoonding else
	# I keep exit as the last option in this menu, if you do the same make sure to update its position here and the corresponding entry in the main program
    if pos==1:
      screen.addstr(5,4, "1 - Dosbox Games", h)
    else:
      screen.addstr(5,4, "1 - Dosbox Games", n)
    if pos==2:
      screen.addstr(6,4, "2 - The Ur-Quan Masters", h)
    else:
      screen.addstr(6,4, "2 - The Ur-Quan Masters", n)
    if pos==3:
      screen.addstr(7,4, "3 - Windows 3.1", h)
    else:
      screen.addstr(7,4, "3 - Windows 3.1", n)
    if pos==4:
      screen.addstr(8,4, "4 - Exit", h)
    else:
      screen.addstr(8,4, "4 - Exit", n)
    screen.refresh()
    x = screen.getch() # Gets user input

    # What is user input? This needs to be updated on changed equal to teh total number of entries in the menu
	# Users can hit a number or use the arrow keys make sure to update this when you add more entries
    if x == ord('1'):
      pos = 1
    elif x == ord('2'):
      pos = 2
    elif x == ord('3'):
      pos = 3
    elif x == ord('4'):
      pos = 4
    elif x == 258:
    
    # This needs to be updated on changes to equal the total number of entries in the menu
      if pos < 4:
          pos += 1
          else: pos = 1
            elif x == 259:
            if pos > 1:
                pos += -1
        else: pos = 4
        elif x != ord('\n'):
      curses.flash()

  return ord(str(pos))

# This functions controls what is displayed on the first submenu
# See topmenu for description of code
def submenu1():
  screen.keypad(1)
  curses.init_pair(1,curses.COLOR_BLACK, curses.COLOR_WHITE)
  pos=1
  x = None
  h = curses.color_pair(1)
  n = curses.A_NORMAL
  while x !=ord('\n'):
    screen.clear()
    screen.border(0)
    screen.addstr(2,2, "Dosbox Games", curses.A_STANDOUT)
    screen.addstr(4,2, "Please selection an option...", curses.A_BOLD)

    #Detect what is higlighted
    if pos==1:
      screen.addstr(5,4, "1 - Midnight Resuce", h)
    else:
      screen.addstr(5,4, "1 - Midnight Rescue", n)
    if pos==2:
      screen.addstr(6,4, "2 - Treasure Mountain", h)
    else:
      screen.addstr(6,4, "2 - Treasure Mountain", n)
    if pos==3:
      screen.addstr(7,4, "3 - Return to Top Menu", h)
    else:
      screen.addstr(7,4, "3 - Return to Top Menu", n)
    screen.refresh()
    x = screen.getch()

    # What is user input?
    if x == ord('1'):
      pos = 1
    elif x == ord('2'):
      pos = 2
    elif x == ord('3'):
      pos = 3
    elif x == 258:
    
    # This needs to be updated on changes to equal the total number of entries in the menu
      if pos < 3:

    # This doesn't need to be changed no matter how many entries you have
	pos += 1
      else: pos = 1
    elif x == 259:
      if pos > 1:
	  pos += -1
  # This needs to be updated on changes to equal the total number of entries in the menu
      else: pos = 3
    elif x != ord('\n'):
      curses.flash()
  return ord(str(pos))

  
# Main program  
# This needs to be updated on changes equal to the number you use for exit
while getin != ord('4'): #Loop until the user chooses to exit the program
  getin = topmenu() # Get the menu item selected on the top menu
  
  if getin == ord('1'): # Top menu option 1
    #Beginning of submenu 1 control logic
	# This needs to be updated on changes equal to the number of menu items in submenu 1
    while sub1get !=ord('3'): # Loop submenu until user selects to return to top menu
      sub1get = submenu1() # Get the menu item selected on submenu 1
      if sub1get == ord('1'): #Submenu 1 option 1
	os.system('dosbox2 /path/to/EXE -conf /path/to/dosbox.conf -exit') #Launches a dosbox program, exits back to menu after program ends
      elif sub1get == ord('2'): # Submenu 2 option 2
	()
      elif sub1get == ord('3'): # Submenu 2 option 3 (Exits to top menu at this point)
	os.system('')
	#End of submenu1 control logic
	
  elif getin == ord('2'): # Topmenu option 2
    os.system('uqm')
  elif getin == ord('3'): # Topmenu option 3
    os.system('dosbox3 /path/to/my/win31/install/WINDOWS/WIN.COM -conf /path/to/my/special/dosbox2.conf -exit') #runs my win 3.1 dosbox, exits back to menu after program ends
  elif getin == ord('4'): # Topmenu option 4
    curses.endwin() #VITAL!  This closes out the menu system and returns you to the bash prompt.
