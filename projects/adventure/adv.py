# built in imports
import os
import random
import time

# components
from room import Room
from player import Player
from world import World
from util import Queue, Stack

from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

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
traversal_path = []
# tuples or dictionary to store possible directions
# correction: n -> s and s -> n ; w -> e and e -> w
direction = {"n": "s", "s": "n", "w": "e", "e": "w"}

# need a path storage
path = []
# need a "visited" rooms storage
# "visited_rooms" used in traversal test
visited_cache = {}

# Create a function to find t he rooms' exits
# 1. init empty list (local cache)
# 2. loop through rooms to find exits
# 3. store exits and ignore collisions
# note: get_exits() is already a func in room
def find_all_exits(current_room):
    exits = []
    for exit in current_room.get_exits():
        # create visited for traversal func (different from visted_rooms)
        if room_graph[current_room.id][1][exit] not in visited:
            exits.append(exit)
    return find_all_exits


# debug
# print(find_all_exits())


# TRAVERSAL TEST
# visited_rooms = set()
# player.current_room = world.starting_room
# visited_rooms.add(player.current_room)

# for move in traversal_path:
#     player.travel(move)
#     visited_rooms.add(player.current_room)

# if len(visited_rooms) == len(room_graph):
#     print(
#         f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited"
#     )
# else:
#     print("TESTS FAILED: INCOMPLETE TRAVERSAL")
#     print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")


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
