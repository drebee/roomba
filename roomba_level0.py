# -----------------------------------------------------------------------------
# Roomba in Python - Difficulty Level 0
# This file implements an algorithm for a roomba cleaning a rectangular room.
#
# Author: Dr. EB <------ REPLACE THIS WITH YOUR NAME!
# -----------------------------------------------------------------------------
 
import tkinter
import turtle
 
# Make the turtle be a cute turtle
turtle.shape("turtle")

# Add a background image with the room design
turtle.bgpic("img/room_level0.png")
 
# Open the window
window = turtle.Screen()
room_width = 100
room_height = 100
window.setup(width=room_width*1.5, height=room_height*1.5)
 
# Find roomba's starting position
# We are imagining that the roomba has a 20-pixel radius. So when the roomba is
# at the top-left corner of the screen, it's *center* is a little bit lower and
# to the right.
roomba_radius = 20
start_x = int(-room_width/2 + roomba_radius)
start_y = int(room_height/2 - roomba_radius)
 
# Move roomba to starting position
turtle.up()
turtle.goto(start_x, start_y)
turtle.down()
turtle.dot()
 
###
# Start your code here
 
 
 
# End your code here
###
 
window.exitonclick()