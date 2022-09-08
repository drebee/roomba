# -----------------------------------------------------------------------------
# Roomba in Python
# This file implements an algorithm for a roomba cleaning a room.
#
# Author: Dr. EB <------ REPLACE THIS WITH YOUR NAME!
# -----------------------------------------------------------------------------
 
from turtle import right, left, forward, backward
import room

# THIS PARAMETER CAN CHANGE!!!
# Make sure your code works for n_alcoves = 0, 1, 2, 3, and 4
# (You are allowed to use this parameter in your code)
n_alcoves = 3

# Draw the Level 7 version of the room
window = room.draw_room(level = 7, n_alcoves = n_alcoves)

###
# Start your code here
 
 
 
# End your code here
###
 
window.exitonclick()