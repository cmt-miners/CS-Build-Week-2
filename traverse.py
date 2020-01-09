from player import Player
import time 

player=Player('jamie', 0)
player.init()





#-------------------------------- Well from room_id 27------------------------------#


# time.sleep(player.currentRoom['cooldown'])
# player.travel("w")
# time.sleep(player.currentRoom['cooldown'])
# player.travel("s")
# time.sleep(player.currentRoom['cooldown'])
# player.travel("s")
# time.sleep(player.currentRoom['cooldown'])
# player.travel("s")
# time.sleep(player.currentRoom['cooldown'])
# player.travel("e")
# time.sleep(player.currentRoom['cooldown'])
# player.travel("n")
# time.sleep(player.currentRoom['cooldown'])
# player.travel("e")
# time.sleep(player.currentRoom['cooldown'])
# player.travel("e")
# time.sleep(player.currentRoom['cooldown'])
# player.examine()





#-------------------------------- NAME CHANGE ------------------------------#


# time.sleep(player.currentRoom['cooldown'])
# player.name_change()
# time.sleep(35)
# player.status()





#-------------------------------- STORE / From room_id 63 ------------------------------#

# time.sleep(player.currentRoom['cooldown'])
# player.travel("s")
# time.sleep(player.currentRoom['cooldown'])
# player.travel("s")
# time.sleep(player.currentRoom['cooldown'])
# player.travel("s")
# time.sleep(player.currentRoom['cooldown'])
# player.travel("s")
# time.sleep(player.currentRoom['cooldown'])
# player.travel("w")
# time.sleep(player.currentRoom['cooldown'])
# player.sell()
# time.sleep(5)
# player.status()



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



# ------------------------------ TRAVERSAL -------------------------#






traversalPath = []
#-----------
copy={}
rooms={}
reverse=[]
#-----------
while len(copy) < 500:
  print("----------------------COPY------------------------------------", copy)
  print("----------------------ROOMS------------------------------------", rooms)
  print("----------------------Current room in while loop----------------", player.currentRoom)
  print("-------------------------COPY LENGTH-------------------------------", len(copy))
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

  if player.currentRoom['room_id']==119:
      print("*****************MINE MINE MINE********************************")
      break


# Break for finding name changer 

#   if player.currentRoom['room_id']==467:
#       print("*****************NAME CHANGE********************************")
#       break

# Breaks for finding store, west of 0

#   if player.currentRoom['room_id']==0:
#       print("*****************SELL********************************")
#       break

#   if player.currentRoom['room_id']==10:
#       print("*****************SELL********************************")
#       break

#   if player.currentRoom['room_id']==19:
#       print("*****************SELL********************************")
#       break

#   if player.currentRoom['room_id']==20:
#       print("*****************SELL********************************")
#       break

#   if player.currentRoom['room_id']==63:
#       print("*****************SELL********************************")
#       break

#   if player.currentRoom['title']=='shop':
#       print("*****************SELL********************************")
#       break

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




