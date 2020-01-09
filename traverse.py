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
enable_traversal = True # Would you like to move around rooms to generate a map?
enable_logging = True # Enables the ability for console printing and or logging in a .json file
enable_room_prints = True # Prints a list of rooms we have been to on each loop, each time it loops there should be +1 more room
enable_json_room_log = True # Prints new rooms to the end of a .json file
enable_print_current_loop = True # Prints info about the loop, cooldowns, messages errors etc
enable_pilfer = False # Enable or disable picking up items
randomly_traverse = True # Enable Traversal for Map Generation
need_1000_gold = True # If you need 1000 gold do this
sell_items = True # If your inventory is filling up, it will sell your items automatically.

# ------

loop_count = 0
while len(copy) < 500:
  ''' JSON Room Print's & Write to File'''
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
    
    # File Writes
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
    print(f"------- Loop Number: {loop_count} -------")
    print(f"{player.name}, {player.currentRoom['description']}")
    print(f"room: {player.currentRoom['room_id']}, {player.currentRoom['title']}")
    print(f"exits: {player.currentRoom['exits']}")
    print(f"cooldown: {player.currentRoom['cooldown']}")
    print(f"messages: {player.currentRoom['messages']}")
    print(f"errors: {player.currentRoom['errors']}")
    print(f"Enemies Nearby: {player.currentRoom['players']}")
  else:
    print("Should print things only if they change from the previous loop.") # Todo, but not mvp

  ''' Pilfering '''
  if enable_pilfer is True:
    if need_1000_gold == True:
      # Look at current items
      if len(player.currentRoom['items']) > 0:
        player.pilfer()
        time.sleep(8)

  ''' Selling Items '''
  if sell_items is True:
    # If user has more than 3 small treasures, sell them
    # If user has more than 
    pass

  ''' Variables '''
  roomObj = player.currentRoom                    # Sets the current room to an Obj
  theCurrentRoom = roomObj['room_id']             # Sets the current room id to a variable
  theCurrentCooldown = roomObj['cooldown']        # Sets the cooldown period to a variable
  theCurrentExits = {}                            # Sets an in-memory Dictionary of the exits for the current room

  ''' Sleep & then get Status '''
  time.sleep(theCurrentCooldown)
  player.status()

  ''' Add's current room to copy & rooms dict '''
  # If theCurrentRoom isn't in the "copy" dict, we need to add it & the exits
  if theCurrentRoom not in copy:
    copy[theCurrentRoom] = theCurrentRoom

    # Generate a list of all of the possible exits for the current room
    for exit in player.currentRoom['exits']:
      theCurrentExits[exit] = "unknown"

    copy[theCurrentRoom] = theCurrentExits

  theCurrentExits = copy[theCurrentRoom]

  # if theCurrentRoom isn't in the "rooms" dict, we have to add it too.
  if theCurrentRoom not in rooms:
    rooms[theCurrentRoom] = theCurrentRoom # Just the rooms ID
    rooms[theCurrentRoom] = roomObj # This is the whole room Object (including user status)


  ''' Traversal Logic '''
  # Traversal Code
  if randomly_traverse is True:
    if 'n' in copy[theCurrentRoom] and theCurrentExits['n'] == 'unknown':
      print(copy[theCurrentRoom], "Currently")
      if theCurrentExits['n']=='unknown':
      #   time.sleep(curCooldown)
        player.travel("n")
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

    elif 's' in copy[theCurrentRoom]:
      print(copy[theCurrentRoom], "Currently")
      if theCurrentExits['s']=='unknown':
      #   time.sleep(curCooldown)
        player.travel("s")
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

    elif 'e' in copy[theCurrentRoom] and theCurrentExits['e'] == 'unknown':
      print(copy[theCurrentRoom], "Currently")
      if theCurrentExits['e']=='unknown':
      #   time.sleep(curCooldown)
        player.travel("e")
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

    elif 'w' in copy[theCurrentRoom] and theCurrentExits['w'] == 'unknown':
      print(copy[theCurrentRoom], "Currently")
      if theCurrentExits['w']=='unknown':
      #   time.sleep(curCooldown)
        player.travel("w")
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
    else:
      reversal = reverse.pop()
      # time.sleep(currentCooldown)
      player.travel(reversal)
      traversalPath.append(reversal)