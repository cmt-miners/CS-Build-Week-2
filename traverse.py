from player import Player

player=Player('jamie', 0)

while True:
    player.init()
    cmds=input("->").lower().split(" ")
    if cmds[0] in ["n", "s", "e", "w"]:
        player.init[cmds[0], True]