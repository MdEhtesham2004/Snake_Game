from turtle import Turtle
# set up wizard completed
POSITIONS=[(0,0),(-20,0),(-40,0)]
SNAKE_COLOUR="white"
UP=90
DOWN=270
LEFT=180
RIGHT=0
class Snake:
    def __init__(self):
        self.segments=[]
        self.create_snake()
        self.head=self.segments[0]

    def create_snake(self):
        for postion in POSITIONS:
            self.add_segments(postion)

    def add_segments(self,postion):
        new_segment = Turtle("square")
        new_segment.color(SNAKE_COLOUR)
        new_segment.penup()
        new_segment.goto(postion)
        self.segments.append(new_segment)


    def extend(self):
        self.add_segments(self.segments[-1].position())
    def move(self):
        for seg_number in range(len(self.segments) - 1, 0, -1):  # going in reverse order
            random_x = self.segments[seg_number - 1].xcor()  # segment 2
            random_y = self.segments[seg_number - 1].ycor()  # segment 2 finding the location of 2nd segment
            self.segments[seg_number].goto(random_x, random_y)  # segment 3 moving seg 3 to seg2 position

        self.head.forward(20)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
