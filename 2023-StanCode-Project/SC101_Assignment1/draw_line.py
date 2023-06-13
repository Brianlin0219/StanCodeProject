"""
File: 
Name:
-------------------------
TODO:
"""

from campy.graphics.gobjects import GOval, GLine
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked

SIZE = 20
window = GWindow()
count = 1

hole = GOval(SIZE, SIZE)


# count % 2 == 1 奇數

def main():
    """
    This program creates lines on an instance of GWindow class.
    There is a circle indicating the user’s first click. A line appears
    at the condition where the circle disappears as the user clicks
    on the canvas for the second time.
    """
    onmouseclicked(draw_line)


def draw_line(mouse):
    global count
    hole.filled = False
    if count % 2 == 1:
        window.add(hole, x=mouse.x - SIZE / 2, y=mouse.y - SIZE / 2)
        count += 1
    elif count % 2 == 0:
        line = GLine(hole.x + SIZE / 2, hole.y + SIZE / 2, mouse.x, mouse.y)
        window.add(line)
        window.remove(hole)
        count += 1


if __name__ == "__main__":
    main()
