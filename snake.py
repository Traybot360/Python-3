import turtle,random

class Cell:
  def __init__(self,t):
    self.x = 0
    self.y = 0
    #size of a cell
    self.cell_size = 10
    self.t = t
  def draw_cell(self,color):
    self.t.pu()
    self.t.goto(self.x,self.y)
    self.t.pd()
    self.t.color(color)
    self.t.begin_fill()
    for i in range(4):
      self.t.fd(self.cell_size)
      self.t.left(90)
    self.t.end_fill()
  def set_cell(self,x,y):
    self.x = x
    self.y = y

class Food:
  def __init__(self):
    self.t = turtle.Turtle()
    self.t.hideturtle()
    self.t.speed(0)
    self.cell = Cell(self.t)
    self.colors = ["red","green","yellow","blue","magenta", "cyan"]
  def create_food(self):
    multiplier = (200-self.cell.cell_size)/self.cell.cell_size
    self.cell.x = random.randint(0,multiplier)*self.cell.cell_size
    self.cell.y = random.randint(0,multiplier)*self.cell.cell_size

  def food_collision(self,x,y):
    if(self.cell.x == x and y == self.cell.y):
      return True
    else: 
      return False
  def draw_food(self):
    self.t.clear()
    turtle.tracer(0,0)
    self.cell.draw_cell(self.cell.x,self.cell.y,random.choice(self.colors))
    turtle.tracer(20,0)

class Snake:
  def __init__(self):
    self.snake = []
    self.direction = "Right"
    self.begin_length = 5
    self.food = Food()
    self.food.draw_food()
    self.pen = turtle.Turtle()
    self.pen.hideturtle()
    self.pen.speed(0)
    self.speed = 400
    self.create_snake()

  def set_direction(self,value):
    if self.direction == "Right" and (value == "Up" or value == "Down"):
      self.direction = value
    if self.direction == "Left" and (value == "Up" or value == "Down"):
      self.direction = value
    if self.direction == "Up" and (value == "Left" or value == "Right"):
      self.direction = value
    if self.direction == "Down" and (value == "Left" or value == "Right"):
      self.direction = value
    
    self.check_snake()
  def food_collision(self,x,y):
    return self.food.food_collision(x,y)
  def self_collision(self):
    collision = False
    for cell in range(1,len(self.snake)):
      if self.snake[0].x == self.snake[cell].x and self.snake[0].y == self.snake[cell].y:
        collision = True
    return collision
  def border_collision(self):
    if(self.snake[0].x > 200 )






