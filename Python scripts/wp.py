from random import choice
 
import random
 
cave_numbers = range(0, 20)
caves =[]
 
for i in cave_numbers:
    caves.append([])
 
unvisited_caves = range(0,20)
visited_caves = [0]
#unvisited caves == []
unvisited_caves.remove(0)
 
while unvisited_caves != []:
    i = choice(visited_caves)
    if len(caves[i]) >= 3:
        break
       
    next_cave = choice(unvisited_caves)
    caves[i].append(next_cave)
    caves[next_cave].append(i)
   
    visited_caves.append(next_cave)
    unvisited_caves.remove(next_cave)
   
    for number in cave_numbers:
        print number, ":", caves[number]
    print '----------'
   
    for i in cave_numbers:
        while len(caves[i]) < 3:
            passage_to = choice(cave_numbers)
            caves[i].append(passage_to)
           
        for i in cave_numbers:
            while len(caves[i]) < 3:
                passage_to = choice(cave_numbers)
                caves[i].append(passage_to)
               
            for number in cave_numbers:
                print number, ":", caves[number]
            print '----------'
   
for i in cave_numbers:
    for j in range(3):
        passage_to = choice(cave_numbers)
        caves[i].append(passage_to)
print caves
wumpus_location = choice(cave_numbers)
player_location = choice(cave_numbers)
#while player_location == wumpus_location
player_location = choice(cave_numbers)
 
print "Welcome to Hunt the Wumpus!"
print "You can see", len(cave_numbers), "caves"
print "To play, just type the number"
print "of the cave you wish to enter next"
 
while True:
 
    def print_location(player_location):
        """ Tell the player where they are """
        print "You are in cave ", player_location
        print "From here you can see caves:"
        print caves[player_location]
        if wumpus_location in caves[player_location]:
            print "I smell and horrible wumpus!"
     
    def setup_caves(cave_numbers):
        """ Create the starting list of caves """
        caves = []
        for cave in cave_numbers:
            caves.append([])
        return caves
 
    def link_caves():
        """ Make sure all of the caves are conneceted with two-way tunnels """
        while unvisited_caves != []:
            this_cave = choose_cave(visited_caves)
            next_cave = choose_cave(unvisited_caves)
            create_tunnel(this_cave, next_cave)
            visit_cave(next_cave)
 
    def finish_caves():
        """ Link the rest of the caves with one-way tunnels """
        for cave in cave_numbers:
            while len(caves[cave]) < 3:
                passage_to = choose_cave(cave_numbers)
                caves[cave].append(passage_to)
           
    def ask_for_cave():
        """Ask the player to choose a cave from their current_location."""
        player_input = raw_input("Which cave?")
        if (not player_input.isdigit() or
            int(player_input) not in caves[player_location]):
            print player_input + "?"
            print "That's not a direction that I can see!"
        else:
            return  int(player_input)
         
    def get_action():
        """ Find out what the player wants to do next. """
        print "What do you do next?"
        print "     m) move"
        print "     a) fire an arrow"
        action = raw_input(">")
        if action == "m" or action == "a":
            return action
        else:
            print action + "?"
            print "That's not an action that I know about"
            return None
         
    def do_movement():
        print "Moving...."
        new_location = ask_for_cave()
        if new_location is None:
            return player_location
        else:
            return new_location
       
    def do_shooting():
        print "Firing..."
        shoot_at = ask_for_cave()
        if shoot_at is None:
            return False
   
        if shoot_at == wumpus_location:
            print "Kapow!  Well done buddy, you shot the mighty wumpus!"
            print "You are the mighty wumpus hunter."
        else:
            print "Twang... clatter, clatter!"
            print "You wasted your ONLY arrow!"
            print "Empty handed, you begin the "
            print "long trek back to your village.  A failure."
            return True
   
         
   
    #...
   
    while 1:
        print_location(player_location)
       
        action = get_action()
        if action is None:
            continue
           
        if action == "m":
            player_location = do_movement()
            if player_location == wumpus_location:
                print "Argh, the wumpus ATE you!"
                print "Game over bro, game over!"
                break
               
        if action == "a":
            game_over = do_shooting()
            if game_over:
                break