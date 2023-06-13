"""
File: 
Name:
----------------------
TODO:
"""

from campy.graphics.gobjects import GOval, GRect, GLabel, GArc, GPolygon, GLine
from campy.graphics.gwindow import GWindow


def main():
    """
    Title: 童年回憶

    小時候一直很好奇，麵包超人換掉的頭，吃起來是什麼味道？
    """
    window = GWindow(width=550, height=550, title='Anpanman')
    sky = GRect(550, 550)
    sky.filled = True
    sky.fill_color = 'skyblue'
    sky.color = 'skyblue'
    window.add(sky)

    cloud = GOval(150, 30, x=0, y=50)
    cloud.filled = True
    cloud.fill_color = 'white'
    cloud.color = 'white'
    window.add(cloud)
    cloud2 = GOval(200, 50, x=50, y=480)
    cloud2.filled = True
    cloud2.fill_color = 'white'
    cloud2.color = 'white'
    window.add(cloud2)
    cloud3 = GOval(100, 40, x=430, y=120)
    cloud3.filled = True
    cloud3.fill_color = 'white'
    cloud3.color = 'white'
    window.add(cloud3)
    cloud4 = GOval(150, 30, x=420, y=410)
    cloud4.filled = True
    cloud4.fill_color = 'white'
    cloud4.color = 'white'
    window.add(cloud4)

    tri = GPolygon()
    tri.add_vertex((350, 350))  # (300, 300)
    tri.add_vertex((410, 530))  # (500, 540)
    tri.add_vertex((430, 480))
    tri.add_vertex((500, 480))
    tri.add_vertex((480, 420))
    tri.add_vertex((540, 400))  # (540, 400)
    tri.filled = True
    tri.fill_color = 'chocolate'
    window.add(tri)

    body = GLine(400, 400, 490, 490)
    window.add(body)

    face = GOval(470, 450, x=15, y=25)
    face.filled = True
    face.fill_color = 'darksalmon'
    face.color = 'black'
    window.add(face)

    l_eye = GOval(50, 70, x=150, y=140)
    l_eye.filled = True
    l_eye.fill_color = 'black'
    window.add(l_eye)
    r_eye = GOval(50, 70, x=300, y=140)
    r_eye.filled = True
    r_eye.fill_color = 'black'
    window.add(r_eye)

    l_eyebrow = GArc(110, 250, 0, 180, x=110, y=100)
    l_eyebrow.filled = False
    l_eyebrow.color = 'black'
    window.add(l_eyebrow)
    r_eyebrow = GArc(110, 250, 0, 180, x=280, y=100)
    r_eyebrow.filled = False
    r_eyebrow.color = 'black'
    window.add(r_eyebrow)

    mouth = GArc(180, 320, 182, 176, x=160, y=275)
    mouth.filled = True
    mouth.fill_color = 'brown'
    mouth.color = 'black'
    window.add(mouth)

    l_n = GOval(135, 135, x=60, y=205)
    l_n.filled = True
    l_n.fill_color = 'red'
    l_n.color = 'red'
    window.add(l_n)
    c_n = GOval(110, 110, x=195, y=220)
    c_n.filled = True
    c_n.fill_color = 'red'
    c_n.color = 'black'
    window.add(c_n)
    r_n = GOval(135, 135, x=305, y=205)
    r_n.filled = True
    r_n.fill_color = 'red'
    r_n.color = 'red'
    window.add(r_n)

    l_n_a = GArc(270, 135, 270, 180, x=60, y=205)
    l_n_a.filled = False
    l_n_a.color = 'black'
    window.add(l_n_a)
    r_n_a = GArc(270, 135, 90, 180, x=305, y=205)
    r_n_a.filled = False
    r_n_a.color = 'black'
    window.add(r_n_a)

    l_n_w = GOval(23, 23, x=100, y=230)
    l_n_w.filled = True
    l_n_w.fill_color = 'white'
    l_n_w.color = 'white'
    window.add(l_n_w)
    c_n_w = GOval(15, 15, x=225, y=235)
    c_n_w.filled = True
    c_n_w.fill_color = 'white'
    c_n_w.color = 'white'
    window.add(c_n_w)
    r_n_w = GOval(23, 23, x=390, y=230)
    r_n_w.filled = True
    r_n_w.fill_color = 'white'
    r_n_w.color = 'white'
    window.add(r_n_w)

    word = GLabel("skr~")
    word.font = "-40"
    window.add(word, x=420, y=80)
    word = GLabel("skr~")
    word.font = "-40"
    window.add(word, x=280, y=520)

    l_arm = GLine(450, 450, 370, 460)
    window.add(l_arm)
    r_arm = GLine(450, 450, 470, 420)
    window.add(r_arm)
    r_arm2 = GLine(470, 420, 440, 410)
    window.add(r_arm2)
    l_leg = GLine(490, 490, 540, 500)
    window.add(l_leg)
    r_leg = GLine(490, 490, 460, 500)
    window.add(r_leg)
    r_leg2 = GLine(460, 500, 500, 520)
    window.add(r_leg2)

    wind = GLine(490, 280, 540, 280)
    window.add(wind)
    wind2 = GLine(470, 350, 540, 350)
    window.add(wind2)
    wind3 = GLine(485, 200, 540, 200)
    window.add(wind3)
    wind = GLine(495, 240, 525, 240)
    window.add(wind)
    wind = GLine(490, 315, 525, 315)
    window.add(wind)


if __name__ == '__main__':
    main()
