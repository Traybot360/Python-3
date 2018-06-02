import time,turtle


class Clock:
  def __init__(self,size):
     self.size = size
     self.turtles = []
     for i in range(5):
       self.turtles.append(turtle.Turtle())

  def get_s(self):
    return time.localtime().tm_sec
  def get_m(self):
    return time.localtime().tm_min
  def get_h(self):
    return time.localtime().tm_hour
  def border(self):
    self.turtles[0].hideturtle()
    self.turtles[0].circle(self.size)

  def seconds(self):
    self.turtles[1].clear()
    self.turtles[1].hideturtle()
    self.turtles[1].pu()
    self.turtles[1].goto(0,self.size)
    self.turtles[1].pd()
    self.turtles[1].color("red")
    self.turtles[1].seth((-1)*(self.get_s()*360/60-90))
    self.turtles[1].forward(self.size*0.8)
#360/12 for the hours
  def minutes(self):
    self.turtles[2].clear()
    self.turtles[2].hideturtle()
    self.turtles[2].pu()
    self.turtles[2].goto(0,self.size)
    self.turtles[2].pd()
    self.turtles[2].color("blue")
    self.turtles[2].seth((-1)*(self.get_m()*360/60-90))
    self.turtles[2].forward(self.size*0.65)

  def hours(self):
    self.turtles[3].clear()
    self.turtles[3].hideturtle()
    self.turtles[3].pu()
    self.turtles[3].goto(0,self.size)
    self.turtles[3].pd()
    self.turtles[3].color("green")
    self.turtles[3].seth((-1)*(self.get_h()*360/12-90))
    self.turtles[3].forward(self.size*.50)

    
clock = Clock(100)
while True:
  turtle.tracer(0,0)
  clock.border()
  clock.minutes()
  clock.seconds()
  clock.hours()
  
  turtle.tracer(20,0)

turtle.update()
