# built in imports
import os

# components
from room import Room
from player import Player
from world import World

from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
# map_file = "maps/main_maze.txt"

# easy to swap out map_file loader so you don't need to worry about file path
dirpath = os.path.dirname(os.path.abspath(__file__))
map_file = dirpath + "/maps/main_maze.txt"

# Loads the map into a dictionary
room_graph = literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']

# Path to visit 'rooms'
traversal_path = []  # ['n', 'n']

# Path to revisit 'rooms'
reversal_path = []

# reversed directions from direction previously traveled
reversed_directions = {"n": "s", "s": "n", "e": "w", "w": "e"}

# Dictionary to loop through rooms
rooms = {}

# {0: ["n", "s", "w", "e"]}

# Initialize empty rooms
rooms[0] = player.current_room.get_exits()


# debug
print(f"this is rooms {rooms}")

# this loop will run as long as the visited rooms are less than total rooms
# we want to visit all rooms
while len(rooms) < len(room_graph) - 1:
    # case: room not visited
    if player.current_room.id not in rooms:
        # 1. add exits from current room into rooms
        rooms[player.current_room.id] = player.current_room.get_exits()
        # 2. store previous direction
        previous_direction = reversal_path[-1]
        # 3. remove last exit from rooms
        rooms[player.current_room.id].remove(previous_direction)

    # what happens when all rooms are explored?!
    while len(rooms[player.current_room.id]) < 1:
        # remove
        go_back = reversal_path.pop()
        # add path to player's path
        traversal_path.append(go_back)
        # make 'player' move
        player.travel(go_back)

    # go to first exit in a room
    # pop instead of dequeue
    player_exit = rooms[player.current_room.id].pop(0)

    # add to trav path
    traversal_path.append(player_exit)

    # reverse direction in reverse path! this is why you made those
    reversal_path.append(reversed_directions[player_exit])

    player.travel(player_exit)


# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(
        f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited"
    )
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")


#######
# UNCOMMENT TO WALK AROUND
#######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
