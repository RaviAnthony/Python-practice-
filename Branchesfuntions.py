from sys import exit
def gold_room():
    print"this room is full of gold"
    next = raw_input(">")
    if "0" in next or "1" in next:
        how_much = int(next)
    else:
        dead( "learn to type number")
    if how_much < 50:
        print(" nice your not greedy")
        exit(0)
        
    else:
        dead( " you are greedy")
def bear_room():
    print " bear here"
    print " bear honey"
    print " bear fat"
    print "move bear"
    bear_moved = False
    
    while True:
        next = raw_input(">")
    
    if next == " take honey ":
        dead(" bear slaps your face")
    elif next == "taunt bear" and not bear_moved:
        print " bear moved go form the door"
        bear_moved = True
    elif next == "taunt bear" and bear_moved:
        dead(" the bear get pissed off and chews of the leg")
    elif next== "open door" and bear_moved:
        gold_room()
    else:
        print " i got no idea what the means"
        
def hulhul_room():
    print " great evil"
    print " insane"
    print " life or eat the head"
    
    next = raw_input(">")
    if "flee" in next:
        start()
    elif "head" in next:
        dead(" taste")
    else:
        hulhul_room()
def dead(why):
    print why, "good job"
    exit(0)
def start():
    print" your in dark room"
    print " room is left and right"
    print " which one do you take"
    
    next = raw_input(">")
    if next == "left":
        bear_room()
    elif next == "right":
        hulhul_room()
    else:
        dead( strave)
start()        


    
        