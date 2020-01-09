import requests
import json 
import time

jamie_api_key= 'Token 6b056b046e07f644c8a86d42fb659a70821439c2'
jacob_api_key= 'Token 5aa999d43330eefb245d81fe9f486056d4c4030f'

headers = {
    'Authorization': jacob_api_key,
    'Content-Type': 'application/json'
}

class Player:
    def __init__(self, name, startingRoom):
        self.name = name
        self.currentRoom = startingRoom
        currentStatus = {}

    def travel(self, direction):
        print("Direction", direction)
        if direction == "n":
            data={"direction": "n"}
        if direction == "s":
            data={"direction": "s"}
        if direction == "e":
            data={"direction": "e"}
        if direction == "w":
            data={"direction": "w"}
        
        res=requests.post(
            'https://lambda-treasure-hunt.herokuapp.com/api/adv/move/', headers=headers, data=json.dumps(data)
        )

        nextRoom=json.loads(res.text)
        self.currentRoom=nextRoom
        print(nextRoom, "Here is our new room")

    def init(self):
        res=requests.get(
            'https://lambda-treasure-hunt.herokuapp.com/api/adv/init/', headers=headers 
        )
        nextRoom=json.loads(res.text)
        self.currentRoom=nextRoom

    def pilfer(self):
        if len(self.currentRoom['items']) > 0:
            data={"name": "treasure"}
            res=requests.post(
            'https://lambda-treasure-hunt.herokuapp.com/api/adv/take/', headers=headers, data=json.dumps(data)
            )
            print("PILFER------- \n", res.text, "TAKING TREASURE")

    def drop(self):
        data={"name": "treasure"}
        res=requests.post(
        'https://lambda-treasure-hunt.herokuapp.com/api/adv/drop/', headers=headers, data=json.dumps(data)
        )
        print("DROP------- \n    ", res.text, "DROPPING TREASURE")

    def status(self):
        res=requests.post(
            'https://lambda-treasure-hunt.herokuapp.com/api/adv/status/', headers=headers
            )
        print("Checking Status\n", json.loads(res.text))
        self.currentStatus = json.loads(res.text)
        # print(type(currentStatus))
        # print(type(currentStatus['inventory']))
        # print(currentStatus['inventory'])

    def sell(self):
        data1 = {"name": "treasure"}
        res = requests.post(
        'https://lambda-treasure-hunt.herokuapp.com/api/adv/sell/', headers=headers, data=json.dumps(data1)
        )
        print("--------", res.text, "SELLING MY TREASURE")
        time.sleep(5)
        data2 = {"name": "treasure", "confirm": "yes"}
        res = requests.post(
        'https://lambda-treasure-hunt.herokuapp.com/api/adv/sell/', headers=headers, data=json.dumps(data2)
        )

    def name_change(self):
        data1 = {"name":"[Jtonna]"}
        res = requests.post(
        'https://lambda-treasure-hunt.herokuapp.com/api/adv/change_name/', headers=headers, data=json.dumps(data1)
        )
        print("--------", res.text, "NAME CHANGE")
        time.sleep(35)
        data2 = {"name":"[Jtonna]", "confirm": "aye"}
        res = requests.post(
        'https://lambda-treasure-hunt.herokuapp.com/api/adv/change_name/', headers=headers, data=json.dumps(data2)
        )
        print("--------", res.text, "NAME CHANGE")
    
    def wishing_well(self):
        data = {"name":"Wishing Well"}
        res = requests.post(
            'https://lambda-treasure-hunt.herokuapp.com/api/adv/examine/', headers=headers, data=json.dumps(data)
        )
        print("--------", res.text, "WISHING WELL INFO")