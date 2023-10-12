# This example is not working in Spyder directly (F5 or Run)
# Please type '!python turtle_runaway.py' on IPython console in your Spyder.
import tkinter as tk
import turtle, random

class RunawayGame:
    def __init__(self, canvas, runner, chaser, catch_radius=50):
        self.canvas = canvas
        self.runner = runner
        self.chaser = chaser
        self.catch_radius2 = catch_radius**2

        # Initialize 'runner' and 'chaser'
        self.runner.shape('turtle')
        self.runner.color('blue')
        self.runner.penup()

        self.chaser.shape('turtle')
        self.chaser.color('red')
        self.chaser.penup()

        # Instantiate an another turtle for drawing
        self.drawer = turtle.RawTurtle(canvas)
        self.drawer.hideturtle()
        self.drawer.penup()

        # add timer and score
        self.time = 10
        self.timer = turtle.RawTurtle(canvas)
        self.timer.shape('blank')
        self.timer.hideturtle()
        self.drawer.penup()

        self.count = 0
        self.score = turtle.RawTurtle(canvas)
        self.score.shape('blank')
        self.score.hideturtle()
        self.score.penup()

    def is_catched(self):
        p = self.runner.pos()
        q = self.chaser.pos()
        dx, dy = p[0] - q[0], p[1] - q[1]
        return dx**2 + dy**2 < self.catch_radius2

    def start(self, init_dist=400, ai_timer_msec=10):
        self.runner.setpos((-init_dist / 2, 0))
        self.runner.setheading(0)
        self.chaser.setpos((+init_dist / 2, 0))
        self.chaser.setheading(180)

        # TODO) You can do something here and follows.
        self.ai_timer_msec = ai_timer_msec
        self.set_score()
        self.set_timer()
        self.canvas.ontimer(self.draw_timer, 1000)
        self.canvas.ontimer(self.step, self.ai_timer_msec)


    def set_score(self):
        self.score.undo()
        self.score.penup()
        self.score.setpos(250,280)
        self.score.write(f'score : {self.count}')

    def draw_timer(self):
        if self.time > 0:
            self.set_timer()
            self.time = self.time - 1
            self.canvas.ontimer(self.draw_timer, 1000)
        else:
            self.set_timer()
            self.timer.clear()
            self.timer.write(f'game over')


    def set_timer(self):
        self.timer.clear()
        self.timer.penup()
        self.timer.setpos(250, 300)
        self.timer.write(f'time : {self.time}')

    def step(self):
        self.chaser.run_ai(self.chaser.pos(), self.chaser.heading())
        if self.runner.pos()[0] > 330 or self.runner.pos()[0] < -330 or self.runner.pos()[1] > 330 or self.runner.pos()[1] < -330:
            print(self.runner.pos())
            self.runner.setheading(self.runner.heading() + 180)
            self.runner.forward(50)
        else:
            self.runner.run_ai(self.runner.pos(), self.runner.heading())

        # TODO) You can do something here and follows.
        is_catched = self.is_catched()
        if is_catched:
            self.count += 1
            self.set_score()
            self.runner.setpos(random.randint(-300, 300), random.randint(-300,300))

        # Note) The following line should be the last of this function to keep the game playing
        if self.time > 0:
            self.canvas.ontimer(self.step, self.ai_timer_msec)
class ManualMover(turtle.RawTurtle):
    def __init__(self, canvas, step_move=10, step_turn=20):
        super().__init__(canvas)
        self.step_move = step_move
        self.step_turn = step_turn

        # Register event handlers
        canvas.onkeypress(lambda: self.forward(self.step_move), 'Up')
        canvas.onkeypress(lambda: self.backward(self.step_move), 'Down')
        canvas.onkeypress(lambda: self.left(self.step_turn), 'Left')
        canvas.onkeypress(lambda: self.right(self.step_turn), 'Right')
        canvas.onkeypress(lambda: self.forward(self.step_move * 10), 'space')
        canvas.listen()

    def run_ai(self, opp_pos, opp_heading):
        pass

class RandomMover(turtle.RawTurtle):
    def __init__(self, canvas, step_move=40, step_turn=20):
        super().__init__(canvas)
        self.step_move = step_move
        self.step_turn = step_turn

    def run_ai(self, opp_pos, opp_heading):
        mode = random.randint(0, 2)
        if mode == 0:
            self.forward(self.step_move)
        elif mode == 1:
            self.left(self.step_turn)
        elif mode == 2:
            self.right(self.step_turn)

if __name__ == '__main__':
    # Use 'TurtleScreen' instead of 'Screen' to prevent an exception from the singleton 'Screen'
    root = tk.Tk()
    canvas = tk.Canvas(root, width=700, height=700)
    canvas.pack()
    screen = turtle.TurtleScreen(canvas)

    # TODO) Change the follows to your turtle if necessary
    runner = RandomMover(screen)
    chaser = ManualMover(screen)

    game = RunawayGame(screen, runner, chaser)
    game.start()
    screen.mainloop()
