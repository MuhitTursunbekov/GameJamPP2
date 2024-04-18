import turtle
import math

wn = turtle.Screen()
wn.bgcolor("black")
wn.title("A Maze Game")
wn.setup(700, 700)

# Register shapes
turtle.register_shape("wizard_right.gif")
turtle.register_shape("wizard_left.gif")
turtle.register_shape("treasure.gif")
turtle.register_shape("wall.gif")

# Create pen
class Pen(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("white")
        self.penup()
        self.speed(0)

class Player(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("wizard_right.gif")
        self.color("blue")
        self.penup()
        self.speed(0)
        self.gold = 0

    def go_up(self):
        move_to_x = self.xcor()
        move_to_y = self.ycor() + 24
        
        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)

    def go_down(self):
        move_to_x = self.xcor()
        move_to_y = self.ycor() - 24
        
        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)

    def go_left(self):
        move_to_x = self.xcor() - 24
        move_to_y = self.ycor()
        self.shape("wizard_left.gif")
        
        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)

    def go_right(self):
        move_to_x = self.xcor() + 24
        move_to_y = self.ycor()

        self.shape("wizard_right.gif")
        
        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)
        
    def is_collision(self, other):
        a = self.xcor() - other.xcor()
        b = self.ycor() - other.ycor()
        distance = math.sqrt((a**2) + (b**2))
        
        if distance < 5:
            return True
        else:
            return False
    
class Treasure(turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape("treasure.gif")
        self.color("gold")
        self.penup()
        self.speed(0)
        self.gold = 100
        self.goto(x, y)

    def destroy(self):
        self.goto(2000, 2000)
        self.hideturtle()

# Create levels list
levels = [""]

# Define first level
level_1 = [
    "XXXXXXXXXXXXXXXXXXXXXXXXX",
    "XP  XX               XXXX",
    "X  XX  XXX  XXXXXX  XXXXX",
    "X  XX  XXXXXXXXXXX  XXXXX",
    "X      XXXXX  XXXX    XXX",
    "XXX  XXXXXXX  XXXX   XXXX",
    "XXX  XX  XXX  T       XXX",
    "XXX  XX  XXXXXXXXXXXXXXXX",
    "X        XXXX  XXXXXXXXXX",
    "XXXXXXX  XX        XXXXXX",
    "XXXXXXX      XXXX    XXXX",
    "XX    XXXXXXXXXXX  XXXXXX",
    "XX       XXXXXX      XXXX",
    "XX  XXX    XXXXXXXX  XXXX",
    "XX  XXXXXXXXX   XXX  XXXX",
    "XX                    XXX",
    "XXXXXXXXXXXXX   XXXX  XXX",
    "XX         XXX  XX    XXX",
    "XXXXXXXXXXXXXXXXX   XXXXX",
    "XX                 XXXXXX",
    "XX  XXXXXXXXXXXXXXXXXXXXX",
    "XX  X                  XX",
    "XX     XXXXXXXXXXX     XX",
    "XXXXXXXXXXXXXXXXXX     XX",
    "XXXXXXXXXXXXXXXXXXXXXXXXX"
]

# Add a treasure list
treasures = []

# Add maze to mazes list
levels.append(level_1)

# Create level setup function
def setup_maze(level):
    for y in range(len(level)):
        for x in range(len(level[y])):
            character = level[y][x]
            screen_x = -288 + (x * 24)
            screen_y = 288 - (y * 24)
            if character == "X":
                pen.goto(screen_x, screen_y)
                pen.shape("wall.gif")
                pen.stamp()
                walls.append((screen_x, screen_y))

            if character == "P":
                player.goto(screen_x, screen_y)
            
            if character == "T":
                treasures.append(Treasure(screen_x, screen_y))
            
# Create class instances
pen = Pen()
player = Player()

# Create wall coordinate list 
walls = []

# Set up the level
setup_maze(levels[1])


# Keyboard Binding
turtle.listen()
turtle.onkey(player.go_left, "Left")
turtle.onkey(player.go_right, "Right")
turtle.onkey(player.go_up, "Up")
turtle.onkey(player.go_down, "Down")

# Turn off screen updates
wn.tracer(0)

# Main game loop
while True:
    for treasure in treasures:
        if player.is_collision(treasure):
            player.gold += treasure.gold
            print("Player Gold: {}".format(player.gold))
            treasure.destroy()
            treasures.remove(treasure)
    wn.update()
