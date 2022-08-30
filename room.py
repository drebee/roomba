from PIL import Image, ImageDraw
import turtle

pixel_width = 40
pixel_height = 40

def draw_rectangle(n_cols, n_rows, room_image_file):

    room_width = n_cols*pixel_width
    room_height = n_rows*pixel_height

    img = Image.new("RGB", (room_width+1, room_height+1), color="white")
    img1 = ImageDraw.Draw(img)  

    for col in range(n_cols):
        start_x = pixel_width * col
        end_x = pixel_width * (col + 1)
        for row in range(n_rows):
            start_y = pixel_height * row
            end_y = pixel_height * (row + 1)
            shape = [(start_x, start_y), (end_x, end_y)]
            # shape = [(border_width, border_height),
            #         (room_width + border_width, room_height + border_height)]
            img1.rectangle(shape, fill ="white", outline = "gray")

    img.save(room_image_file)

    return room_width, room_height

def draw_room(level = 0):
    room_image_file = f"img/room{level}.png"

    room_width, room_height = draw_rectangle(5, 5, room_image_file)
    window_scale_factor = 2
    window_width = int(room_width*window_scale_factor)
    window_height = int(room_height*window_scale_factor)

    # Open the window so it's big enough to see the whole room
    window = turtle.Screen()
    window.setup(width=window_width, height=window_height)

    # Add a background image with the room design
    turtle.bgpic(room_image_file)

    # Make the turtle be a cute turtle
    turtle.shape("turtle")

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
    return window