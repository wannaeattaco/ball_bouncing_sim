import turtle
import random


class Ball:
    def __init__(self, canvas_width, canvas_height, ball_radius):
        self.xpos = random.randint(ball_radius, canvas_width - ball_radius)
        self.ypos = random.randint(ball_radius, canvas_height - ball_radius)
        self.vx = random.randint(1, 0.01 * canvas_width)
        self.vy = random.randint(1, 0.01 * canvas_height)
        self.radius = ball_radius
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    def move_circle(self, canvas_width, canvas_height):
        # update the x, y coordinates of the ball with velocity
        self.xpos += self.vx
        self.ypos += self.vy

        # if the ball hits the side walls, reverse the vx velocity
        if abs(self.xpos + self.vx) > (canvas_width - self.radius):
            self.vx = -self.vx

        # if the ball hits the ceiling or the floor, reverse the vy velocity
        if abs(self.ypos + self.vy) > (canvas_height - self.radius):
            self.vy = -self.vy

    def draw_circle(self):
        turtle.penup()
        turtle.goto(self.xpos, self.ypos - self.radius)
        turtle.pendown()
        turtle.color(self.color)
        turtle.begin_fill()
        turtle.circle(self.radius)
        turtle.end_fill()


class ballsim:
    def __init__(self, canvas_width, canvas_height, ball_radius, num_balls):
        self.canvas_width = canvas_width
        self.canvas_height = canvas_height
        self.balls = [Ball(canvas_width, canvas_height, ball_radius) for _ in range(num_balls)]

    def update_balls(self):
        for ball in self.balls:
            ball.move_circle(self.canvas_width, self.canvas_height)

    def draw_balls(self):
        for ball in self.balls:
            ball.draw_circle()


num_balls = int(input("Number of balls to simulate: "))
turtle.speed(0)
turtle.tracer(0)
turtle.hideturtle()
canvas_width, canvas_height = turtle.screensize()
ball_radius = 0.05 * canvas_width
turtle.colormode(255)

sim = ballsim(canvas_width, canvas_height, ball_radius, num_balls)

while True:
    turtle.clear()
    sim.update_balls()
    sim.draw_balls()
    turtle.update()

    # turtle.done()
