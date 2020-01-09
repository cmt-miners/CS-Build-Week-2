import hashlib
import requests
import json
import time 
import json

jamie_api_key= 'Token 6b056b046e07f644c8a86d42fb659a70821439c2'

headers = {
    'Authorization': jamie_api_key,
    'Content-Type': 'application/json'
}

def get_last_proof():
    response = requests.get('https://lambda-treasure-hunt.herokuapp.com/api/bc/last_proof/', headers=headers)
    
    res=json.loads(response.text)
    print("LAST PROOF", res)
    return res

def mine(proof):
    # data = '{"proof": my_proof}'.replace("my_proof", str(proof))
    proof = {"proof": int(proof)}
    response = requests.post('https://lambda-treasure-hunt.herokuapp.com/api/bc/mine/', headers=headers, data=proof)

    print("Did I mine a coin?", response)
    res=json.loads(response.text)  
    print(res)
    time.sleep(res['cooldown'])
    return res

def proof_of_work(last_proof):
    """
# Get the last valid proof to use to mine a new block. Also returns the current difficulty level, which is the number of 0's required at the beginning of the hash for a new proof to be valid.

# The proof of work algorithm for this blockchain is not the same as we used in class. It uses a different method:

# Does hash(last_proof, proof) contain N leading zeroes, where N is the current difficulty level?
    """
    print(last_proof, "<---------LAST PROOF HERE")
    the_last_proof=last_proof['proof']
    difficulty=last_proof['difficulty']
    print("Searching for next proof")
    last_hash = json.dumps(the_last_proof)
    proof = 0
    while valid_proof(last_hash, proof, difficulty) is False:
        proof += 1

    print("MY PROOF", proof)
    return proof

def valid_proof(last_hash, proof, difficulty):
    guess = f'{last_hash}{proof}'.encode()
    guess_hash = hashlib.sha256(guess).hexdigest()
    return guess_hash[:difficulty] == "0" * difficulty


if __name__ == "__main__":
    while True:
        last_proof = get_last_proof()
        time.sleep(last_proof['cooldown'])
        new_proof = proof_of_work(last_proof)
        mine_res=mine(new_proof)
