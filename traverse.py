from player import Player
import time
import os.path
import json

player=Player('Jtonna', 0)
player.init()
#-------------------------------- NAME CHANGE ------------------------------#
# if player.currentRoom['room_id'] == 467:
#   time.sleep(player.currentRoom['cooldown'])
#   player.name_change()
#   time.sleep(35)
#   player.status()
#-------------------------------- STORE / From room_id 63 ------------------------------#
#-------------------------------- STORE / From room_id 0 ------------------------------#
# time.sleep(player.currentRoom['cooldown'])
# # player.travel("w")
# # time.sleep(player.currentRoom['cooldown'])
# player.sell()
# time.sleep(5)
# player.status()
# ------------------------------ DROP -------------------------------#
# time.sleep(player.currentRoom['cooldown'])
# player.drop()
# time.sleep(10)
# player.status()
# ------------------------------ TRAVERSAL --------------------------#
traversalPath = []
#-----------
copy={}
rooms={}
reverse=[]
#-----------

# ------------------------------ SETTINGS ---------------------------#
# True = on, False = off
enable_traversal = True # Would you like to move around rooms to generate a map?
enable_logging = True # Enables the ability for console printing and or logging in a .json file
enable_console_prints = True
enable_json_room_log = True # Prints new rooms to the end of a .json file
enable_print_current_loop = True # Prints info about the loop, cooldowns, messages errors etc
enable_pilfer = True # Enable or disable picking up items

# ------

loop_count = 0
while len(copy) < 500:

  ''' JSON Room Print's & Write to File'''
  if enable_logging is True:

    # Console Prints copy & then room
    if enable_console_prints is True:

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
              print(f"file exists")
      else:
        # Create the file, set player.currentRoom to a string & replace all ' with " then write the string to the file
        f = open(f"{player.name}s_room_log.json", "w+")
        fixedJSON = json.dumps(player.currentRoom)
        f.write(f"{fixedJSON}")
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


  # print("----------------------Current room in while loop----------------", player.currentRoom)
  if player.currentRoom is not None:
    if player.currentRoom['room_id'] == 63:
      time.sleep(player.currentRoom['cooldown'])
      player.travel("s")
      time.sleep(player.currentRoom['cooldown'])
      player.travel("s")
      time.sleep(player.currentRoom['cooldown'])
      player.travel("s")
      time.sleep(player.currentRoom['cooldown'])
      player.travel("s")
      time.sleep(player.currentRoom['cooldown'])
      player.travel("w")
      time.sleep(player.currentRoom['cooldown'])
      player.sell()
      time.sleep(5)
      player.status()
  # if player.currentRoom['room_id'] == 467:
#   time.sleep(player.currentRoom['cooldown'])
#   player.name_change()
#   time.sleep(35)
#   player.status()
  curCooldown=player.currentRoom['cooldown']
  time.sleep(curCooldown)
#   if len(player.currentRoom['items']) > 0:
#     player.pilfer()
#     time.sleep(8)
  time.sleep(2)
  player.status()
  time.sleep(2)
  curRoom=player.currentRoom['room_id']
  if curRoom not in copy:
    copy[curRoom]=curRoom
    curExits={}
    for exit in player.currentRoom['exits']:
      curExits[exit]="unknown"
    copy[curRoom]=curExits
  curExits=copy[curRoom]
  if curRoom not in rooms:
      rooms[curRoom]=curRoom
      roomObj=player.currentRoom
      rooms[curRoom]=roomObj
# Break for finding name changer
#   if player.currentRoom['room_id']==467:
#       print("****************NAME CHANGE*******************************")
#       break
# Breaks for finding store, west of 0
  # if player.currentRoom['room_id']==0:
  #     print("****************SELL*******************************")
  #     break
  # if player.currentRoom['room_id']==10:
  #     print("****************SELL*******************************")
  #     break
  # if player.currentRoom['room_id']==19:
  #     print("****************SELL*******************************")
  #     break
  # if player.currentRoom['room_id']==20:
  #     print("****************SELL*******************************")
  #     break
  # if player.currentRoom['room_id']==63:
  #     print("****************SELL*******************************")
  #     break
  # if player.currentRoom['title']=='shop':
  #     print("****************SELL*******************************")
  #     break
  if 'n' in copy[curRoom] and curExits['n'] == 'unknown':
    print(copy[curRoom], "Currently")
    if curExits['n']=='unknown':
    #   time.sleep(curCooldown)
      player.travel("n")
      traversalPath.append("n")
      newRoom=player.currentRoom['room_id']
      curExits['n']=newRoom
      newExits={}
      if newRoom not in copy:
        for exit in player.currentRoom['exits']:
          newExits[exit]="unknown"
          copy[newRoom]=newExits
        newExits['s']=curRoom
      reverse.append('s')

  elif 's' in copy[curRoom] and curExits['s'] == 'unknown':
    print(copy[curRoom], "Currently")
    if curExits['s']=='unknown':
    #   time.sleep(curCooldown)
      player.travel("s")
      traversalPath.append("s")
      newRoom=player.currentRoom['room_id']
      curExits['s']=newRoom
      newExits={}
      if newRoom not in copy:
        for exit in player.currentRoom['exits']:
          newExits[exit]="unknown"
          copy[newRoom]=newExits
        newExits['n']=curRoom
      reverse.append('n')

  elif 'e' in copy[curRoom] and curExits['e'] == 'unknown':
    print(copy[curRoom], "Currently")
    if curExits['e']=='unknown':
    #   time.sleep(curCooldown)
      player.travel("e")
      traversalPath.append("e")
      newRoom=player.currentRoom['room_id']
      curExits['e']=newRoom
      newExits={}
      if newRoom not in copy:
        for exit in player.currentRoom['exits']:
          newExits[exit]="unknown"
          copy[newRoom]=newExits
        newExits['w']=curRoom
      reverse.append('w')
      
  elif 'w' in copy[curRoom] and curExits['w'] == 'unknown':
    print(copy[curRoom], "Currently")
    if curExits['w']=='unknown':
    #   time.sleep(curCooldown)
      player.travel("w")
      traversalPath.append("w")
      newRoom=player.currentRoom['room_id']
      curExits['w']=newRoom
      newExits={}
      if newRoom not in copy:
        for exit in player.currentRoom['exits']:
          newExits[exit]="unknown"
          copy[newRoom]=newExits
        newExits['e']=curRoom
      reverse.append('e')
  else:
    reversal=reverse.pop()
    # time.sleep(curCooldown)
    player.travel(reversal)
    traversalPath.append(reversal)
#--------------------------- TRAVERSAL ---------------------------------#