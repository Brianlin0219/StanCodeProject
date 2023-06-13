"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao.

YOUR DESCRIPTION HERE
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved, onmousedragged
import random

BRICK_SPACING = 5  # Space between bricks (in pixels). This space is used for horizontal and vertical spacing
BRICK_WIDTH = 40  # Width of a brick (in pixels)
BRICK_HEIGHT = 15  # Height of a brick (in pixels)
BRICK_ROWS = 10  # Number of rows of bricks
BRICK_COLS = 10  # Number of columns of bricks
BRICK_OFFSET = 50  # Vertical offset of the topmost brick from the window top (in pixels)
BALL_RADIUS = 10  # Radius of the ball (in pixels)
PADDLE_WIDTH = 75  # Width of the paddle (in pixels)
PADDLE_HEIGHT = 15  # Height of the paddle (in pixels)
PADDLE_OFFSET = 50  # Vertical offset of the paddle from the window bottom (in pixels)
INITIAL_Y_SPEED = 7  # Initial vertical speed for the ball
MAX_X_SPEED = 5  # Maximum initial horizontal speed for the ball
BRICK_COLORS = ['red', 'orange', 'yellow', 'green', 'blue']  # List of brick colors
SCORE = 0

# global variable
game_stated = False


class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH, paddle_height=PADDLE_HEIGHT,
                 paddle_offset=PADDLE_OFFSET, brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS, brick_width=BRICK_WIDTH,
                 brick_height=BRICK_HEIGHT, brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING, title='Breakout'):
        # Create a graphical window, with some extra space
        self.window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        self.window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=self.window_width, height=self.window_height, title=title)

        # Create a paddle
        self.paddle = GRect(paddle_width, paddle_height, x=(self.window.width - paddle_width) / 2,
                            y=self.window.height - paddle_offset - paddle_height)
        self.paddle.filled = True
        self.paddle.fill_color = 'black'
        self.paddle.color = 'black'
        self.window.add(self.paddle)
        # Center a filled ball in the graphical window
        self.ball = GOval(ball_radius * 2, ball_radius * 2, x=(self.window.width - ball_radius * 2) / 2,
                          y=(self.window.height - ball_radius * 2) / 2)
        self.ball.filled = True
        self.ball.fill_color = 'black'
        self.ball.color = 'black'
        self.window.add(self.ball)
        self.b_r = BALL_RADIUS
        # Default initial velocity for the ball
        self.vx = 0
        self.vy = 0
        # Initialize our mouse listeners
        onmouseclicked(self.ball_move)
        onmousemoved(self.handle_paddle)

        # Create score_label
        self.score_label = GLabel('SCORE:' + str(SCORE))  # 創造計分板
        self.score_label.font = '-20'
        self.window.add(self.score_label, x=10, y=self.window.height - self.score_label.height + 10)

        # Draw bricks
        for i in range(brick_cols):
            for j in range(brick_rows):
                brick = GRect(brick_width, brick_height)
                brick.filled = True
                brick.fill_color = BRICK_COLORS[j // 2]
                brick.color = BRICK_COLORS[j // 2]
                self.window.add(brick, x=i * (brick_width + brick_spacing), y=j * (brick_height + brick_spacing))
        self.bricks_num = brick_cols * brick_rows

    def handle_paddle(self, event):
        if event.x <= self.paddle.width / 2:
            self.paddle.x = 0
        elif event.x >= self.window.width - self.paddle.width / 2:
            self.paddle.x = self.window.width - self.paddle.width
        else:
            self.paddle.x = event.x - self.paddle.width / 2

    def ball_move(self, event):
        global game_stated
        if not game_stated:
            game_stated = True
            self.set_ball_velocity()

    def set_ball_velocity(self):
        self.vy = INITIAL_Y_SPEED
        self.vx = random.randint(1, MAX_X_SPEED)
        if random.random() > 0.5:
            self.vx = -self.vx

    def reset_position(self):
        global game_stated
        self.ball.x = self.window_width / 2 - self.b_r
        self.ball.y = self.window_height / 2 - self.b_r
        self.vx = 0
        self.vy = 0
        game_stated = False

    def get_vx(self):
        return self.vx

    def get_vy(self):
        return self.vy

    def reflect_ball_x(self):
        self.vx = -self.vx

    def reflect_ball_y(self):
        self.vy = -self.vy
