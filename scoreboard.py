from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 25, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.speed("fastest")
        self.goto(0, 265)
        self.score = 0
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score = {self.score} ", align=ALIGNMENT, font=FONT)


    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)


    def increase_score(self):
        self.clear()
        self.score += 1
        self.update_scoreboard()



