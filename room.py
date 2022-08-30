from PIL import Image, ImageDraw
from turtle import Screen, bgpic, shape, up, goto, down, left, right

pixel_width = 40
pixel_height = 40
circle_room_radius = 5

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

def in_circle(x, y, radius, center):
    # equation of a circle:
    # (x – x1)² + (y – y1)²= r²
    x1 = center[0]
    x2 = center[1]
    return (x - x1)**2 + (y - x2)**2 <= radius**2

def draw_circle(radius, img1, center):
    alcove_radius = radius // 2

    n_rows = (radius*2 + 1)*4
    n_cols = (radius*2 + 1)*4
    
    for col in range(n_cols):
        start_x = pixel_width * col
        end_x = pixel_width * (col + 1)
        for row in range(n_rows):
            if in_circle(col, row, radius, center):
                start_y = pixel_height * row
                end_y = pixel_height * (row + 1)
                shape = [(start_x, start_y), (end_x, end_y)]
                img1.rectangle(shape, fill ="white", outline = "gray")

def draw_circles(radius, room_image_file, n_alcoves):

    alcove_radius = radius // 2
    n_rows = radius*2 + 1 + alcove_radius*2*2
    n_cols = radius*2 + 1 + alcove_radius*2*2
        
    room_width = n_cols*pixel_width
    room_height = n_rows*pixel_height

    img = Image.new("RGB", (room_width+1, room_height+1), color="white")
    img1 = ImageDraw.Draw(img)  
    
    # draw center circle
    draw_circle(
        radius,
        img1,
        center = (radius + alcove_radius*2,
                  radius + alcove_radius*2))
    
    if n_alcoves >= 1:
        draw_circle(
            alcove_radius,
            img1,
            center = (radius*2 + alcove_radius*2 + alcove_radius,
                      radius + alcove_radius*2))
    if n_alcoves >= 2:
        draw_circle(
            alcove_radius,
            img1,
            center = (alcove_radius,
                      radius + alcove_radius*2))
    if n_alcoves >= 3:
        draw_circle(
            alcove_radius,
            img1,
            center = (radius + alcove_radius*2,
                      alcove_radius))
    if n_alcoves >= 4:
        draw_circle(
            alcove_radius,
            img1,
            center = (radius + alcove_radius*2,
                      radius*2 + alcove_radius*2 + alcove_radius))

    img.save(room_image_file)

    return room_width, room_height

def draw_room(level = 0, n_alcoves = 0):
    room_image_file = f"img/room{level}.png"

    if level == 0 or level == 1:
        room_width, room_height = draw_rectangle(5, 5, room_image_file)
    elif level == 2:
        room_width, room_height = draw_rectangle(20, 15, room_image_file)
    elif level == 3:
        room_width, room_height = draw_circles(circle_room_radius,
                                               room_image_file)
    else:
        room_width, room_height = draw_circles(circle_room_radius,
                                               room_image_file,
                                               n_alcoves = n_alcoves)


    window_scale_factor = 1.8
    window_width = int(room_width*window_scale_factor)
    window_height = int(room_height*window_scale_factor)

    # Open the window so it's big enough to see the whole room
    window = Screen()
    window.setup(width=window_width, height=window_height)

    # Add a background image with the room design
    bgpic(room_image_file)

    # Make the turtle be a cute turtle
    shape("turtle")

    # Find roomba's starting position
    # We are imagining that the roomba has a 20-pixel radius. So when the roomba is
    # at the top-left corner of the screen, it's *center* is a little bit lower and
    # to the right.
    roomba_radius = 20

    if level < 3:
        start_x = -room_width//2 + roomba_radius
        start_y = room_height//2 - roomba_radius
    elif n_alcoves >= 3:
        start_x = 0
        start_y = room_height // 2 - roomba_radius
    else:
        start_x = 0
        start_y = (circle_room_radius*2+1)*pixel_height // 2 - roomba_radius


    # Move roomba to starting position
    left(90)
    up()
    goto(start_x, start_y)
    right(180)
    down()
    # dot()
    return window