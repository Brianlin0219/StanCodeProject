"""
File: 
Name:
-------------------------
TODO:
"""

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked

VX = 3
DELAY = 15
GRAVITY = 1
SIZE = 20
REDUCE = 0.9
START_X = 30
START_Y = 40

window = GWindow(800, 500, title='bouncing_ball.py')
count = 0
ball = GOval(SIZE, SIZE)
position = True
ground = False


def main():
    """
    This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself.
    """
    ball.filled = True
    window.add(ball, x=START_X, y=START_Y)
    onmouseclicked(fall)


def fall(mouse):
    global count
    global position
    if position:  # if position is true
        vy = 0
        position = False
    while not position:  # while position is false
        print(vy)
        ball.move(VX, vy)
        vy += GRAVITY
        if ball.y + ball.height >= window.height:
            vy = -vy * REDUCE
        if ball.x + ball.width >= window.width:
            count += 1
            window.add(ball, x=START_X, y=START_Y)
            position = True
        elif count == 3:
            window.add(ball, x=START_X, y=START_Y)
            break
        pause(DELAY)


if __name__ == "__main__":
    main()
