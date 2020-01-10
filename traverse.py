from player import Player
import time
import os.path
import json

player=Player('Jtonna', 0)
player.init()

traversalPath = []
copy={}
rooms={}
reverse=[]

# ------------------------------ SETTINGS ---------------------------#
# True = on, False = off
# ---------------------
test = False                             # Sleep & then test some code & then sleep for 5000 seconds
enable_traversal = True                  # Would you like to move around rooms?
enable_logging = True                    # Enables the ability for console printing and or logging in a .json file
enable_room_prints = False               # Prints a list of rooms we have been to on each loop, each time it loops there should be +1 more room
enable_json_room_log = True              # Prints new rooms to the end of a .json file
eval_prints = True                       # See the logic as it runs
enable_print_current_loop = True         # Prints info about the loop, cooldowns, messages errors etc
enable_pilfer = False                    # Enable or disable picking up items
need_1000_gold = False                   # If you need 1000 gold do this

# These settings will require "randomly_traverse" to be True & will set it to True if it is not already
sell_items = False                       # Would you like to sell items??.
change_name = True                       # If you need to change your name.

# --------------------------------------------------------------------
loop_count = 0
while len(copy) < 500:

  ''' Testing '''
  if test is True:
    time.sleep(player.currentRoom['cooldown'])
    player.status()
    print("************")
    # Code to test here
    print("************")

    # Sleep for a bit
    time.sleep(5000)

  ''' JSON Room Print's & Write to File's'''
  if enable_logging is True:

    # Console Prints copy & then rooms
    if enable_room_prints is True:

      # Copy of Rooms
      print("Copy of Rooms ---")
      if len(copy) == 0:
        print("    Copy is empty", copy)
      else:
        print(    copy)
      
      # Rooms
      print("Rooms ---")
      if len(rooms) == 0:
        print("    Rooms is empty", rooms)
      else:
        print(    rooms)
    
    # Write JSON Log
    if enable_json_room_log is True:

      # If the file we are looking for exists we can write to it, else we have to create it and then write to it.
      if os.path.isfile(f"{player.name}s_room_log.json"):
        f = open(f"{player.name}s_room_log.json", "a+")
        fixedJSON = json.dumps(player.currentRoom)
        f.write(f"{fixedJSON},\n")
        f.close()
      else:
        # Create the file, set player.currentRoom to a string & replace all ' with " then write the string to the file
        f = open(f"{player.name}s_room_log.json", "w+")
        fixedJSON = json.dumps(player.currentRoom)
        f.write(f"{fixedJSON},\n")
        f.close()

  ''' Current loop Prints '''
  if enable_print_current_loop is True:
    loop_count = loop_count +1
    print("\n")
    print(f"------- Loop Number: {loop_count} ------- sleep: {player.currentRoom['cooldown']}")
    print(f"{player.name}, {player.currentRoom['description']}")
    print(f"room: {player.currentRoom['room_id']}, {player.currentRoom['title']}")
    print(f"exits: {player.currentRoom['exits']}")
    print(f"cooldown: {player.currentRoom['cooldown']}")
    print(f"messages: {player.currentRoom['messages']}")
    print(f"errors: {player.currentRoom['errors']}")
    print(f"Enemies Nearby: {player.currentRoom['players']}")
  else:
    print("Should print things only if they change from the previous loop.") # Todo, but not mvp

  ''' Variables '''
  roomObj = player.currentRoom                                 # Sets the current room to an Obj
  theCurrentRoom = roomObj['room_id']                          # Sets the current room id to a variable
  theCurrentCooldown = roomObj['cooldown']                     # Sets the cooldown period to a variable
  theCurrentExits = {}                                         # Sets an in-memory Dictionary of the exits for the current room
  #inventoryItems = player.currentStatus['inventory']           # List of items in your inventory

  ''' Sleep & then update Status '''
  time.sleep(theCurrentCooldown)
  player.status()

  ''' Pilfering '''
  if enable_pilfer is True:
    if need_1000_gold == True:
      if len(player.currentRoom['items']) > 0:
        player.pilfer()
        time.sleep(8)

  ''' Add's current room to copy & rooms dict '''
  # If theCurrentRoom isn't in the "copy" dict, we need to add it & the exits
  print(f"exits: {theCurrentExits}, true_exits: {player.theCurrentRoom['exits']}")
  if theCurrentRoom not in copy:
    copy[theCurrentRoom] = theCurrentRoom

    # Generate a list of all of the possible exits for the current room and set its value to 'unknown'
    for xit in player.currentRoom['exits']:
      theCurrentExits[xit] = "unknown"

    copy[theCurrentRoom] = theCurrentExits
  theCurrentExits = copy[theCurrentRoom]

  # if theCurrentRoom isn't in the "rooms" dict, we have to add it too.
  if theCurrentRoom not in rooms:
    rooms[theCurrentRoom] = theCurrentRoom # Just the rooms ID
    rooms[theCurrentRoom] = roomObj # This is the whole room Object (including user status)

  ''' Selling Items '''
  if sell_items is True:
    ways_to_store=["0", "4", "10", "125", "262"]

    # Disable traversal if its Enabled & if we know how to get to the store
    if enable_traversal is True and theCurrentRoom in ways_to_store:
      print("**** Warning: enable_traversal is enabled, we want to pause after we sell items, so now we are going to to disable it in-memory for this session..")
      enable_traversal = False
    
    # Function to sell items
    def time_to_sell():
      items_looped_over = 0
      item_to_loop_over = len(player.currentStatus['inventory'])
      for item in player.currentStatus['inventory']:
        time.sleep(theCurrentCooldown)
        print(f"attempting to sell {item}, item's left:{items_looped_over - item_to_loop_over}")
        player.sell()
        time.sleep(5)
        items_looped_over = + 1
      print(f"All items sold, {player.currentStatus['inventory']}")
      print("Initializing 10 hour sleep")
      time.sleep(36000)

    # 262 - > Store
    if theCurrentRoom == 262:
      directions = ["n","n","w","n","w","s","w","w","n","n","n","n","n","n","w","n","w"]
      for x in directions:
        player.sleep(theCurrentCooldown)
        player.travel(x, theCurrentRoom)
      time_to_sell()

    # 125 -> Store
    if theCurrentRoom == 125:
      directions = ["e","s","e","s","s","s","s","s","s","w"]
      for x in directions:
        player.sleep(theCurrentCooldown)
        player.travel(x, theCurrentRoom)
      time_to_sell()
    
    # 10 -> Store
    if theCurrentRoom == 10:
      directions = ["s","w"]
      for x in directions:
        player.sleep(theCurrentCooldown)
        player.travel(x, theCurrentRoom)
      time_to_sell()
    
    # room 4 -> store
    if theCurrentRoom == 4:
      directions = ["e","w"]
      for x in directions:
        player.sleep(theCurrentCooldown)
        player.travel(x, theCurrentRoom)
      time_to_sell()

    # 0 -> Store
    if theCurrentRoom == 0:
      time.sleep(theCurrentCooldown)
      player.travel("w", theCurrentRoom)
      time.sleep(theCurrentCooldown)
      time_to_sell()

  ''' Change Name '''
  if change_name is True:
    ways_to_name_changer = ["467", "100", "", ""]

    # Enable traversal in-memory to find name-changing rooms
    if enable_traversal is False:
      print("enable_traversal is False, were going to set it to True in-memory to be able to look for ways to the name changer.")
      enable_traversal = True

    # Checking to see if the player has enough gold.
    if player.currentStatus['gold'] < 1000:
      print("You dont have enough gold to change your name, please traverse and pickup items for a while and then try to find the store.")
      print("Sleeping for 10 hours.")
      time.sleep(36000)
      
    # function to change name
    def attempt_name_change():
      if player.currentStatus['gold'] >= 1000:
        print(f"You have {player.currentStatus['gold']} gold. lets change your name.")
        print("Please configure player.py's change_name function. Press enter to continue or ctrl+c to terminate.")
        input()
        time.sleep(player.currentRoom['cooldown'])
        player.name_change()
        time.sleep(35)
        player.status()
        print("Sleeping for 10 hours")
        time.sleep(360000)
    
    if theCurrentRoom == 100:
      path_to_changer = ["e","s","e","e","e","s","s","s","s","s"]
      for x in path_to_changer:
        time.sleep(theCurrentCooldown)
        player.travel(x,theCurrentRoom['room_id'])
      pass

    if theCurrentRoom == 467:
      attempt_name_change()

  ''' Traversal Logic '''
  if enable_traversal is True:

    # Variable for the current room's exits
    directions_to_check = player.currentRoom['exits']

    # Only check the avaliable exits
    for possible_direction in directions_to_check:
      # Evaluate Logic as it runs
      if eval_prints is True:
        print(f"    Evaluating the {possible_direction} room")
        print(f"    Looking for room:{theCurrentRoom} in copy:{copy[theCurrentRoom]}")

      if possible_direction not in copy[theCurrentRoom]:
        # Evaluate logic as it runs
        if eval_prints is True:
          print(f"    current direction to check: {possible_direction}.")
        
        # If we dont know what room_id is at the current direction we are looking at, we will move there.
        if theCurrentExits[possible_direction] == 'unknown':
          # Evaluate Logic
          if eval_prints is True:
            print(f"        the room {possible_direction} of us should be unknown:{theCurrentExits[possible_direction]}, lets move there.")
          
          # Move to the unknown room
          player.travel(possible_direction, theCurrentRoom)
          # Log the move so we can see the path we took.
          traversalPath.append(possible_direction)

          # Log the oppisite direction in the reverse list
          if possible_direction == "n":
            reverse.append("s")
          elif possible_direction == "e":
            reverse.append("w")
          elif possible_direction == "s":
            reverse.append("n")
          else:
            reverse.append("e")

      # Since all of the directions are known, were going to have to go back until we find an unknown direction
      else:
        if eval_prints is True:
          print(f"**Attempting reversal from {player.currentRoom['room_id']}")
          print(f"** reverse: {reverse}")
        reversal = reverse.pop()
        player.travel(reversal)
        traversalPath.append(reversal)

  # Traversal Code
  if enable_traversal is False:
    print(f"    current exits: {theCurrentExits}")
    # Go north
    if 'n' in copy[theCurrentRoom]:
      #Eval Print
      if eval_prints is True:
        print(f"    evaluating going north from {theCurrentRoom}")
        print(f"        current exits: {theCurrentExits['n']}, if the exit is 'unknown' it will move to that room.")

      if theCurrentExits['n'] == 'unknown':
        # Eval Print
        if eval_prints is True:
          print(f"    moving north from {theCurrentRoom}.")

        player.travel("n", theCurrentRoom)
        traversalPath.append("n")

        newRoom=player.currentRoom['room_id']
        theCurrentExits['n']=newRoom
        newExits={}

        if newRoom not in copy:
          for exit in player.currentRoom['exits']:
            newExits[exit]="unknown"
            copy[newRoom]=newExits
          newExits['s']=theCurrentRoom
        reverse.append('s')

    # Go South
    elif 's' in copy[theCurrentRoom]:
      # Eval Print
      if eval_prints is True:
        print(f"    evaluating going south from {theCurrentRoom}")
        print(f"        current exits: {theCurrentExits['s']}, if the exit is 'unknown' it will move to that room.")

      if theCurrentExits['s'] == 'unknown':
        # Eval Prints
        if eval_prints is True:
          print(f"    moving south from {theCurrentRoom}")

        player.travel("s", theCurrentRoom)
        traversalPath.append("s")
        newRoom=player.currentRoom['room_id']
        theCurrentExits['s']=newRoom
        newExits={}
        if newRoom not in copy:
          for exit in player.currentRoom['exits']:
            newExits[exit]="unknown"
            copy[newRoom]=newExits
          newExits['n']=theCurrentRoom
        reverse.append('n')

    # Go East
    elif 'e' in copy[theCurrentRoom]:
      # Eval Print
      if eval_prints is True:
        print(f"    evaluating going east from {theCurrentRoom}")
        print(f"        current exits: {theCurrentExits['e']}, if the exit is 'unknown' it will move to that room.")

      if theCurrentExits['e'] == 'unknown':
        # Eval Prints
        if eval_prints is True:
          print(f"    moving east from {theCurrentRoom}")
          
        player.travel("e", theCurrentRoom)
        traversalPath.append("e")
        newRoom=player.currentRoom['room_id']
        theCurrentExits['e']=newRoom
        newExits={}
        if newRoom not in copy:
          for exit in player.currentRoom['exits']:
            newExits[exit]="unknown"
            copy[newRoom]=newExits
          newExits['w']=theCurrentRoom
        reverse.append('w')

    # Go West
    elif 'w' in copy[theCurrentRoom]:
      # Eval Print
      if eval_prints is True:
        print(f"    evaluating going west from {theCurrentRoom}")
        print(f"        current exits: {theCurrentExits['w']}, if the exit is 'unknown' it will move to that room.")

      if theCurrentExits['w'] == 'unknown':
        # Eval Prints
        if eval_prints is True:
          print(f"    going west from {theCurrentRoom}")
          
        player.travel("w", theCurrentRoom)
        traversalPath.append("w")
        newRoom=player.currentRoom['room_id']
        theCurrentExits['w']=newRoom
        newExits={}
        if newRoom not in copy:
          for exit in player.currentRoom['exits']:
            newExits[exit]="unknown"
            copy[newRoom]=newExits
          newExits['e']=theCurrentRoom
        reverse.append('e')
    
    # Reverse
    else:
      print(f"**Attempting reversal from {player.currentRoom['room_id']}")
      reversal = reverse.pop()
      # time.sleep(currentCooldown)
      player.travel(reversal)
      traversalPath.append(reversal)