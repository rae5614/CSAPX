import turtle

############
# INITIATE #
############
def init(depth):
    turtle.pensize(4)
    turtle.speed(0)
    turtle.up()
    turtle.backward(200)
    turtle.forward(200)
    turtle.down()

##########
# COLORS #
##########
def set_color(depth):
    if depth == 1:
        turtle.color('green')
    elif depth == 2:
        turtle.color('blue')
    elif depth == 3:
        turtle.color('red')
    elif depth == 4:
        turtle.color('purple')
    else:
        turtle.color('black')


def draw_shapes_1(length):
    """
    Draw the shape at depth 1
    :param length: length of the segments

def draw_squares(length)
"""
Draws a square of a given length.
:param length: the length in pixels of one side of the square
:return: None
"""
# ran twice
for _ in range(4):
    turtle.forward(length)
    turtle.left(90)

