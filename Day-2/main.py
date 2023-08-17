""""Day#2"""

import turtle

def ask_drawing_choice():
    response_str = input("""
    """)

def ask_stair_size():
    stair_size_int = 0
    while stair_size_int == 0:
        stair_size_str = input("Please enter the stair size: ")
        try:
            stair_size_int = int(stair_size_str)
        except ValueError:
            print("ERROR: You need to enter a number for the size ")
    return stair_size_int

def ask_stair_number():
    stair_number_int = 0
    while stair_number_int == 0:
        stair_number_str = input("Please enter the number of stairs: ")
        try:
            stair_number_int = int(stair_number_str)
        except ValueError:
            print("ERROR: You need to enter a number ")
    return stair_number_int

def draw_stairs(size, number):
    for i in range(0, number_of_stairs):
        t.forward(stair_size)
        t.left(90)
        t.forward(stair_size)
        t.right(90)
    t.forward(stair_size)

def draw_square(size):
    for i in range(0, 4):
        t.forward(size)
        t.left(90)

stair_size = ask_stair_size()
number_of_stairs = ask_stair_number()
t = turtle.Turtle()
draw_stairs(stair_size, number_of_stairs)
turtle.done()
