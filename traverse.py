from player import Player
import time 

player=Player('jamie', 0)




# player.init()
# time.sleep(16)
# player.travel("n")
# while True: 
#     cmds=input("->").lower().split(" ")
#     print("Did we get to line 10?")
#     # if cmds[0] in ["n", "s", "e", "w"]:
#     move=input('INPUT A DIRECTION')
#     if move == 'n':
#         player.travel("n")


# Keep track of position somehow??
#  from room import Room
"""

const express = require('express');
const server = express();
const bodyParser = require('body-parser');

const db = require('./dbConfig');
const cors = require('cors');
const axios = require('axios');
const { Client } = require('pg');

server.use(cors());
server.use(express.json());
server.use(bodyParser())

server.get('/players', (req, res) => {
  db.select()
    .from('players')
    .then(players => {
      res.send(players);
    });
});

server.get('/players/:playerID', (req, res) => {
  db.select()
    .from('players')
    .where('playerID', req.params.playerID)
    .then(players => {
      res.send(players);
    });
});

server.get('/map', (req, res) => {
  db.select()
    .from('map')
    .then(map => {
      res.send(map);
    });
});

server.get('/map:room_id', (req, res) => {
  db.select()
    .from('map')
    .where('room_id', req.params.room_id)
    .then(map => {
      res.send(map);
    });
});

server.post('/players', (req, res) => {
  db('players')
    .insert(req.body)
    .then(() => {
      db.select()
        .from('players')
        .then(players => {
          res.send(players);
        });
    });
});

server.post('/map', (req, res) => {
  db('map')
    .insert(req.body)
    .then(() => {
      db.select()
        .from('map')
        .then(map => {
          res.send(map);
        });
    });
});

server.put('/players/update/:playerID', (req, res) => {
  db.select()
    .from('players')
    .where('playerID', req.params.playerID)
    .update(req.body)
    .then(players => {
      db.select()
        .from('players')
        .where('playerID', req.params.playerID)
        .then(players => {
          res.send(players);
        });
    });
});

server.put('/map/update/:room_id', (req, res) => {
  db.select()
    .from('map')
    .where('room_id', req.params.room_id)
    .update(req.body)
    .then(map => {
      db.select()
        .from('map')
        .where('room_id', req.params.room_id)
        .then(map => {
          res.send(map);
        });
    });
});

let treasureMap = {};
let completeMap = [];
// -------- Pseudo DB until static db is created ----------

class Room {
  constructor(room_id, title, coordinates, items, exits, cooldown) {
    this.room_id = room_id;
    this.title = title;
    this.coordinates = [
      Number(coordinates.replace(/[(](\d+)\s?[,]\s?(\d+)[)]/, '$1')),
      Number(coordinates.replace(/[(](\d+)\s?[,]\s?(\d+)[)]/, '$2'))
    ];
    this.items = items;
    this.exits = exits;
    this.cooldown = cooldown;
  }
}

class MapNode {
  constructor(room_id, coordinates, exits) {
    (this.room_id = room_id),
      (this.coordinates = coordinates),
      (this.exits = exits);
  }
}




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


traversalPath = []
#-----------
copy={} 
rooms={}
reverse=[]
#-----------
while len(copy) < 500:
  roomObj=player.currentRoom
  curRoom=player.currentRoom.id
  if curRoom not in copy:
    copy[curRoom]=curRoom 
    curExits={}
  
    for exit in player.currentRoom.exits:
      curExits[exit]="unknown"

    copy[curRoom]=curExits
  
  curExits=copy[curRoom]
  if roomObj not in rooms:
      rooms[roomObj.id]=roomObj

  if 'n' in copy[curRoom] and curExits['n'] == 'unknown':
    print(copy[curRoom], "Currently")
    if curExits['n']=='unknown':
      time.sleep(16)
      player.travel("n")
      traversalPath.append("n")
      newRoom=player.currentRoom.id
      curExits['n']=newRoom
      newExits={}
      if newRoom not in copy:
        for exit in player.currentRoom.exits:
          newExits[exit]="unknown"
          copy[newRoom]=newExits
        newExits['s']=curRoom
      reverse.append('s')

  elif 's' in copy[curRoom] and curExits['s'] == 'unknown':
    print(copy[curRoom], "Currently")
    if curExits['s']=='unknown':
      time.sleep(16)
      player.travel("s")
      traversalPath.append("s")
      newRoom=player.currentRoom.id
      curExits['s']=newRoom
      newExits={}
      if newRoom not in copy:
        for exit in player.currentRoom.exits:
          newExits[exit]="unknown"
          copy[newRoom]=newExits
        newExits['n']=curRoom
      reverse.append('n')

  elif 'e' in copy[curRoom] and curExits['e'] == 'unknown':
    print(copy[curRoom], "Currently")
    if curExits['e']=='unknown':
      time.sleep(16)
      player.travel("e")
      traversalPath.append("e")
      newRoom=player.currentRoom.id
      curExits['e']=newRoom
      newExits={}
      if newRoom not in copy:
        for exit in player.currentRoom.exits:
          newExits[exit]="unknown"
          copy[newRoom]=newExits
        newExits['w']=curRoom
      reverse.append('w')

  elif 'w' in copy[curRoom] and curExits['w'] == 'unknown':
    print(copy[curRoom], "Currently")
    if curExits['w']=='unknown':
      time.sleep(16)
      player.travel("w")
      traversalPath.append("w")
      newRoom=player.currentRoom.id
      curExits['w']=newRoom
      newExits={}
      if newRoom not in copy:
        for exit in player.currentRoom.exits:
          newExits[exit]="unknown"
          copy[newRoom]=newExits
        newExits['e']=curRoom
      reverse.append('e')

  else: 
    reversal=reverse.pop()
    time.sleep(16)
    player.travel(reversal)
    traversalPath.append(reversal)

