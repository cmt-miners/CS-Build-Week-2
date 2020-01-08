from player import Player
import time 

player=Player('Bryce', 0)
player.init()


traversalPath = []
#-----------
copy={} 
rooms=[]
reverse=[]
#-----------
while len(copy) < 500:
  # print("----------------------COPY------------------------------------", copy)
  # print("----------------------ROOMS------------------------------------", rooms)
  """formating the data
  {'room_id': 328, 'title': 'A misty room', 'description': 'You are standing on grass and surrounded by a dense mist. You can barely make out the exits in any direction.', 'coordinates': '(57,70)', 'elevation': 0, 'terrain': 'NORMAL', 'players': [], 'items': [], 'exits': ['n', 's', 'e', 'w'], 'cooldown': 15.0, 'errors': [], 'messages': ['You have walked west.']}


  """
  if player.currentRoom is not None:
    print(f"//=========current while loop info=================//")
    print("room_id:", player.currentRoom['room_id'])
    print('TITLE:', player.currentRoom['title'])
    print(f"messages:",player.currentRoom['messages'])
    print(f'cooldown',player.currentRoom['cooldown'])
    print(f"//===============================================//")







  curCooldown=player.currentRoom['cooldown']
  time.sleep(curCooldown)
  if len(player.currentRoom['items']) > 0:
    player.pilfer()
    time.sleep(8)
  time.sleep(2)
  player.status()
  time.sleep(2)
  roomObj=player.currentRoom
  curRoom=player.currentRoom['room_id']
  if curRoom not in copy:
    copy[curRoom]=curRoom 
    curExits={}
  
    for exit in player.currentRoom['exits']:
      curExits[exit]="unknown"

    copy[curRoom]=curExits
  
  curExits=copy[curRoom]
  if roomObj not in rooms:
      rooms.append(roomObj)

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




"""


const PORT = 5050;

const getUrl = 'https://lambda-treasure-hunt.herokuapp.com/api/adv/init/';
const moveUrl = 'https://lambda-treasure-hunt.herokuapp.com/api/adv/move/';


const takeUrl = 'https://lambda-treasure-hunt.herokuapp.com/api/adv/take/';
const dropUrl = 'https://lambda-treasure-hunt.herokuapp.com/api/adv/drop/';
const sellUrl = 'https://lambda-treasure-hunt.herokuapp.com/api/adv/sell/';
const statusUrl = 'https://lambda-treasure-hunt.herokuapp.com/api/adv/status/';
const examineUrl =
  'https://lambda-treasure-hunt.herokuapp.com/api/adv/examine/';
// const wearUrl = 'https://lambda-treasure-hunt.herokuapp.com/api/adv/wear/';
// const changeNameUrl = 'https://lambda-treasure-hunt.herokuapp.com/api/adv/change_name/';
// const prayUrl = 'https://lambda-treasure-hunt.herokuapp.com/api/adv/pray/';
// const flyUrl = 'https://lambda-treasure-hunt.herokuapp.com/api/adv/fly/';
// const dashUrl = 'https://lambda-treasure-hunt.herokuapp.com/api/adv/dash/';
// const carryUrl = 'https://lambda-treasure-hunt.herokuapp.com/api/adv/carry/';
// const receiveUrl = 'https://lambda-treasure-hunt.herokuapp.com/api/adv/receive/';
// const mineUrl = 'https://lambda-treasure-hunt.herokuapp.com/api/bc/mine/';
// const proofUrl = 'https://lambda-treasure-hunt.herokuapp.com/api/bc/last_proof/';
// const balanceUrl = 'https://lambda-treasure-hunt.herokuapp.com/api/bc/get_balance/';
// const transmorgrifyUrl = 'https://lambda-treasure-hunt.herokuapp.com/api/adv/transmogrify/';




"""